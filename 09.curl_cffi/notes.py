# ==== curl_cffi ====

# https://curl-cffi.readthedocs.io/en/latest/

# ==========================
# == OBJECTIVE ==
# Cheat sheet for using `curl_cffi`, a stealth HTTP client that mimics real browser behavior
# using TLS/JA3 fingerprinting, HTTP/2, ALPN, and header impersonation. Excellent for bypassing
# bot protection and scraping JavaScript-heavy or cloudflare-protected sites.
# ==========================

"""
curl_cffi is a Python wrapper around libcurl using CFFI bindings.
It allows you to make stealthy HTTP requests that mimic real browser behavior.

Key features:
✅ TLS/JA3 fingerprint spoofing
✅ HTTP/2 and ALPN negotiation
✅ Browser impersonation (headers, order, priority)
✅ Seamless proxy support
✅ Built-in retry and timeout handling

Best for:
- Scraping Cloudflare-protected sites
- Avoiding bot detection on high-security pages
- Replacing unreliable headless browsers for API scraping
"""

# --------------------------
# Installation
# --------------------------

"""
# Requires Rust for CFFI build

pip install curl-cffi --upgrade
pip install curl-cffi[http2]   # for full browser impersonation
"""

# --------------------------
# Basic GET Request
# --------------------------


from curl_cffi import requests
r = requests.get("https://example.com")
print(r.status_code)
print(r.text)

# --------------------------
# Impersonating a Real Browser
# --------------------------

r = requests.get("https://example.com", impersonate="chrome110")
print(r.request.headers["user-agent"])

"""
Available impersonation values:
- chrome110
- chrome99
- safari15_3
- safari15_5
- firefox102
"""

# --------------------------
# Sending Headers, Cookies, and Params
# --------------------------

headers = {"x-api-key": "my-key"}
cookies = {"session": "abc123"}
params = {"q": "shoes"}

r = requests.get(
    "https://example.com/api/search",
    impersonate="chrome110",
    headers=headers,
    cookies=cookies,
    params=params
)
print(r.json())

# --------------------------
# Using Proxies
# --------------------------

"""
Supports:
- http://user:pass@host:port
- socks5h://user:pass@host:port
"""

r = requests.get(
    "https://example.com",
    impersonate="chrome110",
    proxies={"http": "http://user:pass@proxy_ip:port"}
)

# --------------------------
# POST Request
# --------------------------

payload = {"username": "admin", "password": "secret"}
r = requests.post(
    "https://example.com/api/login",
    impersonate="firefox102",
    json=payload
)
print(r.status_code)

# --------------------------
# Timeout and Retry Control
# --------------------------

r = requests.get(
    "https://example.com",
    impersonate="chrome110",
    timeout=10,
    max_retries=3
)

# --------------------------
# Why Use curl_cffi Instead of requests/httpx?
# --------------------------

"""
✅ Full TLS fingerprint and JA3 spoofing
✅ HTTP/2 and ALPN negotiation
✅ Works against Cloudflare, Akamai, and other bot mitigations
✅ Much stealthier than requests or httpx

⚠️ Cannot run JavaScript
⚠️ May require extra setup on Windows
"""

# --------------------------
# Best Practices
# --------------------------

"""
✅ Always use impersonate= with a realistic browser value
✅ Combine with rotating proxies and headers
✅ Use curl_cffi for difficult endpoints behind bot protection
✅ Extract real request headers from browser DevTools and reuse them
✅ Use timeout and retry logic for stability

⚠️ Avoid using curl_cffi to scrape raw HTML unless necessary
"""

# --------------------------
# Feature Comparison (as comment block)
# --------------------------

"""
Feature Comparison:

| Feature          | requests | httpx  | curl_cffi | Selenium |
|------------------|----------|--------|-----------|----------|
| TLS Fingerprint  | ❌       | ❌     | ✅        | ✅       |
| HTTP/2 + ALPN    | ❌       | Partial| ✅        | ✅       |
| JS Execution     | ❌       | ❌     | ❌        | ✅       |
| Proxy Support    | ✅       | ✅     | ✅        | ✅       |
| Headless Evasion | ❌       | ❌     | ✅        | ⚠️ (partial) |
"""

# --------------------------
# Documentation
# --------------------------

"""
curl_cffi Docs:
https://curl-cffi.readthedocs.io/en/latest/

GitHub Repo:
https://github.com/yifeikong/curl_cffi

Cloudflare Challenge Help:
https://github.com/DaRealFreak/cloudflare-scrape-js2py
"""
