FROM ghcr.io/ollisulopuisto/ma-server-patched:2.10.4-upnext.11 AS patched

COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
COPY music_assistant-2.10.4+upnext.14-py3-none-any.whl /tmp/
COPY test-media/5.1-spoken-channel-identification.flac /tmp/ma_5.1_test.flac

RUN uv pip install \
    --python /app/venv/bin/python \
    --no-cache \
    --force-reinstall \
    --no-deps \
    /tmp/music_assistant-2.10.4+upnext.14-py3-none-any.whl \
    && rm /tmp/music_assistant-2.10.4+upnext.14-py3-none-any.whl

FROM patched AS verify_dsd
COPY test-media/dst.dff /tmp/dst.dff
COPY verify_dsd_wrapper.py /tmp/verify_dsd_wrapper.py
RUN /app/venv/bin/python /tmp/verify_dsd_wrapper.py /tmp/dst.dff > /tmp/dsd-verification.txt

FROM patched
COPY --from=verify_dsd /tmp/dsd-verification.txt /usr/share/doc/ma-dsd-verification.txt
