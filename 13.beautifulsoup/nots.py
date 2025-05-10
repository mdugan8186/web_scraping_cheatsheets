# ==== beautifulsoup ====

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# ==========================
# == OBJECTIVE ==
# Cheat sheet for using BeautifulSoup (bs4) for parsing and extracting data from HTML/XML.
# Covers searching by tag, class, ID, text, attributes, CSS selectors, and DOM navigation.
# ==========================

# --------------------------
# Installation
# --------------------------

"""
pip install beautifulsoup4
"""

# --------------------------
# Basic Usage
# --------------------------

import requests
from bs4 import BeautifulSoup, NavigableString

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

# --------------------------
# Finding Elements
# --------------------------

# Single element
title = soup.find("title")
h1 = soup.find("h1")
p_by_id = soup.find(id="first")

# Multiple elements
all_paragraphs = soup.find_all("p")
desc_paragraph = soup.find("p", class_="description")

# CSS Selectors
soup.select("p")                 # All <p> tags
soup.select("p.description")     # Class selector
soup.select("#first")            # ID selector
soup.select("h1.title")          # Tag + class

# --------------------------
# Getting Text and Attributes
# --------------------------

text = h1.get_text()                  # 'Hello World'
link = soup.find("a")
link_text = link.text                 # 'link'
link_url = link["href"]              # 'https://example.com'
link_url_safe = link.get("href", "N/A")

# --------------------------
# Navigating the DOM
# --------------------------

parent = h1.parent
next_element = h1.find_next()
previous_element = h1.find_previous()
next_sibling = h1.find_next_sibling()
previous_sibling = h1.find_previous_sibling()

# Direct nested access
link = soup.body.p.a

# --------------------------
# Searching by Text
# --------------------------

soup.find_all(string="Hello World")  # Exact match
soup.find_all(string=lambda t: "Hello" in t)  # Substring match

# --------------------------
# Working with Attributes
# --------------------------

soup.find("a", href="https://example.com")
soup.find_all("p", attrs={"class": "description"})

# --------------------------
# Cleaning or Stripping Tags
# --------------------------

# Extract raw text
clean_text = soup.get_text(separator=" ", strip=True)

# Remove <script> and <style> tags
for tag in soup(["script", "style"]):
    tag.decompose()

# --------------------------
# Parsing External HTML Pages
# --------------------------

res = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(res.text, "html.parser")

titles = [h3.a["title"] for h3 in soup.select("h3")]
prices = [p.text for p in soup.select(".price_color")]

# --------------------------
# Tips and Best Practices
# --------------------------

"""
✅ Use .select() when CSS selectors are easier to express
✅ Use .find_all() for structured iteration
✅ Use .get_text(strip=True) to extract clean text
✅ Use .get() for safe attribute access
✅ Inspect elements with browser DevTools to locate tag/class/ID

⚠️ Avoid .contents or .children unless necessary
⚠️ BeautifulSoup does not run JavaScript — use Selenium or DevTools inspection for dynamic sites
"""

# --------------------------
# Limitations
# --------------------------

"""
- Does not render or execute JavaScript
- Cannot evaluate XPath (use lxml or Scrapy for that)
- Parsing malformed HTML is possible but sometimes brittle
- For performance, use selectolax (faster C-based parser)
"""

# --------------------------
# Documentation
# --------------------------

"""
BeautifulSoup Docs:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/

Real Python Tutorial:
https://realpython.com/beautiful-soup-web-scraper-python/

CSS Selector Reference (MDN):
https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors
"""
