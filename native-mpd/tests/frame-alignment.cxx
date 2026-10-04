// Regression for the CoreAudio output's byte-oriented ring buffer writes.
#include <algorithm>
#include <span>
#include <cstddef>
#include <cstdio>
#include <vector>
#include "util/RingBuffer.hxx"

int main(int argc, char **)
{
    const bool original = argc > 1;
    for (const std::size_t frame : {12u, 24u, 4u, 8u}) {
        for (const std::size_t capacity : {65536u, 17u, 257u}) {
            RingBuffer<std::byte> buffer(capacity);
            std::vector<std::byte> source(frame * 10000);
            std::vector<std::byte> received(frame * 7);
            for (std::size_t i = 0; i < source.size(); ++i)
                source[i] = std::byte(i % 251);
            std::size_t sent = 0, checked = 0;
            if (capacity < frame)
                continue;
            while (checked < source.size()) {
                const auto pending = std::span<const std::byte>(source).subspan(sent);
                const auto written = original ? buffer.WriteFrom(pending)
                    : buffer.WriteFramesFrom(pending, frame);
                if (written % frame != 0) {
                    std::fprintf(stderr, "Partial frame: %zu bytes, frame=%zu, capacity=%zu\n",
                                 written, frame, capacity);
                    return 1;
                }
                sent += written;
                const auto read = buffer.ReadTo(received);
                if (read % frame != 0 || (read == 0 && written == 0))
                    return 2;
                for (std::size_t i = 0; i < read; ++i)
                    if (received[i] != source[checked + i])
                        return 3;
                checked += read;
            }
        }
    }
    std::puts("PASS: complete stereo/5.1 frames and byte identity across buffer wraparound");
}
