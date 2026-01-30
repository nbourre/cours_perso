# Data Model: Lesson Management System

**Feature**: [001-lesson-management-system](../spec.md)  
**Created**: 2026-01-30  
**Purpose**: Define the data structures, entities, and relationships for the lesson management system

## Overview

The lesson management system uses a file-based data model with YAML frontmatter for metadata. All entities are represented as Markdown files and directories in the repository.

## Core Entities

### 1. Subject

**Purpose**: Top-level category for organizing lessons  
**Storage**: Directory under `docs/lessons/[subject]/`  
**Key Attributes**:
- `name` (string): Display name (e.g., "Python Basics")
- `slug` (string): URL-safe identifier (e.g., "python-basics", matches directory name)
- `description` (string, optional): Brief description of the subject
- `order` (integer, optional): Sort order in navigation

**Example**:
```
docs/lessons/python-basics/        # Directory
├── index.md                        # Subject home page with lesson listing
└── [lessons]
```

**Constraints**:
- One subject per directory
- Subject slugs must be lowercase with hyphens
- Subject index.md is mandatory

---

### 2. Lesson

**Purpose**: Individual learning unit with content and metadata  
**Storage**: Markdown file (.md) in subject directory  
**Location**: `docs/lessons/[subject]/lesson-[id]-[slug].md`  
**Key Attributes** (in YAML frontmatter):
- `title` (string, required): Lesson title
- `description` (string, required): One-sentence summary
- `difficulty` (enum, required): "Beginner" | "Intermediate" | "Advanced"
- `duration` (string, required): Estimated learning time (e.g., "30 minutes", "1 hour")
- `tags` (list, required): 1-5 categorical labels for discovery
- `prerequisites` (list, optional): Other lessons required before this one
- `learning_objectives` (list, required): 3-5 learning goals
- `created` (date, required): YYYY-MM-DD format
- `updated` (date, optional): YYYY-MM-DD format
- `author` (string, optional): Lesson creator/contributor
- `status` (enum, optional): "draft" | "published" | "archived"

**YAML Frontmatter Example**:
```yaml
---
title: "Introduction to Python Functions"
description: "Learn how to define, call, and work with functions in Python"
difficulty: "Beginner"
duration: "45 minutes"
tags: [functions, python, variables, code-organization]
prerequisites: []
learning_objectives:
  - "Define and call a function"
  - "Use parameters and return values"
  - "Understand variable scope"
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---
```

**Content Structure** (after frontmatter):
- Learning Objectives (expanded from metadata)
- Prerequisites section (if any)
- Introduction/Context
- Main Content (organized in logical modules)
- Examples and Code
- Exercises
- Assessment/Summary
- Additional Resources

**Constraints**:
- Filename format: `lesson-[id]-[slug].md` (e.g., `lesson-001-functions.md`)
- All required metadata must be present
- Title, description, tags, and learning_objectives must not be empty
- Tags must be lowercase, hyphenated
- Duration must include unit (minutes, hours, days)

---

### 3. Tag

**Purpose**: Categorical label for cross-subject discovery  
**Storage**: Defined in lesson metadata (distributed tagging)  
**Key Attributes**:
- `name` (string): Tag label (e.g., "API", "REST", "authentication")
- `count` (integer, computed): Number of lessons with this tag

**Examples**: "API", "async", "authentication", "backend", "functions", "REST", "variables"

**Constraints**:
- Tags are lowercase, hyphenated (e.g., "async-await", "event-driven")
- 1-5 tags per lesson
- Tags must be meaningful and reusable
- Orphaned tags (0 lessons) automatically disappear from search interface

---

### 4. Metadata

**Purpose**: Structured information about a lesson  
**Storage**: YAML frontmatter in lesson Markdown file  
**Components**:
- Core metadata: title, description, tags, difficulty, duration
- Learning metadata: learning_objectives, prerequisites, status
- Administrative: created, updated, author

**Constraints**:
- All metadata is optional except: title, description, difficulty, duration, tags, learning_objectives
- Dates must follow ISO 8601 format (YYYY-MM-DD)
- Difficulty must be one of: Beginner, Intermediate, Advanced
- Status must be one of: draft, published, archived

---

### 5. Template

**Purpose**: Markdown-based prompt for LLM content generation  
**Storage**: `docs/templates/lesson-template.md` and `docs/templates/llm-prompt-template.txt`  
**Components**:
- Lesson structure template (Markdown with section placeholders)
- LLM prompt template (instructions for prompting an LLM)

**Key Sections**:
1. Metadata section (YAML frontmatter example)
2. Learning Objectives section
3. Prerequisites section
4. Introduction
5. Main Content modules
6. Examples/Code
7. Exercises
8. Assessment

**Constraints**:
- Template must include all required metadata fields
- Section headings must match the standard structure
- Must be easy to copy/paste into an LLM
- Must include clear instructions for filling in placeholders

---

## Relationships

### Subject → Lesson
- **Type**: One-to-Many
- **Cardinality**: One subject contains 1-100+ lessons
- **Path**: `docs/lessons/[subject]/lesson-*.md`
- **Enforcement**: Directory structure enforces subject organization

### Lesson → Tag
- **Type**: Many-to-Many
- **Cardinality**: One lesson has 1-5 tags; one tag applies to 0+ lessons
- **Storage**: Tags stored in lesson metadata
- **Query**: Tag-based filtering queries all lessons and aggregates results

### Lesson → Learning Objectives
- **Type**: One-to-Many
- **Cardinality**: One lesson has 3-5 objectives
- **Storage**: List in metadata and expanded in content

### Lesson → Prerequisites
- **Type**: Many-to-Many (optional)
- **Cardinality**: One lesson may reference 0-3 other lessons
- **Storage**: Lesson IDs in prerequisites list
- **Display**: Subject page highlights prerequisites

---

## Data Validation Rules

### Subject Validation
- [ ] Directory name is lowercase with hyphens
- [ ] `index.md` exists in subject directory
- [ ] Subject title is unique
- [ ] Subject contains at least 1 lesson (warning if empty)

### Lesson Validation
- [ ] All required metadata fields present (title, description, difficulty, duration, tags, learning_objectives)
- [ ] Title is non-empty and unique within subject
- [ ] Difficulty is one of: Beginner, Intermediate, Advanced
- [ ] Duration is non-empty with unit (minutes/hours/days)
- [ ] Tags are lowercase, hyphenated, and 1-5 tags per lesson
- [ ] Learning objectives are 3-5 non-empty items
- [ ] File follows naming convention: `lesson-[id]-[slug].md`
- [ ] Content includes all standard sections
- [ ] No broken internal links to other lessons

### Metadata Validation
- [ ] Dates are ISO 8601 format (YYYY-MM-DD)
- [ ] Status is one of: draft, published, archived
- [ ] Prerequisites reference valid lesson IDs
- [ ] Author field is non-empty if provided

---

## State Transitions

### Lesson Status Lifecycle

```
draft → published → archived
        ↓
      published (can revert to draft)
```

**Transitions**:
- `draft` → `published`: Lesson is ready for learners
- `published` → `archived`: Lesson is no longer maintained
- `published` → `draft`: Lesson needs updates before re-publishing

**Visibility Rules**:
- Only `published` lessons appear in subject indexes and search results
- `draft` lessons are visible only to maintainers/authors
- `archived` lessons are hidden but retained in version control

---

## Storage & Persistence

**Format**: Markdown files with YAML frontmatter  
**Version Control**: Git repository  
**Hosting**: GitHub Pages via GitHub Actions  
**Backup**: Automatic via Git history  
**Scaling**: Up to 1000 lessons supported without performance degradation

**File Structure**:
```
docs/
├── lessons/
│   ├── subject-1/
│   │   ├── index.md
│   │   ├── lesson-001-intro.md
│   │   └── lesson-002-advanced.md
│   └── subject-2/
│       ├── index.md
│       └── lesson-001-basics.md
└── templates/
    ├── lesson-template.md
    └── llm-prompt-template.txt
```

---

## Query Patterns

### Find all lessons in a subject
**Query**: Read `docs/lessons/[subject]/index.md`  
**Returns**: List of lessons in that subject  
**Performance**: O(1) file read

### Find all lessons with a specific tag
**Query**: Search all lesson metadata for tag name  
**Returns**: Lessons across all subjects with matching tag  
**Performance**: O(n) where n = total lessons

### Find lessons by difficulty
**Query**: Filter lessons where difficulty = "Intermediate"  
**Returns**: All lessons at that difficulty level  
**Performance**: O(n) where n = total lessons

### Find prerequisite chain
**Query**: Recursively follow prerequisites from a lesson  
**Returns**: Ordered list of prerequisite lessons  
**Performance**: O(d) where d = depth of prerequisite tree

---

## Assumptions

- All lessons are authored by users and LLMs (no system-generated lessons)
- Lessons can be deleted but not modified retroactively (versioning via Git)
- Metadata is manually maintained by authors (no auto-extraction)
- Tag vocabulary is curated but not centralized (free-form but consistent)
- Search/filter is performed client-side via MkDocs navigation, not server-side
