# ==== html_structure ====

# https://developer.mozilla.org/en-US/docs/Web/HTML/Element

# ==========================
# == OBJECTIVE ==
# Cheat sheet for understanding HTML document structure and common tag usage for web scraping.
# This includes semantic layout, common element patterns, and scraper-relevant attributes.
# ==========================

# region == Basic HTML Document Structure ==
"""
An HTML page is structured like this:

<!DOCTYPE html>
<html>
  <head>
    <title>Page Title</title>
  </head>
  <body>
    <!-- Main content -->
  </body>
</html>
"""
# endregion

# region == Common Tag Types and Usage ==
"""
Block elements:
- <div>: Generic block-level container (used for grouping)
- <section>: Thematic grouping of content
- <article>: Standalone content unit (e.g., blog post)
- <header>, <footer>, <nav>: Semantic layout elements

Inline elements:
- <span>: Generic inline container
- <a>: Hyperlink anchor
- <strong>, <em>: Inline emphasis (bold, italic)
- <img>: Image

Data structures:
- <ul>, <ol>, <li>: Lists
- <table>, <thead>, <tbody>, <tr>, <td>, <th>: Tables
- <form>, <input>, <button>, <label>, <select>, <option>: Forms and input
"""
# endregion

# region == Common HTML Attributes to Target in Scrapers ==
"""
id          → Unique element identifier
class       → Often used for styling, also useful for pattern matching
href        → Used in <a> tags for links
src         → Source URL for <img>, <video>, <script>
alt         → Alternative text for images
title       → Tooltip or supplementary text
data-*      → Custom attributes often used by JavaScript (very useful for scraping)

Example:
  <div class="product" id="item-123" data-stock="in">...</div>
"""
# endregion

# region == Repeated Patterns in Lists and Tables ==
"""
<ul>
  <li class="item">Item 1</li>
  <li class="item">Item 2</li>
</ul>

<table>
  <thead><tr><th>Name</th><th>Price</th></tr></thead>
  <tbody>
    <tr><td>Shirt</td><td>$20</td></tr>
    <tr><td>Hat</td><td>$10</td></tr>
  </tbody>
</table>
"""
# endregion

# region == Example Snippet (Annotated) ==
example_html = """
<div class="product" id="prod-001">
  <h2 class="name">Cool Hat</h2>
  <span class="price">$9.99</span>
  <a href="/buy/001">Buy Now</a>
</div>
"""
"""
- class="product" groups the item's block
- <h2> and <span> are where the actual data lives
- The <a> tag contains the purchase link in its href attribute
"""
# endregion

# region == Scraper Tips ==
"""
- Use DevTools (right-click → Inspect) to explore the structure
- Identify repeated structures for iterating
- Use unique or semi-unique classes/ids when selecting elements
- If there's a <script type="application/json"> block — it's gold. Try parsing it directly.
"""
# endregion

# region == Documentation ==
# MDN Element Reference: https://developer.mozilla.org/en-US/docs/Web/HTML/Element
# HTML Validator: https://validator.w3.org/
# endregion
