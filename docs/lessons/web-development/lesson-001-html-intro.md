---
title: "HTML Fundamentals: Building Web Pages"
description: "Create your first web pages using semantic HTML markup and understand document structure"
difficulty: "Beginner"
duration: "45 minutes"
tags: [html, web, markup, semantic-html, elements]
learning_objectives:
  - "Understand what HTML is and its role in web pages"
  - "Create a valid HTML document structure"
  - "Use common HTML elements correctly"
  - "Write semantic, accessible HTML"
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# HTML Fundamentals: Building Web Pages

**Difficulty**: 🟢 Beginner | **Duration**: 45 minutes

**Tags**: [`html`](../../guides/tags-reference.md#html) · [`web`](../../guides/tags-reference.md#web) · [`markup`](../../guides/tags-reference.md#markup) · [`semantic-html`](../../guides/tags-reference.md#semantic-html) · [`elements`](../../guides/tags-reference.md#elements)

---

## Learning Objectives

By the end of this lesson, you will be able to:

- Understand what HTML is and its role in web pages
- Create a valid HTML document structure
- Use common HTML elements correctly
- Write semantic, accessible HTML

## Introduction

**HTML** (HyperText Markup Language) is the foundation of every web page. It provides the structure and content that web browsers display. HTML works alongside CSS (styling) and JavaScript (interactivity) to create complete web experiences.

Think of HTML as the skeleton of a web page:

- **HTML** = Structure (bones)
- **CSS** = Styling (skin, muscles)
- **JavaScript** = Interactivity (movement)

In this lesson, we focus on HTML fundamentals.

## What Is HTML?

HTML uses **tags** to tell browsers how to display content. A tag looks like this:

```html
<tag>content</tag>
```

Tags come in pairs (opening and closing) and can have **attributes** that provide additional information:

```html
<tag attribute="value">content</tag>
```

### Common HTML Tags

Here are the most essential HTML elements:

#### Headings
```html
<h1>Main Title</h1>        <!-- Largest, most important -->
<h2>Section Title</h2>
<h3>Subsection Title</h3>
<h4>Smaller Heading</h4>
<h5>Even Smaller</h5>
<h6>Smallest Heading</h6>  <!-- Least important -->
```

#### Paragraphs and Text
```html
<p>This is a paragraph of text.</p>
<strong>Important text</strong>
<em>Emphasized text</em>
<br>  <!-- Line break (no closing tag needed) -->
```

#### Links
```html
<a href="https://example.com">Click here</a>
<a href="page.html">Go to another page</a>
```

#### Lists
```html
<!-- Unordered (bullet) list -->
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<!-- Ordered (numbered) list -->
<ol>
  <li>First step</li>
  <li>Second step</li>
</ol>
```

#### Images
```html
<img src="photo.jpg" alt="Description of image">
```

## HTML Document Structure

Every HTML page follows this structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Page Title</title>
  </head>
  <body>
    <!-- Content goes here -->
  </body>
</html>
```

**Let's break it down**:

- `<!DOCTYPE html>`: Tells the browser this is HTML5
- `<html>`: Root element containing everything
- `<head>`: Contains metadata (title, character set, links to CSS)
- `<meta charset="UTF-8">`: Specifies character encoding
- `<title>`: Page title shown in browser tab
- `<body>`: Contains visible page content

## Complete Example

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My First Web Page</title>
  </head>
  <body>
    <h1>Welcome to My Web Page</h1>
    <p>This is my first HTML page!</p>
    
    <h2>My Interests</h2>
    <ul>
      <li>Web Development</li>
      <li>Programming</li>
      <li>Design</li>
    </ul>
    
    <p>Visit <a href="https://example.com">this site</a> for more info.</p>
  </body>
</html>
```

## Semantic HTML

**Semantic HTML** means using HTML tags that describe their purpose, not just how they look.

### Good (Semantic)
```html
<nav>
  <a href="/">Home</a>
  <a href="/about">About</a>
</nav>

<article>
  <h1>Article Title</h1>
  <p>Article content...</p>
</article>

<footer>
  <p>&copy; 2026 My Company</p>
</footer>
```

### Avoid (Non-semantic)
```html
<div>
  <a href="/">Home</a>
  <a href="/about">About</a>
</div>

<div>
  <h1>Article Title</h1>
  <p>Article content...</p>
</div>

<div>
  <p>&copy; 2026 My Company</p>
</div>
```

Semantic tags make code easier to read and improve accessibility.

## Exercises

### Exercise 1: Create a Basic HTML Page

**Task**: Create an HTML page about your favorite hobby that includes:

- A title in the browser tab
- A main heading (h1)
- At least one paragraph describing the hobby
- A bulleted list of things related to the hobby

**Example Solution**:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My Hobby</title>
  </head>
  <body>
    <h1>Photography</h1>
    <p>Photography is my favorite way to capture moments and express creativity.</p>
    
    <h2>Why I Love Photography</h2>
    <ul>
      <li>It helps me see the world differently</li>
      <li>I can share memories with others</li>
      <li>It's a creative outlet</li>
    </ul>
  </body>
</html>
```

### Exercise 2: Create a Recipe Page

**Task**: Create a recipe page with:

- A recipe title (h1)
- Ingredients list (use `<ol>` for numbered list)
- Instructions (use `<ol>` for numbered steps)
- A link to a related recipe site

**Example Solution**:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Chocolate Chip Cookies</title>
  </head>
  <body>
    <h1>Chocolate Chip Cookies</h1>
    
    <h2>Ingredients</h2>
    <ul>
      <li>2 cups flour</li>
      <li>1 cup butter</li>
      <li>1 cup chocolate chips</li>
    </ul>
    
    <h2>Instructions</h2>
    <ol>
      <li>Mix dry ingredients</li>
      <li>Add butter and mix</li>
      <li>Fold in chocolate chips</li>
      <li>Bake at 375°F for 10 minutes</li>
    </ol>
    
    <p>Get more recipes at <a href="https://www.allrecipes.com">AllRecipes</a></p>
  </body>
</html>
```

## Assessment

### Self-Check Questions

1. **What does HTML stand for and what is its purpose?**
   - HTML stands for HyperText Markup Language. Its purpose is to provide the structure and content of web pages.
2. **What is the difference between an opening tag and a closing tag?**
   - An opening tag marks where an element starts (e.g., `<p>`). A closing tag marks where it ends (e.g., `</p>`).
3. **What elements should be inside the `<head>` tag?**
   - Metadata like the page title (`<title>`), character set (`<meta>`), and links to stylesheets should be in the `<head>`.
4. **What is semantic HTML and why is it important?**
   - Semantic HTML uses tags that describe their purpose (like `<nav>`, `<article>`, `<footer>`). It's important for accessibility and code readability.
5. **What's the correct order of HTML, HEAD, and BODY tags?**
   - The `<html>` tag wraps everything. Inside are `<head>` (first) and `<body>` (second).

## Summary

HTML is the foundation of web pages:

- HTML uses **tags** to structure content
- Every page needs a proper **document structure** with `<!DOCTYPE>`, `<html>`, `<head>`, and `<body>`
- Use **semantic HTML** tags to write accessible, readable code
- Learn common tags for headings, paragraphs, links, lists, and images
- Structure is just the start—CSS adds styling, and JavaScript adds interactivity

## Next Steps

- Practice writing HTML pages on different topics
- Learn CSS to style your HTML pages
- Explore forms (`<form>`, `<input>`) for user interaction
- Check out the [CSS Essentials lesson](lesson-002-css-basics.md) to add styling

---

*Great start! Next, learn to style your pages with [CSS Essentials](lesson-002-css-basics.md).*
