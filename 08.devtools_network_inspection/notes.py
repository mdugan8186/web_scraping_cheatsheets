# ==== devtools_network_inspection ====

# https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor

# ==========================
# == OBJECTIVE ==
# Cheat sheet for inspecting network traffic in browser DevTools to extract API calls,
# avoid parsing complex HTML, and reverse-engineer JavaScript-heavy websites for scraping.
# ==========================

"""
Modern websites often load data via JavaScript-powered API calls (XHR, Fetch).
Inspecting these in DevTools can reveal structured JSON data that's easier to scrape
than parsing raw HTML.

Benefits:
✅ Find clean backend API endpoints
✅ Avoid JavaScript-rendered DOM parsing
✅ Copy real headers/cookies/tokens for authenticated requests
"""

# --------------------------
# How to Open DevTools Network Panel
# --------------------------

"""
1. Open the target site in Chrome or Firefox.
2. Right-click → Inspect (or press F12)
3. Go to the **Network** tab.
4. Reload the page (F5 / Ctrl+R / Cmd+R)

You’ll now see traffic like:
- HTML / JS / CSS
- Images and Fonts
- XHR / Fetch (API calls)
"""

# --------------------------
# Filtering for API and Data Requests
# --------------------------

"""
Use filters in the Network tab:

- XHR → XMLHttpRequests (most API calls)
- Fetch → JS fetch requests
- `api`, `.json`, `search`, `product` → manual filters

Click a request → check:
- **Preview** tab (formatted)
- **Response** tab (raw content)
"""

# --------------------------
# Steps to Recreate an API Call
# --------------------------

"""
1. Identify an XHR or Fetch request that returns JSON data.
2. Click the request → go to **Headers**.
3. Copy:
   - Request URL
   - Method (GET, POST)
   - Query string or POST data
   - Headers (User-Agent, Accept, Referer, etc.)
   - Cookies (if present)
4. Test URL directly in your browser or Postman.

Once confirmed, rebuild it in code using `requests` or `httpx`.
"""

# --------------------------
# Example: Rebuilding an API Call with requests
# --------------------------


import requests
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://example.com"
}

params = {"q": "shoes", "limit": 10}
response = requests.get("https://example.com/api/search",
                        headers=headers, params=params)
print(response.json())

# --------------------------
# Copy as cURL → Convert to Python
# --------------------------

"""
1. Right-click request → Copy → "Copy as cURL"
2. Go to https://curlconverter.com/
3. Paste the cURL to auto-convert to Python `requests` code

It preserves:
✅ URL
✅ Headers
✅ Cookies
✅ POST data (for login, filters, etc.)
"""

# --------------------------
# Extracting Auth Headers or Tokens
# --------------------------

"""
APIs often require:

- Authorization: Bearer <token>
- X-CSRF-Token
- Set-Cookie headers

Steps:
1. Login manually
2. Trigger an action in the site (search, dashboard, etc.)
3. Look for those headers in related API calls
4. Copy and reuse them in your scraper
"""

# --------------------------
# Watching API Calls Live While Interacting
# --------------------------

"""
While DevTools is open:

- Click buttons, filters, tabs, paginate, etc.
- Observe triggered XHR/Fetch calls
- Preview tab shows JSON for products, metadata, etc.

Tips:
- Sort by Time or Initiator to see what your action triggered
- Look at query params (e.g., page=2, category=shoes)
"""

# --------------------------
# Tools to Help With DevTools Inspection
# --------------------------

"""
- JSON Viewer (browser extension): formats JSON in Preview/Response tabs
- https://curlconverter.com: convert browser cURL into working Python code
- Copy → "Copy as fetch" (for Playwright-style automation)

Other Tools:
- Postman / Hoppscotch (API testing)
- Request Inspector: https://webhook.site or https://requestbin.com
"""

# --------------------------
# Best Practices
# --------------------------

"""
✅ Use DevTools to reverse-engineer clean JSON APIs
✅ Rebuild only working requests — avoid parsing rendered HTML
✅ Match headers/cookies as closely as possible
✅ Observe request order and dependencies (login → dashboard, etc.)

⚠️ Don't assume all API endpoints are stable — session tokens may expire
⚠️ Some endpoints are protected with CSRF or token verification
⚠️ Avoid scraping if a public/open API is already available
"""

# --------------------------
# Documentation
# --------------------------

"""
MDN - DevTools Network Monitor:
https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor

curlconverter (cURL to Python):
https://curlconverter.com/

Scrapy - XHR scraping:
https://docs.scrapy.org/en/latest/topics/practices.html#using-browser-devtools
"""
