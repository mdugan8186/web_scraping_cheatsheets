# ==== proxies_user_agents ====

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

# ==========================
# == OBJECTIVE ==
# Cheat sheet for using proxies and rotating User-Agent strings in web scraping.
# Covers HTTP/SOCKS proxy formats, rotation strategies, and anti-block best practices
# for `requests`, `Scrapy`, `Selenium`, and modern stealth tools.
# ==========================

# region == What Are Proxies and User-Agents? ==
"""
- A proxy routes your request through a different IP address.
- A User-Agent header identifies the client software (e.g., browser, device).

Using them is essential to:
- Avoid IP bans and rate limiting
- Mimic real browser traffic
- Rotate identities across scraping jobs
"""
# endregion

# region == Proxy Formats ==
"""
HTTP Proxy:
    http://USERNAME:PASSWORD@PROXY_IP:PORT
SOCKS5 Proxy:
    socks5h://USERNAME:PASSWORD@PROXY_IP:PORT
Free Proxy (no auth):
    http://123.45.67.89:8080
"""

# Example dictionary format (used in requests/httpx):
from curl_cffi import requests as stealth_requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
import requests


proxies = {
    "http": "http://USERNAME:PASSWORD@PROXY_IP:PORT",
    "https": "http://USERNAME:PASSWORD@PROXY_IP:PORT"
}
# endregion

# region == requests: Using Proxies and User-Agent ==

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
response = requests.get("https://example.com",
                        headers=headers, proxies=proxies)
print(response.status_code)
# endregion

# region == requests: Rotating User-Agent from a List ==

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0)"
]

headers = {"User-Agent": random.choice(user_agents)}
response = requests.get("https://example.com", headers=headers)
# endregion

# region == Scrapy: Rotate Proxies and User-Agents ==
# In settings.py:

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
]

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
}

ROTATING_PROXY_LIST = [
    "http://USERNAME:PASSWORD@proxy1.com:8000",
    "http://USERNAME:PASSWORD@proxy2.com:8000",
]

# Or use scrapy-rotating-proxies or scrapy-proxies extensions.
# endregion

# region == Selenium: Set User-Agent and Proxy ==

options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0)")
options.add_argument("--proxy-server=http://PROXY_IP:PORT")

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")
# endregion

# region == curl_cffi: Built-in Browser Fingerprint Spoofing ==

response = stealth_requests.get("https://example.com", impersonate="chrome110")
print(response.request.headers["user-agent"])
# Automatically handles fingerprint, TLS, and headers
# endregion

# region == Using Public Proxy APIs (Free/Rotating) ==
# Warning: public/free proxies are slow and often blocked
# Paid services include BrightData, ScraperAPI, Webshare.io, Zyte, and Oxylabs

# Sample (unreliable) free proxy list:
# https://free-proxy-list.net/
# https://proxylist.geonode.com/
# https://proxyscrape.com/
# endregion

# region == Best Practices ==
"""
✅ Rotate User-Agents and IPs together
✅ Use residential proxies or headless browsers for protected sites
✅ Retry failed proxies, blacklist dead ones
✅ Use separate sessions per proxy to isolate cookies
✅ Mimic real browsers (headers, TLS, Accept-Language)

⚠️ Avoid free proxies for commercial scraping
⚠️ Don't reuse IP + UA pairs in tight loops
⚠️ Avoid bot patterns (no JS, predictable intervals, etc.)
"""
# endregion

# region == Detection Tactics to Watch For ==
"""
- IP-based rate limits or bans
- Missing or inconsistent Accept/Referer headers
- Identical headers across requests
- Headless browser detection (Selenium, Playwright)
- JA3/TLS fingerprinting mismatches
- Session mismatch between requests

Use https://httpbin.org/headers or https://www.whatismybrowser.com/ to inspect your fingerprint.
"""
# endregion

# region == Documentation ==
# MDN User-Agent Header: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
# requests Proxies: https://docs.python-requests.org/en/latest/user/advanced/#proxies
# scrapy Proxies: https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#http-proxy
# curl_cffi Docs: https://curl-cffi.readthedocs.io/en/latest/
# endregion
