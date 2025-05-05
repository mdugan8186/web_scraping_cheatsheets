# ==== cookies_sessions ====

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

# ==========================
# == OBJECTIVE ==
# Cheat sheet for handling cookies and sessions in web scraping.
# Covers how to persist state across multiple requests, log in to websites,
# send and read cookies, and use session objects with `requests`, `Scrapy`, `Selenium`, etc.
# ==========================

"""
- Cookies are key-value pairs stored by the browser (or scraper) to maintain state.
- Sessions allow you to persist cookies and headers across multiple requests.

Use cases:
- Login authentication
- Cart/session tracking
- Avoiding CAPTCHAs repeatedly
"""

# --------------------------
# Manually Sending Cookies with requests
# --------------------------

from selenium import webdriver
import requests

cookies = {"sessionid": "abc123", "user": "michael"}
response = requests.get("https://example.com/dashboard", cookies=cookies)
print(response.text)

# --------------------------
# Reading Cookies from a Response
# --------------------------

response = requests.get("https://example.com")
print(response.cookies)  # <RequestsCookieJar>
for cookie in response.cookies:
    print(cookie.name, cookie.value)

# --------------------------
# Persistent Sessions with requests.Session
# --------------------------

session = requests.Session()
session.get("https://example.com/login")  # Sets cookies
session.get("https://example.com/profile")  # Cookies persist

# --------------------------
# Logging In with a Session
# --------------------------

payload = {"username": "myuser", "password": "mypassword"}
session = requests.Session()
response = session.post("https://example.com/login", data=payload)
dashboard = session.get("https://example.com/dashboard")
print(dashboard.text)

# --------------------------
# Session Headers (reused across requests)
# --------------------------

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})
session.get("https://example.com/page1")
session.get("https://example.com/page2")

# --------------------------
# Scrapy: Handling Cookies Automatically
# --------------------------

"""
Scrapy handles cookies automatically by default.
To disable cookie handling, set: COOKIES_ENABLED = False (in settings.py)
"""

# To inspect cookies from a response:


def parse(self, response):
    cookies = response.headers.getlist("Set-Cookie")
    yield {"cookies": cookies}

# --------------------------
# Selenium: Capturing Cookies from Browser
# --------------------------


driver = webdriver.Chrome()
driver.get("https://example.com")

cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie['name'], cookie['value'])

# Optional: Convert for use in requests
cookie_dict = {cookie['name']: cookie['value'] for cookie in cookies}
requests.get("https://example.com", cookies=cookie_dict)

# --------------------------
# Where to Find Cookies in DevTools
# --------------------------

"""
1. Open Chrome or Firefox
2. DevTools → Application → Storage → Cookies
3. Copy cookie names and values to use in scraping sessions
"""

# --------------------------
# Best Practices
# --------------------------

"""
✅ Use requests.Session() for multi-page scraping
✅ Capture cookies from browser sessions for login-required pages
✅ Use headers + cookies together to mimic real browsers
✅ Use one session per IP/proxy if rotating at scale
✅ Consider session re-use when scraping authenticated content

⚠️ Avoid re-logging in on every request — this will get you blocked
⚠️ Don't store cookies with authentication tokens in plain text
⚠️ Some cookies are domain- or path-specific — always match scope
"""

# --------------------------
# Documentation
# --------------------------

"""
MDN - Cookies:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies

requests - Cookies:
https://requests.readthedocs.io/en/latest/user/quickstart/#cookies

Scrapy - Cookie Middleware:
https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#cookiejar-middleware

Selenium - Cookies:
https://www.selenium.dev/documentation/webdriver/interactions/cookies/
"""
