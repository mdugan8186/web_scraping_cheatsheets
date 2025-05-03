# ==== devtools_network_inspection ====

# https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor

# ==========================
# == OBJECTIVE ==
# Cheat sheet for inspecting network traffic in browser DevTools to extract API calls,
# avoid parsing complex HTML, and reverse-engineer JavaScript-heavy websites for scraping.
# ==========================

# region == Why Use DevTools Network Tab? ==
"""
- Many modern websites use JavaScript to fetch data from backend APIs.
- These API calls often return structured JSON data that’s easier to scrape than HTML.
- Inspecting network requests helps avoid:
    - Anti-scraping markup obfuscation
    - Useless rendering elements
    - Complex parsing logic

You can:
✅ Find direct API endpoints
✅ Copy headers/cookies for authentication
✅ Mimic requests in code
"""
# endregion

# region == How to Open DevTools Network Panel ==
"""
1. Open the target website in Chrome or Firefox.
2. Right-click anywhere → "Inspect"
3. Go to the **Network** tab
4. Reload the page (F5 or ⌘R / Ctrl+R)

You’ll now see all network traffic made by the page — including:
- HTML, CSS, JS
- Images
- AJAX/Fetch/XHR requests (usually contain API data)
"""
# endregion

# region == Filtering for API and Data Requests ==
"""
Use the following filters in the Network tab:
- XHR → XML HTTP Requests (JSON, REST APIs)
- Fetch → Newer APIs (same purpose)
- Doc → Main page HTML
- JS → JavaScript files

You can also type filters like:
- `api`
- `.json`
- `search`
- `products`

Click a request → look in **Preview** and **Response** tabs to see data.
"""
# endregion

# region == Steps to Recreate API Calls ==
"""
1. Identify the request (XHR or Fetch) that returns the data you want.
2. Click it, then go to the **Headers** tab.
3. Copy:
    - Request URL
    - Request Method (GET/POST)
    - Query Parameters or JSON payload
    - Request Headers (especially User-Agent, Accept, Referer)
    - Cookies (if present)
4. Try the URL in your browser to verify it works.

✅ You can now recreate this request in Python using `requests` or `httpx`.
"""
# endregion

# region == Example: Rebuilding an API Call with requests ==

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
# endregion

# region == Copying as cURL and Converting to Python ==
"""
1. In DevTools → Right-click any request → "Copy" → "Copy as cURL"
2. Paste it into https://curlconverter.com/ to auto-convert it to Python `requests`

This copies:
- All headers
- URL
- Cookies
- Payload (for POST/PUT)
"""
# endregion

# region == How to Extract Auth Headers or Tokens ==
"""
Sites that require login or have protected APIs often send:
- Authorization: Bearer <token>
- X-CSRF-Token
- Cookie headers with session ID

Steps:
1. Log in manually in your browser
2. Inspect an API request made after login
3. Copy the needed headers into your scraper code
"""
# endregion

# region == Advanced: Watching Live Requests While Interacting ==
"""
- Click buttons, dropdowns, or paginate through results
- Look for new API calls being triggered
- These requests often contain:
    - JSON product data
    - Dynamic filters (category, color, rating)
    - Pagination query params

Tip: Sort by "Time" or "Initiator" to locate user-triggered requests.
"""
# endregion

# region == Tools to Help With DevTools Inspection ==
"""
- JSON Viewer (browser extension): Formats ugly API output
- curlconverter.com: Converts cURL to requests/python
- DevTools → Copy → "Copy as fetch" (for Playwright/Selenium mimicry)
"""
# endregion

# region == Best Practices ==
"""
✅ Use DevTools to inspect API before writing any scraper code
✅ Scrape JSON, not HTML, whenever possible
✅ Use exact headers/cookies seen in browser
✅ Watch requests triggered by JavaScript or user interaction

⚠️ Don't assume URL is stable — inspect params for dynamic keys/tokens
⚠️ Some APIs have rate limits or require login/session to work
⚠️ Avoid headless scraping if a clean API exists
"""
# endregion

# region == Documentation ==
# MDN DevTools Network Monitor: https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor
# curlconverter.com: https://curlconverter.com/
# Scrapy XHR Tutorial: https://docs.scrapy.org/en/latest/topics/practices.html#using-browser-devtools
# endregion
