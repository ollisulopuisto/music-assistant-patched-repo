# Bolt Journal

This journal records critical performance learnings, anti-patterns, and insights discovered in this repository.

## 2026-11-01 - Avoid Reading Entire Patch Files for Header Metadata
**Learning:** Git format patches contain commit metadata in the top 10 lines followed by potentially huge diff blocks (tens or hundreds of kilobytes). Reading the entire file via `read_text()` and running a multiline regex across the full text causes unnecessary memory allocations and I/O overhead.
**Action:** Stream the file line-by-line and stop as soon as the `Subject:` header or diff boundary (`diff --git `) is reached.

## 2026-11-03 - Stream Line-by-Line for Top Changelog Entry Check
**Learning:** Checking whether a published version already exists at the top of a large cumulative changelog (several thousand lines / >200KB) by reading and decoding the entire file into memory causes unnecessary heap allocations and disk I/O, especially when performing early-exit guards before remote network calls.
**Action:** Stream the file line-by-line and inspect only until the first markdown header (`## `) is reached.

## 2026-11-04 - Stream Prepending with Chunked Remainder Copying
**Learning:** Prepending new entries to a large cumulative changelog by reading the whole file into a string, stripping the header, and concatenating strings incurs multiple multi-megabyte heap allocations and string re-encodings. Conversely, pure line-by-line looping across thousands of lines in Python adds interpreter overhead compared to chunked copying.
**Action:** Scan line-by-line only to the first entry header (`## `) and then stream the remainder using `shutil.copyfileobj(src, dst)` to copy directly in large chunks.

## 2026-11-05 - Stream Patch Headers in Binary Mode to Avoid TextIOWrapper Overhead
**Learning:** Opening patch files in text mode (`open("r", encoding="utf-8")`) creates a Python `TextIOWrapper` and decodes every line from bytes to UTF-8 strings. Since patch metadata headers and diff markers are standard ASCII prefixes (`b"Subject:"`, `b"diff --git "`), reading line-by-line in binary mode (`open("rb")`) bypasses decoder initialization and per-line string object allocations for non-matching lines.
**Action:** Stream line-by-line using binary mode (`open("rb")`) and inspect byte prefixes directly, decoding only the target title line to UTF-8.

## 2026-11-06 - Binary Mode Streaming for Changelog Top Entry Check
**Learning:** Checking whether a published version already exists at the top of the changelog using text mode (`open("r", encoding="utf-8")`) initializes `TextIOWrapper` and creates Python string objects for every header and comment line scanned until the first entry. Opening in binary mode (`open("rb")`) and matching byte prefixes (`b"## "`) against UTF-8 encoded target bytes cuts execution time by ~38% without decoding strings on non-matching lines.
**Action:** Stream markdown headers in binary mode (`open("rb")`) when looking for entry markers before doing full string processing.

## 2026-11-08 - Binary Mode Streaming with Chunked Copying for File Prepending
**Learning:** Prepending entries to large markdown files by opening in text mode (`open("r")` / `open("w")`) forces `shutil.copyfileobj` to process characters through `TextIOWrapper`, continuously decoding UTF-8 bytes to Python `str` objects from the source and re-encoding them back to bytes for the destination. Opening in binary mode (`open("rb")` / `open("wb")`) and matching byte markers (`b"## "`) allows `shutil.copyfileobj` to copy raw byte blocks directly via OS read/write buffers, cutting prepending execution time by ~48%.
**Action:** Use binary mode (`open("rb")` and `open("wb")`) when copying large file remainders with `shutil.copyfileobj` after header manipulation.
