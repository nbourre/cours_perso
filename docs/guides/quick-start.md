# Quick Start Guide: Lesson Management System

**Purpose**: Get up and running with lessons and content creation in 10 minutes  
**Audience**: New users, educators, content creators

---

## 1. Browse Existing Lessons (2 minutes)

1. **Visit the documentation site** → GitHub Pages URL
2. **Click on a subject** from the homepage (e.g., "Python", "Web Development")
3. **View lessons in that subject** with difficulty level, duration, and tags
4. **Click a lesson** to read and learn
5. **Search by tags** using the filter/search feature (coming soon)

---

## 2. Understand Lesson Structure (2 minutes)

Every lesson has:

```markdown
---
title: "Lesson Title"
description: "What you'll learn"
difficulty: "Beginner | Intermediate | Advanced"
duration: "30 minutes to 2 hours"
tags: [tag1, tag2, tag3]
learning_objectives: [objective1, objective2, objective3]
---

# Lesson Title

## Learning Objectives
- What you'll be able to do

## Introduction
- Why this matters

## Main Content Sections
- Core concepts with examples

## Exercises
- Practice tasks

## Assessment
- Self-check questions

## Summary & Next Steps
- Recap and what's next
```

---

## 3. Create Your First Lesson (5 minutes)

### Method A: Quick Manual Entry

1. **Download template**: Copy [lesson-template.md](../templates/lesson-template.md)
2. **Fill in metadata** at the top:
   - Title, description, difficulty, duration, tags, learning objectives
3. **Write content** in the sections provided
4. **Save as**: `docs/lessons/[subject]/lesson-[id]-[slug].md`
5. **Submit via GitHub** (create a pull request)

### Method B: Generate with LLM (Recommended)

1. **Copy the LLM prompt template** → Paste into ChatGPT/Claude/etc.
2. **Customize the prompt**:
   - Replace `[TOPIC]` with your lesson topic
   - Replace `[LEVEL]` with difficulty (Beginner/Intermediate/Advanced)
   - Replace `[DURATION]` with time estimate (e.g., "1 hour")
3. **Submit the prompt** to your LLM
4. **Copy the response** (entire generated lesson)
5. **Paste into a file**: `lesson-[id]-[slug].md`
6. **Review for accuracy** (fix any errors or unclear sections)
7. **Submit via GitHub** (create a pull request)

---

## 4. Submit Your Lesson to the Repository (3 minutes)

1. **Fork the repository** on GitHub (if first time)
2. **Create a new branch**: `git checkout -b add-lesson-your-topic`
3. **Add your file**: `git add docs/lessons/[subject]/lesson-*.md`
4. **Commit**: `git commit -m "Add lesson: Your Lesson Title"`
5. **Push**: `git push origin add-lesson-your-topic`
6. **Create pull request** on GitHub with description
7. **Wait for review** (24-48 hours typically)
8. **Done!** Your lesson is published after merge

---

## 5. Key Files & Links

| What | Where | Link |
|------|-------|------|
| **Create a lesson** | Full workflow guide | [Lesson Workflow Guide](workflow-create-lesson.md) |
| **Lesson structure** | Template | [lesson-template.md](../templates/lesson-template.md) |
| **Metadata fields** | Specification | [Metadata Reference](metadata-reference.md) |
| **LLM template** | In templates folder | `docs/templates/llm-prompt-template.txt` |
| **Data model** | Design docs | [../data-model.md](../data-model.md) |

---

## 6. Subject Categories

Default subjects available:

- 📘 **Python Basics** → Python fundamentals, syntax, libraries
- 🌐 **Web Development** → HTML, CSS, JavaScript, frameworks
- 📊 **Data Science** → Analytics, visualization, machine learning

**Need a new subject?** Mention it in your PR description. Maintainers will create the category.

---

## 7. Tags (For Organization)

Use tags to make lessons discoverable across subjects. Examples:

- **Technology**: `python`, `javascript`, `database`, `api`
- **Concept**: `functions`, `loops`, `async`, `authentication`
- **Difficulty**: `beginner-friendly`, `intermediate`, `advanced`
- **Domain**: `web`, `data`, `systems`, `security`

**Choose 1-5 tags per lesson** that help learners find related content.

---

## 8. Metadata Cheat Sheet

Required for every lesson:

| Field | Example | Notes |
|-------|---------|-------|
| `title` | "Python Functions 101" | 3-100 chars, clear title |
| `description` | "Learn to write reusable functions" | 1 sentence, non-technical |
| `difficulty` | "Beginner" | One of: Beginner, Intermediate, Advanced |
| `duration` | "45 minutes" | Include unit (minutes/hours/days) |
| `tags` | [python, functions, reuse] | 1-5 items, lowercase, hyphenated |
| `learning_objectives` | See template | 3-5 specific outcomes |
| `created` | 2026-01-30 | YYYY-MM-DD format |

Optional:

| Field | Example |
|-------|---------|
| `author` | "Claude 3.5" or "Jane Smith" |
| `prerequisites` | [lesson-001-intro] |
| `updated` | 2026-02-15 |
| `status` | "published" (draft, published, archived) |

---

## 9. Common Tasks

### Add tags to a lesson
```yaml
tags: [api, rest, http, backend]  # Add up to 5
```

### Link to a prerequisite lesson
```yaml
prerequisites: [lesson-001-basics, lesson-002-intermediate]
```

### Mark a lesson as draft (not published yet)
```yaml
status: "draft"
```

### Update a lesson you've already published
- Submit a new PR with the updated file
- Maintainers review and merge
- Site auto-updates within minutes

---

## 10. Checklist Before Submitting

Before you create your pull request:

- [ ] Metadata complete: title, description, difficulty, duration, tags, learning_objectives, created
- [ ] All required sections present: Learning Objectives, Introduction, Main Content, Exercises, Assessment
- [ ] Markdown syntax is valid (no broken formatting)
- [ ] Examples are clear and correct
- [ ] Exercises are relevant and progressive (simple → complex)
- [ ] Links work and are relevant
- [ ] File in correct location: `docs/lessons/[subject]/lesson-*.md`
- [ ] File naming follows convention: `lesson-[id]-[slug].md`

---

## Next Steps

1. **Read the full [Lesson Workflow Guide](workflow-create-lesson.md)** for detailed instructions
2. **Copy the [Lesson Template](../templates/lesson-template.md)** to start writing
3. **Use the LLM template** if generating content
4. **Submit your first lesson!**

---

## Need Help?

- **Questions about structure?** → See [Lesson Template](../templates/lesson-template.md)
- **Questions about metadata?** → See [Metadata Reference](metadata-reference.md)
- **Need detailed workflow?** → See [Lesson Workflow Guide](workflow-create-lesson.md)
- **Want to understand the design?** → See [Data Model](../data-model.md)
- **Open issues on GitHub** or email maintainers

---

## Examples

### Beginner Lesson on Python Functions
```yaml
---
title: "Introduction to Python Functions"
description: "Learn to write reusable functions to organize your code"
difficulty: "Beginner"
duration: "45 minutes"
tags: [python, functions, code-organization]
learning_objectives:
  - "Define and call a function"
  - "Use parameters and return values"
  - "Understand variable scope"
created: 2026-01-30
author: "LLM Assistant"
---
```

### Intermediate Lesson on REST APIs
```yaml
---
title: "Building REST APIs with Flask"
description: "Create your first RESTful web service using Python and Flask"
difficulty: "Intermediate"
duration: "1 hour 30 minutes"
tags: [api, rest, flask, python, backend]
learning_objectives:
  - "Understand REST principles and HTTP methods"
  - "Build endpoints using Flask"
  - "Handle requests and responses"
prerequisites: [lesson-001-python-basics, lesson-005-http-intro]
created: 2026-01-30
author: "Claude 3.5"
---
```

---

**Ready to create?** Start with the [Workflow Guide](workflow-create-lesson.md) or dive right in with the template! 🚀
