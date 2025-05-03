# ==== anna ====

# https://github.com/777777miSS/anna

# ==========================
# == OBJECTIVE ==
# Cheat sheet for `anna`, a high-performance, async, stealth-focused HTTP client for web scraping.
# Designed to bypass bot protection using browser fingerprints and TLS mimicking.
# Built with Rust and exposes a Python interface similar to `httpx`, but with stealth baked in.
# ==========================

# region == What is `anna`? ==
"""
- `anna` is a modern, stealth HTTP client built on Rust and `hyper`, with Python bindings.
- Supports:
  ✅ Async requests using Python's asyncio
  ✅ TLS JA3 fingerprint spoofing
  ✅ HTTP/2 and ALPN
  ✅ Header and TLS fingerprint mimicry of browsers
  ✅ Extremely fast and stealthy

Why use it:
- To avoid blocks on sites protected by Cloudflare, Akamai, or fingerprinting tools
- To scale up async scraping with high throughput and stealth
"""
# endregion

# region == Installation ==
"""
# Install Rust if not already present
# macOS/Linux
brew install rustup
rustup-init

# Then install `anna`
pip install git+https://github.com/777777miSS/anna.git

# Note: Requires Python 3.8+, Rust toolchain, and `maturin` (may auto-install)
"""
# endregion

# region == Basic GET Request ==
import asyncio
from anna import request


async def main():
    resp = await request("GET", "https://example.com")
    print(resp.status)
    print(await resp.text())

asyncio.run(main())
# endregion

# region == Custom Headers and Browser Fingerprinting ==
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "application/json",
    "Referer": "https://google.com"
}


async def fetch_with_headers():
    resp = await request(
        "GET",
        "https://example.com/api",
        headers=headers,
        fingerprint="chrome_118"
    )
    print(await resp.json())

asyncio.run(fetch_with_headers())
# endregion

# region == Supported Fingerprints ==
"""
These tell `anna` which browser+OS profile to mimic:
- chrome_118
- firefox_118
- safari_16
- opera_105
- edge_118

This adjusts:
- JA3 fingerprint
- TLS cipher suites
- ALPN negotiation
- User-Agent and Accept headers
"""
# endregion

# region == Sending POST Requests ==


async def login():
    payload = {"email": "user@example.com", "password": "pass123"}
    resp = await request(
        "POST",
        "https://example.com/login",
        json=payload,
        fingerprint="chrome_118"
    )
    print(await resp.text())

asyncio.run(login())
# endregion

# region == Using Proxies ==


async def proxied_request():
    resp = await request(
        "GET",
        "https://example.com",
        proxy="http://user:pass@proxyip:port",
        fingerprint="firefox_118"
    )
    print(resp.status)

asyncio.run(proxied_request())
# endregion

# region == Error Handling ==


async def safe_request():
    try:
        resp = await request("GET", "https://bad-url.com")
        print(resp.status)
    except Exception as e:
        print("Request failed:", e)

asyncio.run(safe_request())
# endregion

# region == Why Use `anna`? ==
"""
✅ Designed for stealth scraping on modern protected websites
✅ Async — great for concurrent scraping pipelines
✅ Browser-level fingerprinting
✅ Faster and less detectable than Selenium or Playwright

⚠️ Still under active development — not as battle-tested as requests/httpx
⚠️ Less documentation than curl_cffi
"""
# endregion

# region == Best Practices ==
"""
✅ Always use a fingerprint string to mimic real browsers
✅ Combine with rotating proxies and user-agents
✅ Use asyncio for batch/concurrent scraping
✅ Capture headers and cookies from DevTools to feed into requests
"""
# endregion

# region == anna vs Other Tools ==
"""
| Feature           | requests | curl_cffi | anna     | Selenium |
|-------------------|----------|-----------|----------|----------|
| TLS Fingerprint   | ❌       | ✅        | ✅       | ✅       |
| HTTP/2 + ALPN     | ❌       | ✅        | ✅       | ✅       |
| JS Execution      | ❌       | ❌        | ❌       | ✅       |
| Async Support     | ❌       | ❌        | ✅       | ❌       |
| Proxy Support     | ✅       | ✅        | ✅       | ✅       |
| Browser Mimicry   | ❌       | ✅        | ✅       | ⚠️       |
"""
# endregion

# region == Documentation ==
# GitHub (source): https://github.com/777777miSS/anna
# Issues/Discussions: https://github.com/777777miSS/anna/issues
# Related project (`TLS-Py`): https://github.com/777777miSS/tls-py
# endregion
