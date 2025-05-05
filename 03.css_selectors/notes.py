# ==== css_selectors ====

# https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors

# ==========================
# == OBJECTIVE ==
# Cheat sheet for using CSS selectors to extract elements in HTML documents.
# Focuses on syntax, real-world scraping examples, and equivalents to XPath.
# Used in BeautifulSoup, parsel, Scrapy, and browser DevTools.
# ==========================

"""
CSS selectors let you query HTML elements using patterns similar to those in CSS stylesheets.

They're supported in:
- BeautifulSoup (.select(), .select_one())
- Scrapy (via parsel.Selector.css)
- Browser DevTools (Inspect → Copy selector)
- Playwright & Puppeteer

Selectors are easier to read than XPath and preferred when exact structure isn't needed.
"""

# --------------------------
# Basic Selectors
# --------------------------

"""
tag              → matches element by tag (e.g., div, p, h1)
.class           → matches element with class
#id              → matches element with id
*                → wildcard (matches all tags)
[attr]           → element with an attribute
[attr="value"]   → attribute equals value

Examples:
- div             → all <div> elements
- .product        → elements with class="product"
- #main-header    → element with id="main-header"
- a[href]         → <a> tags with an href
- input[type="text"] → <input type="text">
"""

# --------------------------
# Combinators and Nesting
# --------------------------

"""
descendant        → div span       → span inside any div
child             → div > span     → span directly inside div
adjacent sibling  → h2 + p         → <p> immediately after <h2>
general sibling   → h2 ~ p         → all <p> after <h2> siblings

Examples:
- ul li           → all <li> inside <ul>
- div > a         → <a> tags that are direct children of div
- h1 + p          → paragraph that immediately follows an h1
"""

# --------------------------
# Attribute Selectors
# --------------------------

"""
[attr]                → matches elements that have the attribute
[attr="value"]        → exact match
[attr~="value"]       → space-separated value contains word
[attr^="prefix"]      → starts with
[attr$="suffix"]      → ends with
[attr*="substring"]   → contains substring

Examples:
- a[href^="/product"]    → links that start with "/product"
- img[src$=".jpg"]       → images ending in ".jpg"
- div[class*="featured"] → divs where class includes "featured"
"""

# --------------------------
# Pseudo-Classes
# --------------------------

"""
:first-child        → first element among siblings
:last-child         → last element among siblings
:nth-child(n)       → nth child (1-based)
:nth-of-type(n)     → nth tag of that type among siblings
:not(selector)      → negate match

Examples:
- li:first-child          → first <li> in a list
- li:nth-child(2)         → second <li>
- p:not(.description)     → all <p> tags that don’t have class="description"
"""

# --------------------------
# Chaining and Combining Selectors
# --------------------------

"""
p.description                   → <p class="description">
div.product > h2                → <h2> inside <div class="product">
ul.features > li:nth-child(2)   → second list item
"""

# --------------------------
# Real-World Scraping Examples
# --------------------------


from bs4 import BeautifulSoup
html = """
<div class="product">
  <h2>Widget 3000</h2>
  <span class="price">$24.99</span>
  <a href="/buy/123" class="buy-link">Buy Now</a>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

title = soup.select_one("div.product h2").text
price = soup.select_one("div.product .price").text
link = soup.select_one("div.product a.buy-link")["href"]

print(title)  # Widget 3000
print(price)  # $24.99
print(link)   # /buy/123

# --------------------------
# Best Practices
# --------------------------

"""
✅ Use DevTools to inspect and right-click → Copy selector
✅ Use class or id selectors over positional ones when possible
✅ Use attribute selectors when data-* values hold useful info
✅ Use chaining like div.product h2 to match nested structure

⚠️ Avoid over-relying on nth-child() — page layout changes can break it
⚠️ Don't use overly long selectors unless needed (e.g., html > body > div > div)
"""

# --------------------------
# Documentation
# --------------------------

"""
MDN CSS Selector Reference:
https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors

CSS Selectors Cheat Sheet:
https://www.freecodecamp.org/news/css-selectors-cheat-sheet/

Playground (test CSS selectors online):
https://css-tricks.com/examples/nth-child-tester/

Scrapy Selector Reference:
https://docs.scrapy.org/en/latest/topics/selectors.html

BeautifulSoup .select() Docs:
https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors

Practice Pages:
- https://books.toscrape.com/
- https://quotes.toscrape.com/
"""
