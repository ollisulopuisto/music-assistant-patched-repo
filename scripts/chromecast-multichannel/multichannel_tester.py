"""Cast one 5.1 file to a Chromecast in several formats to see which reaches the AVR as 5.1.

Untested hypotheses; see docs/chromecast-multichannel-roadmap.md.
Requires: pip install pychromecast flask; ffmpeg on PATH.
"""

import os
import subprocess
import threading
import pychromecast
from flask import Flask, Response

# CONFIGURATION
CAST_DEVICE_NAME = os.environ.get("CAST_DEVICE_NAME", "Ultracast TV")
SOURCE_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "..", "test-media", "5.1-channel-identification.flac",
)
SERVER_PORT = 8088
SERVER_IP = os.environ.get("SERVER_IP", "192.168.1.222")  # this machine's LAN IP

app = Flask(__name__)

def get_ffmpeg_command(mode):
    """Generate FFmpeg command for the given mode."""
    base = ["ffmpeg", "-re", "-i", SOURCE_FILE]
    if mode == "flac":
        # Direct FLAC streaming
        return base + ["-c:a", "flac", "-f", "flac", "pipe:1"]
    elif mode == "ac3":
        # Transcode to AC3 in MP4 container (common for cast)
        # Note: we use fragmenting for streaming MP4
        return base + ["-c:a", "ac3", "-b:a", "640k", "-f", "mp4", "-movflags", "frag_keyframe+empty_moov+default_base_moof", "pipe:1"]
    elif mode == "eac3":
        # Transcode to E-AC3 in MP4 container
        return base + ["-c:a", "eac3", "-b:a", "1024k", "-f", "mp4", "-movflags", "frag_keyframe+empty_moov+default_base_moof", "pipe:1"]
    elif mode == "mkv":
        # The "Video Trick" - MKV container, audio only
        return base + ["-c:a", "copy", "-f", "matroska", "pipe:1"]
    return None

@app.route('/stream/<mode>')
def stream_audio(mode):
    cmd = get_ffmpeg_command(mode)
    if not cmd:
        return "Invalid mode", 400
    
    def generate():
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        try:
            while True:
                chunk = process.stdout.read(4096)
                if not chunk:
                    break
                yield chunk
        finally:
            process.terminate()

    # Determine MIME type based on mode and Google Docs
    mime_types = {
        "flac": "audio/flac",
        "ac3": 'audio/mp4; codecs="ac-3"',
        "eac3": 'audio/mp4; codecs="ec-3"',
        "mkv": "video/x-matroska"
    }
    
    return Response(generate(), mimetype=mime_types.get(mode, "audio/flac"))

def run_flask():
    app.run(host='0.0.0.0', port=SERVER_PORT, threaded=True)

# 1. Start Flask in background
flask_thread = threading.Thread(target=run_flask, daemon=True)
flask_thread.start()

# 2. Discovery
print(f"Searching for {CAST_DEVICE_NAME}...")
chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[CAST_DEVICE_NAME])
if not chromecasts:
    print(f"Could not find {CAST_DEVICE_NAME}")
    raise SystemExit(1)

cast = chromecasts[0]
cast.wait()
print(f"Connected to {cast.friendly_name} ({cast.model_name})")

# 3. Test Loop
modes = ["flac", "ac3", "eac3", "mkv"]
print("\n--- MULTICHANNEL TESTER ---")
print("Available modes: flac, ac3, eac3, mkv")
print("Enter a mode to start casting, or 'q' to quit.")

try:
    while True:
        mode = input("\nSelect mode: ").strip().lower()
        if mode == 'q':
            break
        if mode not in modes:
            print(f"Invalid mode. Try: {', '.join(modes)}")
            continue
        
        url = f"http://{SERVER_IP}:{SERVER_PORT}/stream/{mode}"
        mime = {
            "flac": "audio/flac",
            "ac3": 'audio/mp4; codecs="ac-3"',
            "eac3": 'audio/mp4; codecs="ec-3"',
            "mkv": "video/x-matroska"
        }[mode]
        
        print(f"Casting {mode} to {CAST_DEVICE_NAME}...")
        print(f"URL: {url}")
        print(f"MIME: {mime}")
        
        cast.media_controller.play_media(url, content_type=mime)
        cast.media_controller.block_until_active()
        print("Playback active. Check AVR.")

except KeyboardInterrupt:
    pass
finally:
    pychromecast.discovery.stop_discovery(browser)
