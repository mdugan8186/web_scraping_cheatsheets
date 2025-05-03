# ==== curl_cffi ====

# https://curl-cffi.readthedocs.io/en/latest/

# ==========================
# == OBJECTIVE ==
# Cheat sheet for using `curl_cffi`, a stealth HTTP client that mimics real browser behavior
# using TLS/JA3 fingerprinting, HTTP/2, ALPN, and header impersonation. Excellent for bypassing
# bot protection and scraping JavaScript-heavy or cloudflare-protected sites.
# ==========================

# region == What Is curl_cffi? ==
"""
- curl_cffi is a Python wrapper around libcurl written in CFFI
- Supports:
  ✅ TLS fingerprint spoofing (JA3)
  ✅ HTTP/2 and ALPN negotiation
  ✅ Header impersonation for browsers (Chrome, Safari, Firefox)
  ✅ Seamless proxy support
  ✅ Built-in retry and timeout handling

- Best for scraping high-security websites that block `requests`, `httpx`, and Selenium.
"""
# endregion

# region == Installation ==
"""
# Requires a Rust toolchain (for building cffi extensions)

# macOS/Linux
pip install curl-cffi --upgrade

# Windows (requires curl prebuilt DLLs or WSL)

For full browser impersonation:
pip install curl-cffi[http2]
"""
# endregion

# region == Basic GET Request ==

from curl_cffi import requests
r = requests.get("https://example.com")
print(r.status_code)
print(r.text)
# endregion

# region == Impersonating a Real Browser ==
r = requests.get("https://example.com", impersonate="chrome110")
print(r.request.headers["user-agent"])
"""
Available browser impersonation options:
- chrome110
- chrome99
- safari15_3
- safari15_5
- firefox102
"""
# endregion

# region == Passing Headers, Cookies, and Params ==
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
# endregion

# region == Using Proxies ==
"""
Supports HTTP/SOCKS proxies in standard format:
- http://user:pass@host:port
- socks5h://user:pass@host:port
"""

r = requests.get(
    "https://example.com",
    impersonate="chrome110",
    proxies={"http": "http://user:pass@ip:port"}
)
# endregion

# region == Handling POST Requests ==
payload = {"username": "admin", "password": "secret"}
r = requests.post(
    "https://example.com/api/login",
    impersonate="firefox102",
    json=payload
)
print(r.status_code)
# endregion

# region == Timeout and Retry Control ==
r = requests.get(
    "https://example.com",
    impersonate="chrome110",
    timeout=10,
    max_retries=3
)
# endregion

# region == Why Use curl_cffi Over requests/httpx? ==
"""
✅ Built-in browser-like TLS fingerprinting (JA3)
✅ HTTP/2 support with realistic ALPN
✅ Bypasses many bot protections (e.g. Cloudflare)
✅ Better stealth than Selenium or Playwright for HTTP scraping

⚠️ Cannot execute JavaScript (unlike a browser)
⚠️ May need extra setup on Windows
"""
# endregion

# region == Best Practices ==
"""
✅ Always use impersonate= with a real browser string
✅ Combine with rotating proxies and headers
✅ Use curl_cffi for protected endpoints, not static HTML
✅ Use DevTools to extract real headers and test in curl_cffi
"""
# endregion

# region == curl_cffi vs Other Tools ==
"""
| Feature           | requests | httpx | curl_cffi | Selenium |
|-------------------|----------|-------|-----------|----------|
| TLS Fingerprint   | ❌       | ❌     | ✅        | ✅       |
| HTTP/2 + ALPN     | ❌       | Partial| ✅        | ✅       |
| JS Execution      | ❌       | ❌     | ❌        | ✅       |
| Proxy Support     | ✅       | ✅     | ✅        | ✅       |
| Headless Evasion  | ❌       | ❌     | ✅        | ⚠️ (detectable) |
"""
# endregion

# region == Documentation ==
# Official Docs: https://curl-cffi.readthedocs.io/en/latest/
# GitHub: https://github.com/yifeikong/curl_cffi
# Cloudflare Challenges: https://github.com/DaRealFreak/cloudflare-scrape-js2py
# endregion
