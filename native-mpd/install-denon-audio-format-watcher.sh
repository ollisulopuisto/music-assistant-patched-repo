#!/bin/bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_file="$repo_root/native-mpd/denon-audio-format-watcher.swift"
install_dir="$HOME/.local/opt/denon-audio-format-watcher"
binary="$install_dir/denon-audio-format-watcher"
log_file="$install_dir/watcher.log"
label="fi.sulopuisto.denon-audio-format-watcher"
plist="$HOME/Library/LaunchAgents/$label.plist"
build_dir="$(mktemp -d "${TMPDIR:-/tmp}/denon-audio-watcher.XXXXXX")"
trap 'rm -rf "$build_dir"' EXIT

mkdir -p "$install_dir" "$(dirname "$plist")"
swiftc -module-cache-path "$build_dir/module-cache" \
  -framework CoreAudio -framework AudioToolbox \
  "$source_file" -o "$binary"
chmod 0755 "$binary"

cat > "$plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>$label</string>
  <key>ProgramArguments</key>
  <array>
    <string>$binary</string>
  </array>
  <key>RunAtLoad</key>
  <true/>
  <key>KeepAlive</key>
  <true/>
  <key>ProcessType</key>
  <string>Background</string>
  <key>StandardOutPath</key>
  <string>$log_file</string>
  <key>StandardErrorPath</key>
  <string>$log_file</string>
</dict>
</plist>
PLIST

uid="$(id -u)"
launchctl bootout "gui/$uid/$label" 2>/dev/null || true
launchctl bootstrap "gui/$uid" "$plist"
launchctl kickstart -k "gui/$uid/$label"
printf 'Installed and started %s\nLog: %s\n' "$label" "$log_file"
