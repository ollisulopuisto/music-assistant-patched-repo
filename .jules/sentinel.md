# Sentinel Journal

This journal records critical security learnings, vulnerability patterns, and architectural constraints discovered in this repository.

## 2026-11-04 - Origin-based Credential Stripping on HTTP Redirects
**Vulnerability:** Credential leakage (`Authorization` header / API tokens) across scheme downgrades (HTTPS -> HTTP) or port changes when redirect validation only checks `req.host`.
**Learning:** Checking `req.host.lower() != new_req.host.lower()` in `urllib.request.HTTPRedirectHandler` only detects hostname changes, not scheme downgrades or destination port switches. An attacker able to trigger or influence redirects to `http://` on the same host or a different listening port could intercept sensitive authorization tokens in plaintext or via unintended services.
**Prevention:** Always perform full same-origin verification (scheme, normalized hostname, and port) before retaining sensitive authentication headers across HTTP redirects.

## 2026-11-05 - Restricting Target Schemes in HTTP Redirect Handlers
**Vulnerability:** SSRF / arbitrary local or protocol access via cross-scheme HTTP redirects (e.g. `file://`, `gopher://`, `ftp://`).
**Learning:** Python's standard `urllib.request.HTTPRedirectHandler` follows HTTP 3xx redirects to any handler recognized by `OpenerDirector` (including `FileHandler` and `FTPHandler`) unless `redirect_request` rejects the target scheme.
**Prevention:** In custom `HTTPRedirectHandler` subclasses, validate that redirect destination schemes are strictly restricted to expected protocols (`http`, `https`) and return `None` to abort redirection to unsupported or dangerous URI schemes.
