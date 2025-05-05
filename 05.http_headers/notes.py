# ==== http_headers ====

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

# ==========================
# == OBJECTIVE ==
# Cheat sheet for working with HTTP headers in web scraping.
# Covers request/response headers, browser spoofing, session persistence,
# and integration with libraries like `requests`, `httpx`, `curl_cffi`, and `Scrapy`.
# ==========================

"""
HTTP headers are key-value pairs sent between the client and server.
They control metadata like content format, user identity, authentication, and caching.

They are critical in web scraping to:
- Mimic real browser behavior
- Avoid basic bot detection
- Pass authentication tokens and cookies
"""

# --------------------------
# Common Request Headers
# --------------------------

"""
User-Agent: Identifies the client (browser, bot, etc.)
Accept: Tells the server what content types are accepted
Accept-Language: Preferred languages
Referer: The page that linked to the current request
Connection: Controls TCP connection behavior
Host: The domain of the target server (usually auto-set)
Authorization: Bearer tokens or Basic Auth credentials
X-Requested-With: Often used by JavaScript apps to identify AJAX requests
"""

# --------------------------
# Example Headers Dictionary
# --------------------------

import requests
from curl_cffi import requests as stealth_requests
import scrapy
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive"
}

# --------------------------
# Setting Headers with requests
# --------------------------


response = requests.get("https://httpbin.org/headers", headers=headers)
print(response.status_code)
print(response.json())

# --------------------------
# Using Session with Persistent Headers
# --------------------------

session = requests.Session()
session.headers.update(headers)
session.get("https://example.com/page1")
session.get("https://example.com/page2")  # headers persist

# Override per request
override = {"User-Agent": "CustomAgent/1.0"}
response = session.get("https://example.com/override", headers=override)

# --------------------------
# Viewing Response Headers
# --------------------------

response = requests.get("https://example.com")
print(response.headers)  # All headers
print(response.headers.get("Content-Type"))  # e.g., text/html

# --------------------------
# Scrapy: Setting Headers in Request
# --------------------------


class ExampleSpider(scrapy.Spider):
    name = "example"

    def start_requests(self):
        yield scrapy.Request(
            url="https://example.com",
            headers={
                "User-Agent": "Mozilla/5.0",
                "Referer": "https://google.com"
            }
        )

# --------------------------
# curl_cffi: Real Browser Headers (JA3 + TLS Spoofing)
# --------------------------


response = stealth_requests.get("https://example.com", impersonate="chrome110")
print(response.request.headers)

"""
curl_cffi auto-generates:
- Realistic User-Agent, Accept, Accept-Language, etc.
- TLS fingerprints and JA3 hashes that match real browsers
"""

# --------------------------
# Best Practices
# --------------------------

"""
✅ Use a real User-Agent string (get from browser DevTools)
✅ Set Accept and Accept-Language to match a real browser
✅ Use Referer if scraping from link chains (e.g., from search engines)
✅ Use a session object for multi-page scraping
✅ Add X-Requested-With: XMLHttpRequest for AJAX requests
✅ Combine headers with cookies and proxy rotation

⚠️ Don’t rely only on headers — many sites inspect TLS fingerprint and JS behavior
⚠️ Avoid default Python headers; they are detectable
⚠️ Don’t send Authorization headers unless required (may trigger rate-limiting)
"""

# --------------------------
# How to Copy Real Headers from Your Browser
# --------------------------

"""
1. Open DevTools (F12 or right-click → Inspect)
2. Go to the Network tab
3. Reload the page
4. Click a request → Headers → Request Headers
5. Copy the full header block into your script
"""

# --------------------------
# Testing and Debugging Tools
# --------------------------

"""
Test how your headers appear:

- https://httpbin.org/headers
- https://www.whatsmyua.info/
- https://www.httpwatch.com/httpgallery/
- https://requestbin.com/
"""

# --------------------------
# Documentation
# --------------------------

"""
MDN HTTP Headers Reference:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

curl_cffi Docs:
https://curl-cffi.readthedocs.io/en/latest/

Scrapy Headers:
https://docs.scrapy.org/en/latest/topics/request-response.html#request-headers

requests Custom Headers:
https://requests.readthedocs.io/en/latest/user/quickstart/#custom-headers
"""
