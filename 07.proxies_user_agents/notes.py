# ==== proxies_user_agents ====

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

# ==========================
# == OBJECTIVE ==
# Cheat sheet for using proxies and rotating User-Agent strings in web scraping.
# Covers HTTP/SOCKS proxy formats, rotation strategies, and anti-block best practices
# for `requests`, `Scrapy`, `Selenium`, and modern stealth tools.
# ==========================

"""
A proxy routes your request through a different IP address.
A User-Agent header identifies the client software (browser, OS, device).

Together they help:
- Avoid IP bans and rate limiting
- Mimic real browser traffic
- Rotate identities across scraping jobs
"""

# --------------------------
# Proxy Formats
# --------------------------

"""
HTTP Proxy:
    http://USERNAME:PASSWORD@PROXY_IP:PORT
SOCKS5 Proxy:
    socks5h://USERNAME:PASSWORD@PROXY_IP:PORT
Free Proxy (no auth):
    http://123.45.67.89:8080
"""

from curl_cffi import requests as stealth_requests
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import random
import requests
proxies = {
    "http": "http://USERNAME:PASSWORD@PROXY_IP:PORT",
    "https": "http://USERNAME:PASSWORD@PROXY_IP:PORT"
}

# --------------------------
# requests: Using Proxies and User-Agent
# --------------------------


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

response = requests.get("https://example.com",
                        headers=headers, proxies=proxies)
print(response.status_code)

# --------------------------
# requests: Rotating User-Agent from a List
# --------------------------

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0)"
]

headers = {"User-Agent": random.choice(user_agents)}
response = requests.get("https://example.com", headers=headers)

# --------------------------
# Scrapy: Rotate Proxies and User-Agents
# --------------------------

"""
In settings.py:

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
"""

# --------------------------
# Selenium: Set User-Agent and Proxy
# --------------------------


options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0)")
options.add_argument("--proxy-server=http://PROXY_IP:PORT")

driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

# --------------------------
# curl_cffi: Built-in Browser Fingerprint Spoofing
# --------------------------


response = stealth_requests.get("https://example.com", impersonate="chrome110")
print(response.request.headers["user-agent"])

"""
curl_cffi automatically handles:
- TLS fingerprint spoofing (JA3)
- Accept-Language and other realistic headers
- Browser impersonation (Chrome, Safari, Firefox, etc.)
"""

# --------------------------
# Using Public Proxy APIs (Free/Rotating)
# --------------------------

"""
⚠️ Warning: public proxies are often slow, unreliable, or blocked

Free proxy lists:
- https://free-proxy-list.net/
- https://proxyscrape.com/
- https://proxylist.geonode.com/

Paid proxy providers:
- BrightData
- Webshare.io
- ScraperAPI
- Zyte
- Oxylabs
"""

# --------------------------
# Best Practices
# --------------------------

"""
✅ Rotate User-Agent + IP together
✅ Use session or cookie isolation per proxy
✅ Retry or blacklist failing proxies automatically
✅ Mimic real browsers (headers, Accept-Language, TLS)
✅ Randomize delays between requests

⚠️ Avoid free proxies for commercial use
⚠️ Don’t reuse the same IP + User-Agent combo in a tight loop
⚠️ Don’t ignore JavaScript-based bot detection (use stealth tools)
"""

# --------------------------
# Detection Tactics to Watch For
# --------------------------

"""
Sites may detect you if:
- Requests come too quickly from same IP
- User-Agent doesn't match TLS fingerprint
- Headless browsers are detected (e.g., Selenium)
- Cookies or sessions are inconsistent
- Headers are missing or too uniform

Use these tools to inspect your footprint:
- https://httpbin.org/headers
- https://www.whatismybrowser.com/
"""

# --------------------------
# Documentation
# --------------------------

"""
MDN - User-Agent:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent

requests - Proxies:
https://docs.python-requests.org/en/latest/user/advanced/#proxies

Scrapy Proxy Middleware:
https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#http-proxy

curl_cffi:
https://curl-cffi.readthedocs.io/en/latest/
"""
