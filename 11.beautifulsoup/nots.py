# ==== beautifulsoup ====

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# ==========================
# == OBJECTIVE ==
# Cheat sheet for using BeautifulSoup (bs4) for parsing and extracting data from HTML/XML.
# Covers searching by tag, class, ID, text, attributes, CSS selectors, and DOM navigation.
# ==========================

# region == Installation ==
"""
pip install beautifulsoup4
"""
# endregion

# region == Basic Usage ==
import requests
from bs4 import NavigableString
from bs4 import BeautifulSoup

html = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <h1 class="title">Hello World</h1>
    <p id="first">This is a <a href="https://example.com">link</a>.</p>
    <p class="description">Another paragraph</p>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# endregion

# region == Finding Elements ==
# Single element
title = soup.find("title")                 # <title>Test Page</title>
h1 = soup.find("h1")                       # <h1 class="title">Hello World</h1>
p_by_id = soup.find(id="first")           # <p id="first">...</p>

# Multiple elements
all_paragraphs = soup.find_all("p")       # list of <p> tags
desc_paragraph = soup.find("p", class_="description")

# CSS Selectors
soup.select("p")                          # all <p> tags
soup.select("p.description")              # <p class="description">
soup.select("#first")                     # element with id="first"
soup.select("h1.title")                   # <h1 class="title">
# endregion

# region == Getting Text and Attributes ==
text = h1.get_text()                      # 'Hello World'
link = soup.find("a")
link_text = link.text                     # 'link'
link_url = link["href"]                   # 'https://example.com'

# Safe attribute access
link_url_safe = link.get("href", "N/A")   # fallback if missing
# endregion

# region == Navigating the DOM ==
h1 = soup.find("h1")
parent = h1.parent                        # <body>...
next_element = h1.find_next()             # <p>...
previous_element = h1.find_previous()     # <head>...
next_sibling = h1.find_next_sibling()     # <p>...
previous_sibling = h1.find_previous_sibling()  # None in this case

# Nested tag chaining
link = soup.body.p.a                      # direct access to <a> inside <p>
# endregion

# region == Searching by Text ==
soup.find_all(string="Hello World")       # exact match
soup.find_all(string=lambda t: "Hello" in t)  # substring match
# endregion

# region == Working with Attributes ==
# Find tag with specific attribute
soup.find("a", href="https://example.com")

# Find tags with any attribute key-value match
soup.find_all("p", attrs={"class": "description"})
# endregion

# region == Cleaning or Stripping Tags ==

# Extract raw text only
clean_text = soup.get_text(separator=" ", strip=True)

# Remove all <script> and <style> tags
for tag in soup(["script", "style"]):
    tag.decompose()
# endregion

# region == Parsing External HTML Pages ==

res = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")

titles = [h3.a["title"] for h3 in soup.select("h3")]
prices = [p.text for p in soup.select(".price_color")]
# endregion

# region == Tips and Best Practices ==
"""
✅ Use `.select()` when CSS selectors are more readable
✅ Use `.find_all()` for structured iteration
✅ Use `.get_text(strip=True)` to extract clean text
✅ Combine with DevTools for tag/class inspection
✅ Use `.get()` for safe attribute access (avoids KeyError)

⚠️ Avoid `.contents` or raw `.children` unless you're deeply navigating the DOM
⚠️ Don't parse JavaScript-generated content with bs4 — use Selenium or API calls
"""
# endregion

# region == Limitations ==
"""
- BeautifulSoup does not execute JavaScript
- It parses HTML as-is — you need to inspect and handle malformed or complex structures
- For performance or large-scale scraping, use `lxml` or `selectolax`
"""
# endregion

# region == Documentation ==
# BeautifulSoup 4 Docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# Tutorial (Real Python): https://realpython.com/beautiful-soup-web-scraper-python/
# CSS Selectors Reference: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors
# endregion
