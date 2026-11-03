# Bolt Journal

This journal records critical performance learnings, anti-patterns, and insights discovered in this repository.

## 2026-11-01 - Avoid Reading Entire Patch Files for Header Metadata
**Learning:** Git format patches contain commit metadata in the top 10 lines followed by potentially huge diff blocks (tens or hundreds of kilobytes). Reading the entire file via `read_text()` and running a multiline regex across the full text causes unnecessary memory allocations and I/O overhead.
**Action:** Stream the file line-by-line and stop as soon as the `Subject:` header or diff boundary (`diff --git `) is reached.

## 2026-11-03 - Stream Line-by-Line for Top Changelog Entry Check
**Learning:** Checking whether a published version already exists at the top of a large cumulative changelog (several thousand lines / >200KB) by reading and decoding the entire file into memory causes unnecessary heap allocations and disk I/O, especially when performing early-exit guards before remote network calls.
**Action:** Stream the file line-by-line and inspect only until the first markdown header (`## `) is reached.
