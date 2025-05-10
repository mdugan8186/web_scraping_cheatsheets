# ==== using_apis ====

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

# ==========================
# == OBJECTIVE ==
# Cheat sheet for extracting data from web APIs during scraping.
# Covers how to detect, inspect, mimic, and reliably interact with RESTful APIs
# using tools like `requests`, `httpx`, `curl_cffi`, and `anna`.
# ==========================

"""
When available, APIs are the most stable and efficient way to scrape data.

✅ Return structured data (JSON/XML)
✅ Avoid parsing HTML
✅ Often easier to scale and maintain
"""

# --------------------------
# What Is a Web API?
# --------------------------

"""
A web API is an interface that exposes data (often in JSON) via HTTP.

Example:
GET https://example.com/api/products?q=shoes&page=2

Response:
{
    "products": [
        {"name": "Shoe 1", "price": 29.99},
        {"name": "Shoe 2", "price": 49.99}
    ]
}
"""

# --------------------------
# Common Request Types
# --------------------------

"""
- GET     → Fetch data (e.g., search results, product listings)
- POST    → Submit data (e.g., login, filters, forms)
- PUT     → Update data (rare in scraping)
- DELETE  → Remove data (usually avoided)

APIs often require:
- Headers (e.g., User-Agent, Authorization)
- Cookies (e.g., session ID)
- Query string (for GET)
- JSON payload (for POST)
"""

# --------------------------
# Detecting APIs via DevTools
# --------------------------

"""
1. Open browser → Inspect → Network tab
2. Reload the page or interact with it
3. Filter by:
   - XHR / Fetch
   - `api`, `.json`, `search`, `products`
4. Click a request → Check:
   - URL
   - Method (GET, POST)
   - Headers
   - Query or request body
   - Preview / Response (structured JSON?)

5. Test in browser or curl:
   - Paste URL into browser → See JSON?
   - Or use curlconverter.com to test it in code
"""

# --------------------------
# Example: GET API with Query Params
# --------------------------


import time
import requests
params = {"q": "shoes", "limit": 10}
headers = {"User-Agent": "Mozilla/5.0", "Accept": "application/json"}

res = requests.get("https://example.com/api/search",
                   headers=headers, params=params)
data = res.json()
print(data["products"])

# --------------------------
# Example: POST API with JSON Payload
# --------------------------

payload = {"email": "user@example.com", "password": "mypassword"}
res = requests.post("https://example.com/api/login", json=payload)
print(res.status_code)

# --------------------------
# Handling Pagination
# --------------------------

"""
Common patterns:
- page=1,2,3
- offset=0,10,20
- cursor or next_url
"""


def paginate(base_url):
    for page in range(1, 6):
        res = requests.get(base_url, params={"page": page})
        print(res.json()["data"])


paginate("https://example.com/api/items")

# --------------------------
# Authentication (Auth Tokens & Headers)
# --------------------------

"""
Some APIs require login:
1. Submit a login POST request
2. Capture session cookies or tokens
3. Send them on future requests

Auth examples:
- Authorization: Bearer <token>
- X-CSRF-Token: <value>
- Cookie: session_id=abc123
"""

headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://example.com"
}

res = requests.get("https://example.com/api/protected", headers=headers)
print(res.status_code)

# --------------------------
# Retry and Error Handling
# --------------------------

"""
APIs often return:
- 429 Too Many Requests (rate limit)
- 401 Unauthorized (bad token)
- 403 Forbidden (IP block or bot detection)
- 500+ (server error)

Use retry logic for robustness:
"""


for i in range(3):
    try:
        res = requests.get("https://example.com/api", timeout=5)
        res.raise_for_status()
        break
    except requests.exceptions.RequestException as e:
        print("Retrying...", e)
        time.sleep(2)

# --------------------------
# API Rate Limits
# --------------------------

"""
Look for these in response headers:
- Retry-After
- X-RateLimit-Remaining
- X-RateLimit-Reset

Respect them with `time.sleep()` or backoff libraries
"""

# --------------------------
# Tools That Work Well with APIs
# --------------------------

"""
✅ requests — for most APIs
✅ httpx — async support, retry plugins
✅ curl_cffi — best for stealth APIs (TLS spoofing)
✅ anna — for async + stealth combo
✅ Postman / Hoppscotch — for debugging manually
✅ curlconverter.com — copy DevTools → Python code
"""

# --------------------------
# Best Practices
# --------------------------

"""
✅ Always check DevTools before scraping HTML — look for API first
✅ Use headers and tokens exactly as seen in DevTools
✅ Reuse cookies or sessions when logged in
✅ Watch for pagination, sorting, and filtering logic
✅ Use try/except and delay logic for error resilience

⚠️ Don’t scrape HTML if a clean API is available
⚠️ Avoid scraping APIs too quickly — triggers rate limits
⚠️ Some APIs return valid 200s but with empty payload if you're blocked
"""

# --------------------------
# Documentation
# --------------------------

"""
MDN HTTP Methods:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods

Requests Docs:
https://requests.readthedocs.io/en/latest/

HTTP Status Codes:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

curlconverter:
https://curlconverter.com/

Postman (API GUI):
https://www.postman.com/
"""
