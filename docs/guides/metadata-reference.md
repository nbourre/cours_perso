# Metadata Specification: YAML Frontmatter

**Purpose**: Define the required and optional metadata fields for all lessons  
**Format**: YAML frontmatter at the top of each lesson Markdown file  
**Location**: First lines of `docs/lessons/[subject]/lesson-*.md`

---

## Frontmatter Structure

All lessons MUST include a YAML frontmatter block at the beginning, enclosed by `---` markers:

```yaml
---
title: "string"
description: "string"
difficulty: "enum"
duration: "string"
tags: [list]
learning_objectives: [list]
prerequisites: [list, optional]
created: "YYYY-MM-DD"
author: "string, optional"
updated: "YYYY-MM-DD, optional"
status: "enum, optional"
---
```

---

## Required Fields

### `title`
- **Type**: String
- **Required**: Yes
- **Description**: The lesson's display name
- **Constraints**:
  - Non-empty
  - 3-100 characters
  - Should be descriptive and action-oriented
  - Unique within subject (recommended)
- **Example**: `"Introduction to Python Functions"`

### `description`
- **Type**: String
- **Required**: Yes
- **Description**: One-sentence summary of the lesson
- **Constraints**:
  - Non-empty
  - 10-200 characters
  - Single sentence (no periods implied)
  - Describes outcome, not process
- **Example**: `"Learn how to define, call, and use functions to organize your code"`

### `difficulty`
- **Type**: Enum
- **Required**: Yes
- **Description**: Target audience level
- **Allowed Values**:
  - `"Beginner"`: No prior knowledge assumed
  - `"Intermediate"`: Basic understanding required
  - `"Advanced"`: Strong foundation required
- **Example**: `difficulty: "Beginner"`

### `duration`
- **Type**: String
- **Required**: Yes
- **Description**: Estimated time to complete lesson
- **Constraints**:
  - Must include numeric value and unit
  - Units: minutes, hours, days
  - Realistic estimate (accounts for exercises)
- **Valid Examples**:
  - `"30 minutes"`
  - `"1 hour"`
  - `"2 hours 30 minutes"`
  - `"1 day"`

### `tags`
- **Type**: List of strings
- **Required**: Yes
- **Description**: Categorical labels for discovery
- **Constraints**:
  - 1-5 tags per lesson
  - Lowercase letters, numbers, hyphens only
  - No spaces
  - Meaningful and reusable
  - Examples: `api`, `async`, `authentication`, `backend`, `rest`
- **Example**: 
  ```yaml
  tags: [functions, python, code-organization, variables]
  ```

### `learning_objectives`
- **Type**: List of strings
- **Required**: Yes
- **Description**: What learners will be able to do
- **Constraints**:
  - 3-5 objectives
  - Start with action verb (understand, create, apply, analyze, etc.)
  - Specific and measurable
  - Achievable within duration
- **Example**:
  ```yaml
  learning_objectives:
    - "Define and call a function"
    - "Use parameters and return values"
    - "Apply functions to organize your code"
  ```

### `created`
- **Type**: Date (ISO 8601)
- **Required**: Yes
- **Description**: Lesson creation date
- **Format**: `YYYY-MM-DD`
- **Example**: `created: 2026-01-30`

---

## Optional Fields

### `prerequisites`
- **Type**: List of strings (lesson IDs)
- **Required**: No
- **Description**: Lessons that should be completed first
- **Constraints**:
  - 0-3 prerequisites recommended
  - Reference valid lesson IDs
  - Can be from same or different subject
- **Example**:
  ```yaml
  prerequisites: [lesson-001-intro, lesson-002-basics]
  ```

### `author`
- **Type**: String
- **Required**: No
- **Description**: Who created or significantly contributed
- **Constraints**:
  - Name or identifier (e.g., "John Smith", "LLM Assistant", "Claude 3.5")
  - If omitted, defaults to repository maintainers
- **Example**: `author: "Claude 3.5 (with human review)"`

### `updated`
- **Type**: Date (ISO 8601)
- **Required**: No
- **Description**: Last modification date
- **Format**: `YYYY-MM-DD`
- **Example**: `updated: 2026-02-15`
- **Note**: Automatically updated by maintainers; authors need not set this

### `status`
- **Type**: Enum
- **Required**: No
- **Default**: `"published"`
- **Description**: Publishing status of the lesson
- **Allowed Values**:
  - `"draft"`: Not ready for learners; visible only to maintainers
  - `"published"`: Ready for learners; visible in all interfaces
  - `"archived"`: No longer maintained; hidden from search/navigation
- **Example**: `status: "published"`

---

## Complete Frontmatter Example

```yaml
---
title: "Advanced Array Methods in JavaScript"
description: "Master array methods like map, filter, and reduce to write functional JavaScript"
difficulty: "Intermediate"
duration: "1 hour 15 minutes"
tags: [javascript, functional-programming, arrays, es6]
learning_objectives:
  - "Understand functional programming concepts"
  - "Use map, filter, and reduce effectively"
  - "Chain array methods for complex transformations"
prerequisites: [lesson-001-array-basics, lesson-002-es6-intro]
created: 2026-01-30
author: "LLM Assistant (ChatGPT-4)"
updated: 2026-02-10
status: "published"
---
```

---

## Validation Rules

### Metadata Completeness
- [ ] All required fields present: title, description, difficulty, duration, tags, learning_objectives, created
- [ ] No empty fields (except optional fields)
- [ ] YAML syntax is valid (no syntax errors)

### Field Value Validation

| Field | Rule | Error Message |
|-------|------|---------------|
| `title` | Non-empty, 3-100 chars | "Title must be 3-100 characters" |
| `description` | Non-empty, 10-200 chars | "Description must be 10-200 characters" |
| `difficulty` | One of: Beginner, Intermediate, Advanced | "Difficulty must be Beginner, Intermediate, or Advanced" |
| `duration` | Contains number + unit (minutes, hours, days) | "Duration must include number and unit (e.g., '30 minutes')" |
| `tags` | 1-5 items, lowercase, hyphenated | "Tags must be 1-5 items, lowercase, hyphenated" |
| `learning_objectives` | 3-5 items, non-empty | "Must have 3-5 learning objectives" |
| `created` | YYYY-MM-DD format | "Created date must be YYYY-MM-DD" |
| `difficulty` | One of: Beginner, Intermediate, Advanced | "Difficulty must be Beginner, Intermediate, or Advanced" |
| `status` | One of: draft, published, archived | "Status must be draft, published, or archived" |

---

## Search & Filter Integration

### By Tag
Metadata tags are used by the search/filter interface to find lessons:
```
User selects tag: "api"
→ System finds all lessons where tags contains "api"
→ Returns matching lessons across all subjects
```

### By Difficulty
Metadata difficulty enables filtering by level:
```
Filter: Difficulty = "Intermediate"
→ System returns all Intermediate lessons
→ Users can narrow by subject + difficulty
```

### By Duration
Metadata duration helps users find lessons they have time for:
```
User searches: "lessons under 1 hour"
→ System parses duration field
→ Returns lessons where duration < 60 minutes
```

### Prerequisites Chain
Metadata prerequisites enables dependency visualization:
```
Lesson A → [prerequisite: Lesson B]
Lesson B → [prerequisite: Lesson C]
→ System displays "Prerequisites: Lesson B → Lesson C"
→ Links help learners start at correct level
```

---

## Examples by Context

### LLM-Generated Lesson
```yaml
---
title: "Python List Comprehensions Explained"
description: "Learn to write concise and readable lists using Python's list comprehension syntax"
difficulty: "Intermediate"
duration: "45 minutes"
tags: [python, lists, functional-programming, syntax]
learning_objectives:
  - "Understand list comprehension syntax"
  - "Convert loops to list comprehensions"
  - "Use conditionals in list comprehensions"
created: 2026-01-30
author: "Claude 3.5 (with human review)"
status: "published"
---
```

### Beginner Lesson
```yaml
---
title: "Getting Started with HTML"
description: "Create your first web page using HTML elements and structure"
difficulty: "Beginner"
duration: "30 minutes"
tags: [html, web, markup, basics]
learning_objectives:
  - "Create a valid HTML document"
  - "Use common HTML elements"
  - "Understand HTML document structure"
created: 2026-01-28
author: "Sarah Chen"
status: "published"
---
```

### Advanced Lesson with Prerequisites
```yaml
---
title: "Designing Microservices Architecture"
description: "Plan and design scalable microservices systems for complex applications"
difficulty: "Advanced"
duration: "3 hours"
tags: [architecture, microservices, system-design, distributed-systems]
learning_objectives:
  - "Evaluate when microservices are appropriate"
  - "Design service boundaries and contracts"
  - "Plan for resilience and observability"
prerequisites: [lesson-005-apis, lesson-008-databases]
created: 2026-01-25
author: "DevOps Team"
status: "published"
---
```

---

## See Also

- [Lesson Template](../templates/lesson-template.md) - Full lesson structure
- [Lesson Workflow Guide](workflow-create-lesson.md) - Step-by-step creation guide
- [Quick Start Guide](quick-start.md) - 10-minute onboarding
