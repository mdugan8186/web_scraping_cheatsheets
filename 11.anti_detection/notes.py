# ==== anti_detection ====

# https://intoli.com/blog/not-possible-to-block-chrome-headless/

# ==========================
# == OBJECTIVE ==
# Cheat sheet for evading detection while web scraping.
# Covers bot protection mechanisms, browser fingerprinting, proxy hygiene,
# headers, session management, and stealth tool selection.
# ==========================

"""
Sites use many detection techniques beyond IP blocking.
This guide helps you avoid common scraping pitfalls and mimic real user behavior effectively.

Covers:
✅ Headers and fingerprints
✅ Proxy usage and isolation
✅ Session persistence and cookies
✅ Request timing and behavior
✅ Tools with stealth built-in
"""

# --------------------------
# Common Detection Techniques
# --------------------------

"""
1. IP-based Blocking
   - Too many requests from same IP
   - Use of known data center IPs (AWS, GCP, etc.)
   - Country/geolocation mismatch

2. User-Agent / Headers
   - Missing or generic headers (e.g., "python-requests/2.31.0")
   - Inconsistent header order or values
   - Reused User-Agent + TLS fingerprint combos

3. TLS Fingerprinting (JA3)
   - Chrome vs Python TLS client fingerprint mismatch
   - ALPN order, ciphers, SNI values analyzed

4. JavaScript Fingerprinting
   - Detection of headless browser environment (e.g., `navigator.webdriver`)
   - Canvas/font/audio fingerprinting
   - Missing browser APIs or behavior differences

5. Behavior-Based Detection
   - No mouse movement, keyboard interaction
   - Instant page loads, no scrolling
   - Requests that skip normal navigation paths

6. Cookie and Session Fingerprinting
   - Re-using the same cookie across IPs
   - Invalid session headers
   - Missing authentication headers after login
"""

# --------------------------
# Essential Evasion Tactics
# --------------------------

"""
✅ Rotate IP addresses and User-Agent headers together
✅ Use real browser fingerprints (via curl_cffi, anna, or Selenium stealth plugins)
✅ Reuse session cookies across requests for authenticity
✅ Mimic real header structure (User-Agent, Accept, Referer, Accept-Language)
✅ Use DevTools to inspect real user requests and replicate them exactly
✅ Add realistic delays or randomized sleeps between requests
✅ Always obey robots.txt and Terms of Service when appropriate
"""

# --------------------------
# Tooling Overview
# --------------------------

"""
Tool Comparison:

| Tool        | JS Support | TLS Fingerprint | HTTP/2 | Async | Headless |
|-------------|------------|------------------|--------|--------|-----------|
| requests    | ❌         | ❌               | ❌     | ❌     | N/A       |
| httpx       | ❌         | ❌               | ⚠️     | ✅     | N/A       |
| curl_cffi   | ❌         | ✅               | ✅     | ❌     | N/A       |
| anna        | ❌         | ✅               | ✅     | ✅     | N/A       |
| Selenium    | ✅         | ✅ (limited)     | ✅     | ❌     | ✅        |
| Playwright  | ✅         | ✅ (stealth)     | ✅     | ✅     | ✅        |

Recommended combos:
- Static JSON/API: `curl_cffi`, `anna`
- Dynamic pages: `Playwright` with stealth plugin
"""

# --------------------------
# Best Practices by Category
# --------------------------

# ✅ Headers

"""
- Always set:
    - User-Agent (real browser string)
    - Accept
    - Accept-Language
    - Referer (if coming from another site)
- Use DevTools to copy real headers
- Maintain consistent header sets across requests in a session
"""

# ✅ Proxies

"""
- Use residential or ISP proxies when possible
- Rotate proxies per session or per request if scraping at scale
- Match IP location with Accept-Language or time zone
- Avoid free proxies — they are often blacklisted
"""

# ✅ Cookies & Sessions

"""
- Login manually, then extract session cookies from DevTools
- Use `requests.Session()` or Selenium storage
- Reuse cookies across paginated data scraping
- Mimic login flow if scraping authenticated dashboards
"""

# ✅ Timing and Behavior

"""
- Add realistic delays between requests (1-5s)
- Use `time.sleep(random.uniform(a, b))` or `asyncio.sleep()`
- If scraping with Selenium/Playwright:
    - Scroll down the page
    - Click or interact with elements
    - Avoid making all requests instantly
"""

# --------------------------
# Detecting You’ve Been Blocked
# --------------------------

"""
Watch for:
- Sudden 403 Forbidden or 503 Service Unavailable responses
- HTML pages instead of JSON payloads
- Redirections to CAPTCHA pages
- Empty responses or JavaScript challenges
- Increased latency for each new request
"""

# --------------------------
# Debugging Evasion Issues
# --------------------------

"""
- Use https://httpbin.org/headers to test what your scraper is sending
- Compare your request to DevTools → Network tab
- Use browser fingerprint testers:
    - https://ja3er.com
    - https://bot.sannysoft.com/
    - https://amiunique.org
    - https://www.whatismybrowser.com/
- Test proxy IPs:
    - https://ipinfo.io
    - https://whoer.net
"""

# --------------------------
# Red Flags to Avoid
# --------------------------

"""
⚠️ Using default Python User-Agent
⚠️ Not sending Accept-Language or Referer
⚠️ Logging in and re-logging in every request
⚠️ Mixing proxy IPs with same cookie/session
⚠️ Making 100s of requests in under a minute
⚠️ Running scraping without verifying API or headers first
"""

# --------------------------
# Documentation
# --------------------------

"""
Bot Detection Explained (Intoli):
https://intoli.com/blog/not-possible-to-block-chrome-headless/

JA3 Fingerprints:
https://github.com/salesforce/ja3

DevTools Network Monitor:
https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor

curl_cffi Docs:
https://curl-cffi.readthedocs.io/en/latest/

anna GitHub:
https://github.com/777777miSS/anna
"""
