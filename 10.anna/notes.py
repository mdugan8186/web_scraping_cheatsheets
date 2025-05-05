# ==== anna ====

# https://github.com/777777miSS/anna

# ==========================
# == OBJECTIVE ==
# Cheat sheet for `anna`, a high-performance, async, stealth-focused HTTP client for web scraping.
# Designed to bypass bot protection using browser fingerprints and TLS mimicking.
# Built with Rust and exposes a Python interface similar to `httpx`, but with stealth baked in.
# ==========================

"""
`anna` is an async-first stealth HTTP client for Python.
Built in Rust and powered by `hyper`, it mimics real browser behavior
to bypass advanced bot protection (JA3/TLS, ALPN, headers, etc.).

Use cases:
✅ Bypass Cloudflare, Akamai, and fingerprinting blocks
✅ Scale async scraping pipelines with stealth
✅ Replace headless browsers for JSON/API scraping
"""

# --------------------------
# Installation
# --------------------------

"""
# Install Rust if not already installed:
brew install rustup
rustup-init

# Then install anna (Python 3.8+)
pip install git+https://github.com/777777miSS/anna.git
"""

# --------------------------
# Basic GET Request
# --------------------------

import asyncio
from anna import request


async def main():
    resp = await request("GET", "https://example.com")
    print(resp.status)
    print(await resp.text())

asyncio.run(main())

# --------------------------
# Custom Headers and Browser Fingerprinting
# --------------------------

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

# --------------------------
# Supported Fingerprints
# --------------------------

"""
anna fingerprint options:
- chrome_118
- firefox_118
- safari_16
- opera_105
- edge_118

Each fingerprint modifies:
- JA3 fingerprint
- TLS cipher suite
- ALPN order
- Default headers
"""

# --------------------------
# POST Request
# --------------------------


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

# --------------------------
# Using Proxies
# --------------------------


async def proxied_request():
    resp = await request(
        "GET",
        "https://example.com",
        proxy="http://user:pass@proxy_ip:port",
        fingerprint="firefox_118"
    )
    print(resp.status)

asyncio.run(proxied_request())

# --------------------------
# Error Handling
# --------------------------


async def safe_request():
    try:
        resp = await request("GET", "https://bad-url.com")
        print(resp.status)
    except Exception as e:
        print("Request failed:", e)

asyncio.run(safe_request())

# --------------------------
# Why Use `anna`?
# --------------------------

"""
✅ Async support for high-speed concurrent scraping
✅ Browser-like TLS, ALPN, and header fingerprinting
✅ Great stealth vs Cloudflare, Akamai, Imperva, etc.
✅ Faster and lighter than Selenium or Playwright

⚠️ Still new — not as widely documented
⚠️ No JS execution — use for APIs or static JSON endpoints
"""

# --------------------------
# Best Practices
# --------------------------

"""
✅ Always use a fingerprint string (e.g., chrome_118)
✅ Combine with rotating proxies and User-Agent strings
✅ Use browser DevTools to extract headers and tokens
✅ Ideal for scraping structured data (not full-page rendering)
"""

# --------------------------
# Feature Comparison (commented table)
# --------------------------

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

# --------------------------
# Documentation
# --------------------------

"""
GitHub (anna):
https://github.com/777777miSS/anna

Open Issues/Discussions:
https://github.com/777777miSS/anna/issues

Related Project (`tls-py`):
https://github.com/777777miSS/tls-py
"""
