# Playwright Python Locators - AI Decision & Reference Guide

This document serves as a lightweight reference guide for selecting and constructing optimal Playwright Python locators based on official best practices.

---

## 1. Locator Selection Priority Hierarchy

When choosing a locator, always follow this priority order to ensure tests/automation are resilient, maintainable, and reflect user perception:

| Priority | Locator Method | Best Suited For | Key Advantages |
| :--- | :--- | :--- | :--- |
| **1 (Highest)** | `page.get_by_role()` | Interactive elements (buttons, links, checkboxes, headings, textboxes) | Reflects accessibility & user experience; resilient to DOM structure changes |
| **2** | `page.get_by_label()` | Form controls with `<label>` tags | Natural form interaction |
| **3** | `page.get_by_placeholder()` | Input elements with `placeholder` attributes (lacking clear labels) | Clear user-visible cue |
| **4** | `page.get_by_text()` | Non-interactive text containers (`<div>`, `<span>`, `<p>`) | User-visible content matching |
| **5** | `page.get_by_alt_text()` | Images (`<img>`), SVGs, map areas with `alt` attributes | Accessible visual element selection |
| **6** | `page.get_by_title()` | Elements with `title` tooltip attributes | Tooltip/attribute fallback |
| **7** | `page.get_by_test_id()` | Dynamic / complex UI lacking ARIA roles or distinct text | Highly resilient, explicit testing contract (`data-testid`) |
| **8 (Lowest)** | `page.locator()` (CSS / XPath) | Legacy DOM structures or fallback when no standard locator works | Brittle; prone to breaking on layout changes |

---

## 2. Standard Locator API Reference

### 1. `get_by_role(role, name=..., exact=..., include_hidden=...)`
- **Roles:** `"button"`, `"checkbox"`, `"heading"`, `"link"`, `"textbox"`, `"combobox"`, `"list"`, `"listitem"`, `"table"`, `"row"`, etc.
- **Examples:**
  ```python
  page.get_by_role("button", name="Sign in")
  page.get_by_role("heading", name="Dashboard", level=1)
  page.get_by_role("checkbox", name="Subscribe")
  page.get_by_role("button", name=re.compile(r"submit", re.IGNORECASE))
  ```

### 2. `get_by_label(text, exact=False)`
- **Examples:**
  ```python
  page.get_by_label("Username")
  page.get_by_label("Password").fill("secret")
  ```

### 3. `get_by_placeholder(text, exact=False)`
- **Examples:**
  ```python
  page.get_by_placeholder("name@example.com")
  ```

### 4. `get_by_text(text, exact=False)`
- **Behavior:** Automatically normalizes whitespace.
- **Examples:**
  ```python
  page.get_by_text("Welcome back")
  page.get_by_text("Submit", exact=True)
  page.get_by_text(re.compile(r"welcome", re.IGNORECASE))
  ```

### 5. `get_by_alt_text(text, exact=False)`
- **Examples:**
  ```python
  page.get_by_alt_text("Company Logo")
  ```

### 6. `get_by_title(text, exact=False)`
- **Examples:**
  ```python
  page.get_by_title("Close window")
  ```

### 7. `get_by_test_id(test_id)`
- Defaults to matching `data-testid`.
- Custom test-id attribute configuration:
  ```python
  playwright.selectors.set_test_id_attribute("data-pw")
  page.get_by_test_id("submit-button")
  ```

### 8. `locator(selector, has_text=..., has=...)` (CSS / XPath Fallback)
- **Examples:**
  ```python
  page.locator("button.submit-btn")
  page.locator("xpath=//button[@type='submit']")
  ```

---

## 3. Chaining & Filtering Locators

Narrow down scope by combining locators or applying filters.

### Filtering (`locator.filter()`)
- **By Text:**
  ```python
  page.get_by_role("listitem").filter(has_text="Product 2")
  page.get_by_role("listitem").filter(has_not_text="Out of Stock")
  ```
- **By Child Element (`has` / `has_not`):**
  ```python
  page.get_by_role("listitem").filter(
      has=page.get_by_role("button", name="Delete")
  )
  ```

### Chaining
- **Parent to Child:**
  ```python
  product_card = page.get_by_role("listitem", name="Product 1")
  product_card.get_by_role("button", name="Add to cart").click()
  ```

---

## 4. Working with Multiple Elements

When a locator matches multiple elements:

- **Specific Index:**
  ```python
  page.get_by_role("button").nth(0)  # First item
  page.get_by_role("button").first
  page.get_by_role("button").last
  ```
- **Iterating / Counting:**
  ```python
  items = page.get_by_role("listitem").all()
  for item in items:
      print(item.text_content())
  ```

---

## 5. Frames & Shadow DOM

- **Shadow DOM:** Playwright automatically pierces open Shadow DOM roots for all locators (except XPath).
  ```python
  page.get_by_text("Inside Shadow Root").click()
  ```
- **Iframes:** Use `frame_locator()` before calling standard locators:
  ```python
  frame = page.frame_locator("#my-iframe")
  frame.get_by_role("button", name="Submit").click()
  ```

---

## 6. Anti-Patterns to Avoid

1. ❌ **Avoid Long CSS/XPath Chains:**
   `page.locator("#main > div:nth-child(2) > div.card > button")`
   *Why:* Prone to breaking with layout or styling updates.

2. ❌ **Avoid Using Text Locators for Buttons/Inputs:**
   `page.get_by_text("Submit")` on a `<button>`
   *Why:* Prefer `page.get_by_role("button", name="Submit")` to match user accessibility tree semantics.

3. ❌ **Avoid Manual Sleep/Delay:**
   Playwright locators auto-wait for actionability before clicking or filling.