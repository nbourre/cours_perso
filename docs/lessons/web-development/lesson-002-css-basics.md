---
title: "CSS Essentials: Styling Your Web Pages"
description: "Master CSS to make your web pages beautiful with colors, layouts, and responsive design"
difficulty: "Beginner"
duration: "1 hour"
tags: [css, styling, web, selectors, layout, responsive]
learning_objectives:
  - "Understand CSS syntax and how to apply styles"
  - "Use CSS selectors to target HTML elements"
  - "Apply colors, fonts, and spacing effectively"
  - "Create responsive layouts for different screen sizes"
prerequisites: [lesson-001-html-intro]
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# CSS Essentials: Styling Your Web Pages

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand CSS syntax and how to apply styles
- Use CSS selectors to target HTML elements
- Apply colors, fonts, and spacing effectively
- Create responsive layouts for different screen sizes

## Introduction

**CSS** (Cascading Style Sheets) is the language of web design. While HTML provides structure, CSS makes web pages beautiful by controlling colors, fonts, layouts, and spacing.

CSS lets you:
- **Style text**: Colors, fonts, sizes
- **Control layout**: Positioning, grids, flexbox
- **Add visual effects**: Shadows, borders, animations
- **Make pages responsive**: Adapt to different screen sizes
- **Separate content from design**: Keep HTML clean

## CSS Basics

### CSS Syntax

A CSS rule has two parts:

```css
selector {
  property: value;
}
```

**Example**:
```css
p {
  color: blue;
  font-size: 16px;
}
```

This says: "Make all paragraphs blue and 16 pixels large."

### Three Ways to Add CSS

#### 1. Inline CSS
```html
<p style="color: red;">This is red text</p>
```

#### 2. Internal CSS (in `<head>`)
```html
<head>
  <style>
    p {
      color: red;
    }
  </style>
</head>
```

#### 3. External CSS (recommended)
```html
<head>
  <link rel="stylesheet" href="styles.css">
</head>
```

In `styles.css`:
```css
p {
  color: red;
}
```

## CSS Selectors

Selectors determine which HTML elements get styled.

### Element Selector
```css
p {
  color: blue;
}
```
Styles ALL `<p>` elements.

### Class Selector
```css
.highlight {
  background-color: yellow;
}
```

```html
<p class="highlight">This is highlighted</p>
```

### ID Selector
```css
#header {
  background-color: navy;
  color: white;
}
```

```html
<div id="header">Welcome</div>
```

### Multiple Selectors
```css
h1, h2, h3 {
  color: darkgreen;
}
```
Styles all h1, h2, and h3 elements the same way.

## Common CSS Properties

### Colors
```css
p {
  color: blue;                    /* Text color */
  background-color: lightblue;    /* Background color */
  border: 2px solid black;        /* Border */
}
```

Colors can be: named (`red`), hex (`#FF0000`), or RGB (`rgb(255, 0, 0)`)

### Fonts
```css
body {
  font-family: Arial, sans-serif;    /* Font type */
  font-size: 14px;                   /* Text size */
  font-weight: bold;                 /* Bold, normal */
  line-height: 1.5;                  /* Space between lines */
}
```

### Spacing
```css
p {
  margin: 10px;         /* Space outside element */
  padding: 10px;        /* Space inside element */
}
```

### Box Model
```css
div {
  width: 300px;         /* Element width */
  height: 200px;        /* Element height */
  margin: 20px;         /* Outside spacing */
  padding: 15px;        /* Inside spacing */
  border: 1px solid;    /* Border */
}
```

## Complete Example

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>Styled Page</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f5f5f5;
        margin: 0;
        padding: 20px;
      }
      
      h1 {
        color: darkblue;
        border-bottom: 3px solid darkblue;
        padding-bottom: 10px;
      }
      
      .intro {
        background-color: lightblue;
        padding: 15px;
        border-radius: 5px;
      }
      
      p {
        line-height: 1.6;
        color: #333;
      }
    </style>
  </head>
  <body>
    <h1>Welcome to My Site</h1>
    <p class="intro">This is a styled introduction paragraph.</p>
    <p>This paragraph has regular styling.</p>
  </body>
</html>
```

## Responsive Design Basics

Responsive design makes pages look good on phones, tablets, and computers.

### The Viewport Meta Tag
Always include this in your `<head>`:
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Media Queries
Adjust styles based on screen size:

```css
/* Desktop styles */
.container {
  width: 1000px;
}

/* Tablet styles */
@media (max-width: 768px) {
  .container {
    width: 100%;
  }
}

/* Mobile styles */
@media (max-width: 480px) {
  .container {
    width: 100%;
    padding: 10px;
  }
}
```

## Exercises

### Exercise 1: Style a Simple Page

**Task**: Create an HTML page with CSS that styles:
- A heading with a background color and text color
- Paragraphs with specific font and spacing
- At least one element with a class selector

**Example Solution**:
```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
    <title>My Styled Page</title>
    <style>
      h1 {
        color: white;
        background-color: navy;
        padding: 20px;
        text-align: center;
      }
      
      p {
        font-size: 16px;
        line-height: 1.6;
        color: #333;
      }
      
      .special {
        color: red;
        font-weight: bold;
      }
    </style>
  </head>
  <body>
    <h1>My Site</h1>
    <p>Welcome to my page.</p>
    <p class="special">This paragraph is special!</p>
  </body>
</html>
```

### Exercise 2: Create a Card Layout

**Task**: Create a "card" with CSS that has:
- A border
- Padding inside
- A shadow effect
- A background color different from the page

**Example Solution**:
```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        background-color: #f0f0f0;
        padding: 20px;
      }
      
      .card {
        background-color: white;
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        max-width: 400px;
      }
      
      .card h2 {
        margin-top: 0;
        color: darkblue;
      }
    </style>
  </head>
  <body>
    <div class="card">
      <h2>Product Card</h2>
      <p>This is a styled card component.</p>
    </div>
  </body>
</html>
```

## Assessment

### Self-Check Questions

1. **What does CSS stand for and what is its purpose?**
   - CSS stands for Cascading Style Sheets. Its purpose is to style HTML elements with colors, fonts, layouts, and spacing.

2. **What are the three ways to add CSS to an HTML page?**
   - Inline CSS (in the HTML tag), Internal CSS (in `<style>` tag), External CSS (in separate .css file).

3. **What's the difference between a class selector and an ID selector?**
   - Class selectors (`.classname`) can be used on multiple elements. ID selectors (`#idname`) are unique to one element.

4. **What does the CSS box model include?**
   - The box model includes margin (outside space), border, padding (inside space), and the content.

5. **How do you make a page responsive to different screen sizes?**
   - Use the viewport meta tag and media queries to adjust styles based on screen width.

## Summary

CSS transforms plain HTML into beautiful web pages:

- **CSS syntax**: `selector { property: value; }`
- **Three placement options**: Inline, internal, external (external recommended)
- **Selectors**: Element, class, ID to target elements
- **Key properties**: Color, font, spacing, borders, dimensions
- **Responsive design**: Use media queries for different screen sizes

CSS is the bridge between content and design!

## Next Steps

- Practice styling various HTML elements
- Learn flexbox and CSS Grid for advanced layouts
- Explore CSS animations and transitions
- Dive into JavaScript to add interactivity to your styles

---

*You're now ready to create beautiful web pages! Explore more lessons in the [Web Development](index.md) section.*
