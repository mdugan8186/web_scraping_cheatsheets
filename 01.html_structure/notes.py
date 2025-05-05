# ==== html_structure ====

# https://developer.mozilla.org/en-US/docs/Web/HTML

# ==========================
# == OBJECTIVE ==
# Cheat sheet for understanding the basic structure of HTML as used in web scraping.
# Covers tags, attributes, nesting, document flow, and scraping patterns.
# ==========================

"""
HTML (HyperText Markup Language) defines the structure and content of web pages.
Understanding how elements are arranged in the DOM (Document Object Model)
is essential for scraping with libraries like BeautifulSoup, lxml, and Scrapy.
"""

# --------------------------
# Example HTML Document
# --------------------------

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Example Page</title>
  </head>
  <body>
    <h1 class="header">Featured Products</h1>

    <div class="product" data-id="p001">
      <h2>Widget 3000</h2>
      <span class="price">$24.99</span>
      <a href="/buy/001" class="buy-link">Buy Now</a>
    </div>

    <div class="product" data-id="p002">
      <h2>Widget 4000</h2>
      <span class="price">$29.99</span>
      <a href="/buy/002" class="buy-link">Buy Now</a>
    </div>

    <ul class="features">
      <li>Durable</li>
      <li>Energy Efficient</li>
      <li>2-Year Warranty</li>
    </ul>
  </body>
</html>
"""

# --------------------------
# Common HTML Tags
# --------------------------

"""
<html>        - Root element of the page
<head>        - Metadata like <title>, <meta>, CSS/JS links
<title>       - Page title (appears in tab or browser bar)
<body>        - Main visible content container

<h1> to <h6>  - Headings (h1 = most important)
<p>           - Paragraph
<a>           - Anchor (hyperlink), uses href
<div>         - Block-level container
<span>        - Inline container
<ul>, <ol>    - Unordered/ordered lists
<li>          - List item
<img>         - Image, uses src
<table>       - Table container
<tr>, <td>    - Table row, data cell
"""

# --------------------------
# Common HTML Attributes
# --------------------------

"""
class     - Defines a CSS class, used in styling and JS (can be shared across many elements)
id        - Unique identifier for an element (should only be used once per page)
href      - URL for links (in <a> tags)
src       - Source for <img>, <script>, or <iframe>
alt       - Alternative text for images
title     - Tooltip or descriptive label
data-*    - Custom metadata (e.g., data-id="123", data-price="9.99")
name      - Form field names (for input, textarea, etc.)

⚠️ Tip: Most scraping libraries let you search by any of these attributes.
"""

# --------------------------
# Understanding Nesting
# --------------------------

"""
HTML is hierarchical. Elements can contain children:

<body>
  <div class="product">
    <h2>Widget 3000</h2>
    <span class="price">$24.99</span>
    <a href="/buy/001">Buy Now</a>
  </div>
</body>

Use nesting in your selectors:
- CSS: div.product > h2
- XPath: //div[@class='product']/h2
"""

# --------------------------
# Pattern Recognition for Scraping
# --------------------------

"""
When you see repeated elements like:

<div class="product">
  <h2>Title</h2>
  <span class="price">$19.99</span>
</div>

This is a sign that you're dealing with a list of records.
Target them using loops:
- find_all("div", class_="product")
- select("div.product")
- XPath: //div[@class="product"]
"""

# --------------------------
# Real-World Tips
# --------------------------

"""
✅ Use browser DevTools (right-click > Inspect) to find:
   - The structure of the element
   - Unique classes or IDs
   - Parent-child relationships
   - Headers, footers, ads to ignore

✅ Use the "Copy selector" or "Copy XPath" feature in DevTools for a starting point.

✅ Prefer classes for repeatable patterns, IDs for single-use elements.

✅ Consider custom attributes like data-* (e.g., data-id="123") — these often contain structured data!

⚠️ Avoid absolute paths like html > body > div > div > span
⚠️ Don't rely on tag positions unless necessary (like div[3])
⚠️ If the content is missing in the HTML, it's probably rendered by JavaScript
"""

# --------------------------
# JavaScript-Generated Content
# --------------------------

"""
If you don't see the content in the page source or initial response,
but you DO see it in the browser, the site is likely using JavaScript to load it.

You can:
- Use the Network tab to find the actual API calls (often returning JSON)
- Switch to Selenium/Playwright if you must scrape rendered content
- Use Scrapy + Splash or curl_cffi/anna with DevTools info
"""

# --------------------------
# HTML Debugging Resources
# --------------------------

"""
- View Page Source: Shows raw HTML served to browser (right-click > View Page Source)
- Inspect Element: Shows live DOM, including JavaScript changes
- Network > XHR: Shows backend API requests
- Accessibility > ARIA: Good for semantic tags (like roles)

Tools like https://httpbin.org/html or https://books.toscrape.com are great practice sites.
"""

# --------------------------
# Documentation
# --------------------------

"""
MDN HTML Reference:
https://developer.mozilla.org/en-US/docs/Web/HTML

W3C HTML Specification:
https://html.spec.whatwg.org/
"""
