# Tagging Guide: Organize Lessons for Discovery

**Purpose**: Learn how to use tags effectively to make lessons discoverable  
**Audience**: Content creators, lesson authors  
**Goal**: Help learners find lessons through cross-subject tag-based search

---

## What Are Tags?

Tags are 1-5 keywords attached to each lesson that describe its content and make it discoverable. Unlike the Subject (Python, Web Development, etc.), tags enable **cross-subject discovery**.

**Example**: A lesson on "Database Design" in Web Development could be tagged with:

- `database` (learners can find all DB lessons)
- `system-design` (learners can find architecture lessons)
- `scalability` (learners interested in performance)
- `sql` (learners looking for database languages)
- `schema` (learners designing data structures)

---

## Tag Categories

### Technology Tags
The specific tools, languages, or frameworks:

- `python`, `javascript`, `java`, `golang`, `rust`
- `react`, `vue`, `angular`
- `postgresql`, `mongodb`, `redis`
- `docker`, `kubernetes`
- `git`, `github`, `gitlab`

### Concept Tags
Abstract ideas and patterns:

- `functions`, `loops`, `conditionals`
- `async`, `promises`, `callbacks`
- `authentication`, `authorization`
- `api`, `rest`, `graphql`
- `recursion`, `sorting`, `searching`

### Domain Tags
Areas of application:

- `web`, `backend`, `frontend`
- `data-analysis`, `visualization`
- `machine-learning`, `ai`
- `devops`, `infrastructure`
- `security`, `cryptography`

### Difficulty Indicators** (optional, also in metadata):

- `beginner-friendly`, `intermediate-focused`, `advanced-concepts`

### Cross-Cutting Tags
Meta-information:

- `performance`, `optimization`
- `testing`, `debugging`
- `documentation`
- `best-practices`

---

## Tagging Rules

### 1. Use 1-5 Tags Per Lesson

- **Minimum**: 1 tag (though 3+ recommended)
- **Maximum**: 5 tags (avoid tag bloat)
- **Sweet spot**: 3-4 tags per lesson

### 2. Lowercase, Hyphenated Format
Tags must be:

- ✅ Lowercase: `python-basics`, not `Python_Basics`
- ✅ Hyphenated: `rest-api`, not `rest_api` or `restapi`
- ✅ No spaces: `machine-learning`, not `machine learning`
- ✅ No special chars: `async-await`, not `async/await`

### 3. Be Specific, Not Redundant

**Good**:
```yaml
tags: [python, functions, scope]
```

**Avoid Redundancy**:
```yaml
tags: [python, python-functions, python-scope]  # Too specific, overlapping
```

**Too Broad**:
```yaml
tags: [programming, learning]  # Not helpful for discovery
```

### 4. Think Like a Learner

Ask yourself: "What would I search for to find this lesson?"

**Example lesson**: "Async/Await in JavaScript"

**Learner searches**:

- "async" → Found ✅
- "javascript" → Found ✅
- "callbacks" → Missing ❌ (add tag: `callbacks`)
- "promises" → Missing ❌ (add tag: `promises`)

**Better tags**: `[javascript, async, promises, callbacks, es6]`

---

## Tagging by Subject

### Python Basics
Common tags for Python lessons:

- Language: `python`, `python3`
- Concepts: `variables`, `functions`, `loops`, `classes`, `modules`
- Domains: `data-science`, `web`, `scripting`
- Techniques: `debugging`, `testing`, `performance`

**Example lesson**: "Python Functions"
```yaml
tags: [python, functions, code-organization, scope, parameters]
```

### Web Development
Common tags for Web lessons:

- Languages: `html`, `css`, `javascript`, `typescript`
- Frameworks: `react`, `vue`, `angular`, `nextjs`
- Concepts: `dom`, `async`, `api`, `rest`, `graphql`
- Architecture: `ssr`, `spa`, `pwa`

**Example lesson**: "Building REST APIs with Node.js"
```yaml
tags: [nodejs, api, rest, express, backend]
```

### Data Science
Common tags for Data Science lessons:

- Languages: `python`, `sql`, `r`
- Libraries: `pandas`, `numpy`, `matplotlib`, `sklearn`
- Concepts: `data-cleaning`, `visualization`, `statistics`, `machine-learning`
- Domains: `analytics`, `prediction`, `classification`

**Example lesson**: "Data Visualization with Matplotlib"
```yaml
tags: [python, matplotlib, data-visualization, pandas, analysis]
```

---

## Tag Selection Examples

### Case 1: Python List Comprehensions

**Topic**: "Use list comprehensions to write concise Python code"

**Potential tags**:

- `python` ✅ (primary technology)
- `list-comprehensions` ✅ (specific concept)
- `functional-programming` ✅ (programming paradigm)
- `syntax` ✅ (type of learning)
- `code-organization` ✅ (benefit)

**Final tags**:
```yaml
tags: [python, list-comprehensions, functional-programming, syntax]
```

### Case 2: REST API Design

**Topic**: "Design RESTful APIs following best practices"

**Potential tags**:

- `api` ✅ (primary concept)
- `rest` ✅ (specific architecture)
- `http` ✅ (underlying protocol)
- `web` ✅ (domain)
- `backend` ✅ (component)
- `system-design` ✅ (category)
- `best-practices` ✅ (meta-tag)

**Final tags** (pick 5 max):
```yaml
tags: [api, rest, http, backend, system-design]
```

### Case 3: React Hooks

**Topic**: "Learn React Hooks to manage state in functional components"

**Potential tags**:

- `react` ✅ (primary framework)
- `javascript` ✅ (language)
- `hooks` ✅ (specific feature)
- `state-management` ✅ (concept)
- `frontend` ✅ (domain)
- `es6` ✅ (JavaScript version)

**Final tags**:
```yaml
tags: [react, javascript, hooks, state-management, frontend]
```

---

## Tag Discovery: How Learners Use Tags

### Browse by Tag (Future Feature)

```
Homepage → Tag Cloud
Click "python" → See all Python lessons
  ├── Lesson 1: "Python Functions"
  ├── Lesson 2: "List Comprehensions"
  └── Lesson 3: "Classes and OOP"
```

### Multi-Tag Filter

```
Filter: ["python", "async"]
→ Shows only lessons tagged with BOTH python AND async
→ Example: "Asyncio in Python"
```

### Tag Pages

Each tag gets its own page:

- `/tags/python/` → All Python lessons
- `/tags/react/` → All React lessons
- `/tags/testing/` → All testing-related lessons

---

## Common Tagging Mistakes

### ❌ Mistake 1: Too Specific/Nested

```yaml
tags: [python, python-basics, python-functions, python-scope]
```

**Problem**: Redundant, duplicates subject/metadata  
**Fix**: `tags: [python, functions, scope]`

### ❌ Mistake 2: Too Vague

```yaml
tags: [learning, tutorial, web]
```

**Problem**: Not helpful for finding this specific lesson  
**Fix**: `tags: [javascript, react, hooks, state-management]`

### ❌ Mistake 3: Multiple Words as One Tag

```yaml
tags: [machine learning, data visualization]
```

**Problem**: Markdown/YAML expects hyphenation  
**Fix**: `tags: [machine-learning, data-visualization]`

### ❌ Mistake 4: Inconsistent Capitalization

```yaml
tags: [Python, functions, LOOPS]
```

**Problem**: Breaks tag aggregation (Python ≠ python)  
**Fix**: `tags: [python, functions, loops]`

### ❌ Mistake 5: Mixing Levels

```yaml
tags: [beginner, intermediate]
```

**Problem**: Metadata already specifies difficulty  
**Fix**: Use single-level tags like `beginner-friendly` (optional) OR omit and use metadata.difficulty

---

## Tag Maintenance

### Adding New Tags

It's okay to introduce new tags as you create lessons. The system automatically indexes them.

**Process**:

1. Use a new tag in your lesson: `tags: [python, decorators, ...]`
2. Submit PR
3. Maintainers approve
4. Tag appears in tag cloud and tag pages

### Deprecating Tags

If a tag becomes outdated (e.g., Python 2 → Python 3):

**Process**:

1. Create alias or replacement tag
2. Update existing lessons to new tag
3. Gradually phase out old tag
4. Remove from tag index

### Standardizing Tags

Occasionally, maintainers may standardize tags:

- `async-await` vs `asyncio` → Standardize to `async-await`
- `db` vs `database` → Standardize to `database`

Your existing lessons will be updated automatically.

---

## Quick Reference

### Tag Format
```yaml
tags: [word1, word2-word3, word4]  # lowercase, hyphenated
```

### Recommended Tags by Subject

**Python**:
`python`, `functions`, `loops`, `classes`, `async`, `testing`, `data-science`

**Web Development**:
`javascript`, `react`, `css`, `html`, `api`, `rest`, `frontend`, `backend`

**Data Science**:
`python`, `pandas`, `data-analysis`, `visualization`, `machine-learning`, `statistics`

### Tag Workflow

1. Choose 3-5 tags that answer: "What would someone search for to find this?"
2. Use lowercase, hyphenated format
3. Be specific but not redundant
4. Verify no metadata/subject overlap

---

## See Also

- [Metadata Reference](metadata-reference.md) - Full field specifications
- [Lesson Workflow Guide](workflow-create-lesson.md) - Complete creation workflow
- [Quick Start Guide](quick-start.md) - 10-minute overview

---

## Examples

**Python Functions Lesson**:
```yaml
tags: [python, functions, parameters, scope, code-organization]
```

**REST API Design Lesson**:
```yaml
tags: [api, rest, http, web-services, backend]
```

**React Hooks Lesson**:
```yaml
tags: [react, javascript, hooks, functional-components, state]
```

**Machine Learning Intro**:
```yaml
tags: [machine-learning, python, scikit-learn, classification, data-science]
```

---

Ready to tag your lessons? 🏷️
