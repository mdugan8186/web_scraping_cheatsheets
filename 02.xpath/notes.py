# ==== xpath ====

# https://developer.mozilla.org/en-US/docs/Web/XPath

# ==========================
# == OBJECTIVE ==
# Cheat sheet for XPath: querying HTML/XML documents using node paths.
# Used in lxml, Scrapy, and Selenium. Crucial for precise web scraping.
# ==========================

# region == XPath Syntax Basics ==
"""
//tag              → All <tag> elements
//div[@class='x']  → <div> with exact class match
//a/@href          → Extract href values from all <a> tags
//*[@id='main']   → Any tag with id='main'
/html/body/div    → Absolute path (not recommended for scraping)

//*                → Wildcard (any element)
"""
# endregion

# region == Attribute and Text Selectors ==
"""
//div[@data-id]                  → Has 'data-id' attribute
//span[text()='Buy Now']        → Exact text match
//div[contains(text(), 'Price')]→ Partial text match
//a[starts-with(@href, '/prod')]→ Href starts with /prod
"""
# endregion

# region == Position and Indexing ==
"""
(//li)[1]             → First <li> in entire document
(//div[@class='x'])[3]→ Third <div> with class="x"
(//tr)[last()]        → Last table row
//ul/li[position()=2] → Second list item
"""
# endregion

# region == Logical Conditions ==
"""
//div[@id='a' or @class='b']
//*[contains(@class, 'card') and contains(@data-type, 'active')]
"""
# endregion

# region == Axis Navigation ==
"""
//li/parent::ul               → Get <ul> containing <li>
.//img/ancestor::div         → Closest ancestor <div> of an <img>
.//a/following-sibling::span → <span> that follows an <a>
"""
# endregion

# region == Use in Libraries ==
"""
# lxml
from lxml import html
tree = html.fromstring(response.content)
title = tree.xpath("//h1/text()")

# Scrapy
response.xpath("//div[@class='item']/h2/text()").get()

# Selenium
element = driver.find_element(By.XPATH, "//button[@id='submit']")
"""
# endregion

# region == Documentation ==
# MDN: https://developer.mozilla.org/en-US/docs/Web/XPath
# W3Schools XPath: https://www.w3schools.com/xml/xpath_intro.asp
# Devhints: https://devhints.io/xpath
# endregion
