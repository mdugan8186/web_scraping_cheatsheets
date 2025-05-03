# ==== http_headers ====

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers

# ==========================
# == OBJECTIVE ==
# Cheat sheet for working with HTTP headers in web scraping.
# Covers request headers, response headers, browser spoofing, session persistence,
# and integration with libraries like `requests`, `httpx`, `curl_cffi`, and `Scrapy`.
# ==========================

# region == What Are HTTP Headers? ==
"""
HTTP headers are key-value pairs sent between the client and server.
They control metadata like content format, user identity, authentication, and caching.

They are critical in web scraping to:
- Mimic real browser behavior
- Avoid basic bot detection
- Pass authentication tokens and cookies
"""
# endregion

# region == Common Request Headers to Set ==
"""
User-Agent: Identifies the client (browser, bot, etc.)
Accept: Tells the server what content types are accepted
Accept-Language: Preferred languages
Referer: The page that linked to the current request
Connection: Controls TCP connection behavior
Host: The domain of the target server (usually auto-set)
Authorization: Bearer tokens or Basic Auth credentials
X-Requested-With: Often used by JavaScript-based apps to identify Ajax requests
"""

# Example realistic browser headers:
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
# endregion

# region == Setting Headers with Requests ==

response = requests.get("https://example.com", headers=headers)
print(response.status_code)
if response and response.request:
    print(dict(response.request.headers))
else:
    print("Request object is missing or invalid.")
# endregion

# region == Using Headers with a Session Object ==
session = requests.Session()
session.headers.update(headers)
session.get("https://example.com/page1")
session.get("https://example.com/page2")
# Headers persist across all session requests
# endregion

# region == Modifying Headers Per Request ==
# You can override session headers for a single request:
custom_headers = {"User-Agent": "CustomAgent/1.0"}
response = session.get("https://example.com/override", headers=custom_headers)
# endregion

# region == Viewing Response Headers ==
response = requests.get("https://example.com")
print(response.headers)                # All headers
print(response.headers.get("Content-Type"))  # Specific header
# endregion

# region == Scrapy: Setting Headers in a Request ==
# Inside a Scrapy Spider class:


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
# endregion


# region == curl_cffi: Real Browser Headers (JA3 + TLS Spoofing) ==
# https://curl_cffi.readthedocs.io/

response = stealth_requests.get("https://example.com", impersonate="chrome110")
print(response.request.headers)
# Automatically includes real browser headers, JA3 fingerprint, and more
# endregion

# region == Best Practices ==
"""
✅ Use a real User-Agent string (get it from browser DevTools)
✅ Set Accept and Accept-Language for realistic requests
✅ Use Referer when scraping from linked pages
✅ Keep headers consistent across multi-page scraping (via session)
⚠️ Don't over-customize: overly fake headers can be suspicious
⚠️ Never send Authorization tokens unless required
"""
# endregion

# region == Testing Browser Headers ==
"""
To inspect your browser's real headers:

1. Open browser DevTools → Network tab
2. Reload the page
3. Click on a request → Headers → Request Headers
4. Copy them directly into your script

Example sites:
- https://httpbin.org/headers
- https://www.whatsmyua.info/
"""
# endregion

# region == Documentation ==
# MDN HTTP Headers Overview: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
# curl_cffi Docs: https://curl-cffi.readthedocs.io/en/latest/
# Scrapy Headers: https://docs.scrapy.org/en/latest/topics/request-response.html#request-headers
# endregion
