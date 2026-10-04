"""Compare direct DSD-to-stereo with buffered multichannel PCM downmix."""

import asyncio
import math
import sys

from music_assistant.helpers.ffmpeg import get_ffmpeg_stream
from music_assistant_models.enums import ContentType
from music_assistant_models.media_items import AudioFormat

SOURCE = sys.argv[1]

async def feed(data: bytes):
    for offset in range(0, len(data), 65536):
        yield data[offset : offset + 65536]

async def collect(stream) -> bytes:
    return b"".join([chunk async for chunk in stream])

def s24_samples(data: bytes):
    for offset in range(0, len(data), 3):
        sample = data[offset] | (data[offset + 1] << 8) | (data[offset + 2] << 16)
        yield sample - (1 << 24) if sample & (1 << 23) else sample

async def main() -> None:
    dsd = AudioFormat(content_type=ContentType.DSF, sample_rate=352800, bit_depth=8, channels=6)
    surround_float = AudioFormat(
        content_type=ContentType.PCM_F32LE, sample_rate=176400, bit_depth=32, channels=6
    )
    stereo_s24 = AudioFormat(
        content_type=ContentType.PCM_S24LE, sample_rate=176400, bit_depth=24, channels=2
    )
    direct = await collect(
        get_ffmpeg_stream(SOURCE, dsd, stereo_s24, extra_output_args=["-t", "2"])
    )
    buffered = await collect(
        get_ffmpeg_stream(SOURCE, dsd, surround_float, extra_output_args=["-t", "2"])
    )
    staged = await collect(
        get_ffmpeg_stream(
            feed(buffered),
            surround_float,
            stereo_s24,
            preserve_dsd_downmix_gain=True,
        )
    )
    assert len(direct) == len(staged) > 0, (len(direct), len(staged))

    count = equal = max_diff = 0
    sum_a = sum_b = sum_aa = sum_bb = sum_ab = 0
    for a, b in zip(s24_samples(direct), s24_samples(staged), strict=True):
        diff = abs(a - b)
        count += 1
        equal += diff == 0
        max_diff = max(max_diff, diff)
        sum_a += a
        sum_b += b
        sum_aa += a * a
        sum_bb += b * b
        sum_ab += a * b
    gain = math.sqrt(sum_bb / sum_aa)
    correlation = (count * sum_ab - sum_a * sum_b) / math.sqrt(
        (count * sum_aa - sum_a * sum_a) * (count * sum_bb - sum_b * sum_b)
    )
    exact_ratio = equal / count
    print(
        f"direct={len(direct)} bytes buffered_6ch_f32={len(buffered)} bytes "
        f"staged={len(staged)} bytes gain={gain:.9f} correlation={correlation:.12f} "
        f"max_diff={max_diff} LSB exact={exact_ratio:.2%}"
    )
    assert abs(gain - 1) < 1e-6 and correlation > 0.999999 and max_diff <= 1

asyncio.run(main())
