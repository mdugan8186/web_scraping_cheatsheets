# ==== requests ====

# https://docs.python-requests.org/en/latest/

# ==========================
# == OBJECTIVE ==
# Full cheat sheet for Python's `requests` library.
# Covers GET, POST, headers, sessions, cookies, file downloads, timeouts, redirects,
# error handling, and documentation links.
# ==========================

from requests.auth import HTTPBasicAuth
import requests

# --------------------------
# Basic GET Request
# --------------------------

response = requests.get("https://example.com")
print(response.status_code)
print(response.text)

# --------------------------
# GET with Query Parameters
# --------------------------

params = {"q": "web scraping", "page": 2}
response = requests.get("https://example.com/search", params=params)
print(response.url)  # → https://example.com/search?q=web+scraping&page=2

# --------------------------
# Setting Headers
# --------------------------

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://google.com"
}
response = requests.get("https://example.com", headers=headers)

# --------------------------
# Sending Cookies
# --------------------------

cookies = {"session_id": "abc123"}
response = requests.get("https://example.com", cookies=cookies)

# --------------------------
# Handling Timeouts
# --------------------------

try:
    response = requests.get("https://example.com", timeout=5)
except requests.Timeout:
    print("Request timed out")

# --------------------------
# Handling Redirects
# --------------------------

response = requests.get("https://httpbin.org/redirect/3", allow_redirects=True)
print(response.history)  # List of intermediate redirect responses

# --------------------------
# Handling Errors (Status Codes)
# --------------------------

try:
    response = requests.get("https://example.com/not-found")
    response.raise_for_status()
except requests.HTTPError as e:
    print(f"HTTP error: {e}")
except requests.RequestException as e:
    print(f"Request failed: {e}")

# --------------------------
# POST Request with Form Data
# --------------------------

form_data = {"username": "myuser", "password": "mypassword"}
response = requests.post("https://example.com/login", data=form_data)

# --------------------------
# POST Request with JSON
# --------------------------

json_data = {"title": "Hello", "body": "World"}
response = requests.post("https://example.com/api", json=json_data)

# --------------------------
# Custom HTTP Methods (PUT, DELETE, etc.)
# --------------------------

response = requests.put(
    "https://example.com/resource/123", json={"status": "active"})
response = requests.delete("https://example.com/resource/123")

# --------------------------
# File Upload
# --------------------------

files = {"file": open("example.txt", "rb")}
response = requests.post("https://example.com/upload", files=files)

# --------------------------
# File Download
# --------------------------

response = requests.get("https://example.com/image.png")
with open("image.png", "wb") as f:
    f.write(response.content)

# --------------------------
# Session Object (Persistent Headers/Cookies)
# --------------------------

session = requests.Session()
session.headers.update({"User-Agent": "Mozilla/5.0"})
session.get("https://example.com/page1")
session.get("https://example.com/page2")  # Same headers & cookies reused

# --------------------------
# Inspecting Response
# --------------------------

response = requests.get("https://example.com")
print(response.status_code)             # 200, 404, etc.
print(response.headers["Content-Type"])  # text/html, application/json
print(response.encoding)                # e.g., 'utf-8'
print(response.cookies)                 # <RequestsCookieJar>
print(response.url)                     # Final URL after redirects

# --------------------------
# JSON Response Parsing
# --------------------------

response = requests.get("https://api.example.com/data")
data = response.json()
print(data)

# --------------------------
# Streaming Responses (for large files)
# --------------------------

response = requests.get("https://example.com/large.zip", stream=True)
with open("large.zip", "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

# --------------------------
# Disable SSL Verification (Not Recommended for Production)
# --------------------------

response = requests.get("https://self-signed.badssl.com/", verify=False)

# --------------------------
# Authentication
# --------------------------

response = requests.get("https://example.com/protected",
                        auth=HTTPBasicAuth("user", "pass"))

# --------------------------
# Best Practices
# --------------------------

"""
✅ Always use a User-Agent header to avoid 403 errors  
✅ Use sessions to persist headers and cookies across requests  
✅ Handle timeouts and connection errors with try/except  
✅ Use params for pagination instead of hardcoding URLs  
✅ For large downloads, stream the response  

⚠️ Don’t scrape too quickly — use delays between requests  
⚠️ Don’t disable SSL verification unless absolutely necessary  
"""

# --------------------------
# Documentation
# --------------------------

"""
Official Docs: https://docs.python-requests.org/en/latest/  
GitHub Repo: https://github.com/psf/requests  
Cheat Sheet: https://realpython.com/python-requests/  
HTTPBin (for testing): https://httpbin.org/  
"""
