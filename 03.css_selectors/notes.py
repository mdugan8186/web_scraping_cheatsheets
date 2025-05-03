# ==== css_selectors ====

# https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors

# ==========================
# == OBJECTIVE ==
# Cheat sheet for CSS selectors used in web scraping via BeautifulSoup, Scrapy, and lxml.
# CSS selectors offer readable, concise queries and are supported across scraping libraries.
# ==========================

# region == Basic Selectors ==
"""
div           → All <div> elements
.class-name   → Class selector
#id-name      → ID selector
*             → All elements (wildcard)
"""
# endregion

# region == Combinators ==
"""
div p         → All <p> inside <div> (descendants)
div > p       → Direct children only
h2 + p        → <p> immediately after <h2>
ul ~ li       → All <li> siblings after <ul>
"""
# endregion

# region == Attribute Selectors ==
"""
a[href]                   → All <a> tags with href
img[alt='logo']           → Exact match
div[data-id^="user-"]     → Starts with "user-"
a[href$=".pdf"]           → Ends with ".pdf"
span[class*="highlight"]  → Contains "highlight"
"""
# endregion

# region == Pseudo-classes ==
"""
li:first-child
li:last-child
tr:nth-child(odd)
div:not(.hidden)
"""
# endregion

# region == Practical Examples ==
"""
.product .price         → Element with class 'price' inside 'product'
ul.items > li:nth-child(2) → Second <li> in unordered list with class 'items'
table#orders td.total   → 'total' cell inside table with id 'orders'
"""
# endregion

# region == Use in Libraries ==
"""
# BeautifulSoup
soup.select("div.product span.price")

# Scrapy
response.css("a[href^='/product']::attr(href)").getall()

# lxml
tree.cssselect("ul.list > li.active")
"""
# endregion

# region == Docs ==
# MDN: https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors
# Scrapy Selectors: https://docs.scrapy.org/en/latest/topics/selectors.html#using-css
# W3Schools: https://www.w3schools.com/cssref/css_selectors.asp
# endregion
