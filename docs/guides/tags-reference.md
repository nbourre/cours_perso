# Tags Reference

Welcome to the tags reference guide! This page lists all available tags used across the lesson system and shows which lessons are tagged with each one.

**Tags enable cross-subject discovery**. Instead of browsing by subject, you can search by topic or concept to find related lessons across all subjects.

---

## How Tags Work

Each lesson is tagged with 1-5 keywords that describe its content. Tags help you:

- **Discover related lessons** across different subjects
- **Find lessons by technology** (e.g., "python", "javascript", "css")
- **Find lessons by concept** (e.g., "functions", "data-types", "async")
- **Find lessons by domain** (e.g., "web", "backend", "data-analysis")

### Example: Finding Async Programming

If you search for the tag **"async"**, you'll find lessons about asynchronous programming regardless of which subject they're in. Currently we have lessons tagged with individual concepts, but this helps when we have lessons from multiple subjects covering the same topic.

---

## All Available Tags

### Technology Tags
Tags for specific programming languages, frameworks, and libraries:

- **`python`** (3 lessons)
  - Lesson: Introduction to Variables
  - Lesson: Functions: Code Reuse and Organization
  - Lesson: Pandas for Data Analysis

- **`javascript`** (0 lessons)
  - *Coming soon*

- **`html`** (1 lesson)
  - Lesson: HTML Fundamentals: Building Web Pages

- **`css`** (1 lesson)
  - Lesson: CSS Essentials: Styling Your Web Pages

- **`pandas`** (1 lesson)
  - Lesson: Pandas for Data Analysis

### Concept Tags
Tags for abstract ideas, patterns, and programming concepts:

- **`variables`** (1 lesson)
  - Lesson: Introduction to Variables

- **`data-types`** (1 lesson)
  - Lesson: Introduction to Variables

- **`functions`** (1 lesson)
  - Lesson: Functions: Code Reuse and Organization

- **`code-organization`** (1 lesson)
  - Lesson: Functions: Code Reuse and Organization

- **`parameters`** (1 lesson)
  - Lesson: Functions: Code Reuse and Organization

- **`return-values`** (1 lesson)
  - Lesson: Functions: Code Reuse and Organization

- **`markup`** (1 lesson)
  - Lesson: HTML Fundamentals: Building Web Pages

- **`semantic-html`** (1 lesson)
  - Lesson: HTML Fundamentals: Building Web Pages

- **`elements`** (1 lesson)
  - Lesson: HTML Fundamentals: Building Web Pages

- **`styling`** (1 lesson)
  - Lesson: CSS Essentials: Styling Your Web Pages

- **`selectors`** (1 lesson)
  - Lesson: CSS Essentials: Styling Your Web Pages

- **`layout`** (1 lesson)
  - Lesson: CSS Essentials: Styling Your Web Pages

- **`responsive`** (1 lesson)
  - Lesson: CSS Essentials: Styling Your Web Pages

- **`data-analysis`** (1 lesson)
  - Lesson: Pandas for Data Analysis

- **`dataframes`** (1 lesson)
  - Lesson: Pandas for Data Analysis

### Domain Tags
Tags for areas of application:

- **`web`** (2 lessons)
  - Lesson: HTML Fundamentals: Building Web Pages
  - Lesson: CSS Essentials: Styling Your Web Pages

- **`basics`** (1 lesson)
  - Lesson: Introduction to Variables

- **`data-science`** (1 lesson)
  - Lesson: Pandas for Data Analysis

- **`frontend`** (0 lessons)
  - *Coming soon* - JavaScript, React, Vue lessons

- **`backend`** (0 lessons)
  - *Coming soon* - Node.js, Python frameworks

### Subject-Specific Tags

- **`python`** - Topics related to Python language
- **`html`** - Web structure and markup
- **`css`** - Web styling and layout
- **`data-analysis`** - Data analysis and manipulation

---

## Tag Usage Examples

### Example 1: Finding Beginner-Friendly Content
Browse lessons tagged with foundational concepts:

- `variables` (variables and data types)
- `basics` (introductory content)
- `fundamentals` (foundational concepts)

### Example 2: Finding Web Development Lessons
Browse all web-related lessons:

- `web` (web development lessons)
- `html` (web structure)
- `css` (web styling)
- `javascript` (web interactivity)

### Example 3: Finding Data Analysis Content
Browse data-specific lessons:

- `data-analysis`
- `data-science`
- `pandas`

---

## Tag Statistics

| Category | Total Tags | Total Tagged Lessons |
|----------|-----------|----------------------|
| Technology | 5 | 5 |
| Concept | 14 | 5 |
| Domain | 4 | 3 |
| **TOTAL** | **23** | **5** |

---

## Tagging Guidelines

When creating new lessons, follow these guidelines for consistent tagging:

### Do's ✅
- Use lowercase letters and hyphens: `data-analysis`, not `Data_Analysis`
- Choose 3-5 tags per lesson
- Use specific, meaningful tags
- Think about how learners would search

### Don'ts ❌
- Don't use spaces or underscores: `async-await` not `async_await`
- Don't tag the same concept multiple ways: use either `functions` or `function-basics`, not both
- Don't use overly broad tags: `programming` is too broad, use specific tags instead
- Don't tag metadata (use metadata fields instead): difficulty should be in `difficulty` field, not as a tag

### Examples of Good Tags
```yaml
tags: [python, functions, scope]          # Specific and useful
tags: [javascript, async, promises]       # Clear and discoverable
tags: [web, html, semantic-html]          # Domain, technology, concept
```

### Examples to Avoid
```yaml
tags: [Python, JavaScript, learning]      # Capitalization, too generic
tags: [function, functions, func]         # Redundant variations
tags: [beginner, intermediate]            # Should use metadata.difficulty instead
```

---

## Adding New Tags

New tags are automatically indexed when you add them to lessons. To add a new tag:

1. Choose a meaningful, lowercase, hyphenated name
2. Add it to a lesson's frontmatter: `tags: [existing, new-tag]`
3. Submit the lesson via pull request
4. New tag appears in this index automatically

---

## Current Tag Index

### Most Used Tags
1. `python` (3 lessons)
2. `web` (2 lessons)
3. All others (1 lesson each)

### Newest Tags
- `return-values` (added with Functions lesson)
- `semantic-html` (added with HTML lesson)
- `responsive` (added with CSS lesson)
- `dataframes` (added with Pandas lesson)

---

## Want to Find Lessons by Tag?

Currently, browse this page to see which lessons have each tag. In the future, lessons will be filterable by tag with:

- Tag cloud on the homepage
- Tag filter on subject pages
- Global tag search
- Related lessons based on shared tags

---

## See Also

- [Quick Start Guide](quick-start.md) - 10-minute overview
- [Tagging Guide](tagging-guide.md) - How to tag lessons when creating them
- [Metadata Reference](metadata-reference.md) - Complete field specifications

---

*Last updated: January 30, 2026*  
*Total lessons: 5 | Total unique tags: 23*
