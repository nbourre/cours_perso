# Lesson Creation Workflow Guide

**Purpose**: Step-by-step guide for creating and publishing new lessons  
**Audience**: Content creators, educators, LLM users  
**Time required**: 30-90 minutes depending on approach

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step-by-Step Workflow](#step-by-step-workflow)
4. [Using the LLM Template](#using-the-llm-template)
5. [Quality Checklist](#quality-checklist)
6. [Submission & Review](#submission--review)
7. [FAQ](#faq)

---

## Overview

This workflow describes how to create a new lesson for the repository. Whether you're writing the content yourself or using an LLM (ChatGPT, Claude, etc.) to generate it, this guide will help you produce a lesson that meets repository standards.

**Skill level**: Basic Markdown and command-line comfort helpful but not required

---

## Prerequisites

- [ ] GitHub account (to submit pull requests)
- [ ] Git installed on your computer (download from [git-scm.com](https://git-scm.com))
- [ ] Text editor (VS Code, Sublime, Notepad++, etc.)
- [ ] Basic understanding of Markdown (see [Markdown guide](https://www.markdownguide.org/basic-syntax/))
- [ ] Access to the LLM of your choice if using one (optional)

---

## Step-by-Step Workflow

### Phase 1: Plan Your Lesson

**Time**: 5-10 minutes

1. **Identify the topic**
   - What concept or skill will this lesson teach?
   - Examples: "REST API Design", "Python Functions", "CSS Grid Layout"
2. **Determine the level**
   - Is this for Beginner, Intermediate, or Advanced learners?
   - What prior knowledge is assumed?
3. **Estimate the time**
   - How long should it take to complete (including exercises)?
   - Realistic estimates: 30 min, 45 min, 1 hour, 1.5 hours, 2 hours, etc.
4. **Identify the subject category**
   - Which subject does this fit under? (Python, Web Development, Data Science, etc.)
   - If it doesn't fit, propose a new subject category in your PR description
5. **Choose 3-5 tags**
   - What keywords would help someone discover this lesson?
   - Tags must be lowercase and hyphenated (e.g., `api-design`, `rest`, `http`)

---

### Phase 2: Write or Generate Content

**Time**: 30-60 minutes depending on approach

#### Option A: Write Content Yourself

1. **Copy the lesson template**
   - Download or copy [docs/templates/lesson-template.md](../templates/lesson-template.md)
   - Save as: `lesson-[id]-[slug].md` (e.g., `lesson-001-python-intro.md`)
2. **Fill in metadata** (YAML frontmatter)
   - title, description, difficulty, duration, tags, learning_objectives, created, author
   - See [Metadata Specification](metadata-reference.md) for details
3. **Write content sections**
   - Learning Objectives, Introduction, Main Concepts, Examples, Exercises, Assessment
   - See [Lesson Template Contract](../templates/lesson-template.md) for full structure
4. **Skip to Phase 3** → Review Your Content

#### Option B: Generate with LLM

1. **Prepare your prompt**
   - Decide on: topic, level (Beginner/Intermediate/Advanced), duration
   - Example: "I want to teach JavaScript async/await for Intermediate developers in 1 hour"
2. **Copy the LLM prompt template**
   - See [Using the LLM Template](#using-the-llm-template) below
   - Customize it for your lesson
3. **Paste into your LLM** (ChatGPT, Claude, Gemini, etc.)
   - Use the prompt template
   - Include the lesson structure template
   - Request specific sections: learning objectives, examples, exercises
4. **Copy generated content**
   - Copy the LLM's response (should follow the template structure)
   - Paste into a new file: `lesson-[id]-[slug].md`
5. **Review & refine**
   - Read through for accuracy
   - Fix any inconsistencies with your subject
   - Ensure examples are clear
   - Verify learning objectives are covered
6. **Proceed to Phase 3** → Review Your Content

---

### Phase 3: Review Your Content

**Time**: 5-10 minutes

Use the **Quality Checklist** below to verify your lesson:

**Metadata Check**:

- [ ] All required fields present: title, description, difficulty, duration, tags, learning_objectives, created
- [ ] Title is clear and descriptive (3-100 characters)
- [ ] Description is 1 sentence, non-technical (10-200 characters)
- [ ] Difficulty is: Beginner, Intermediate, or Advanced
- [ ] Duration is realistic and includes unit (minutes/hours/days)
- [ ] Tags are 1-5 items, lowercase, hyphenated
- [ ] Learning objectives are 3-5 items, specific and measurable
- [ ] Created date is in YYYY-MM-DD format

**Content Check**:

- [ ] All required sections present: Learning Objectives, Introduction, Main Concepts, Exercises, Assessment
- [ ] Learning objectives are referenced in the content
- [ ] Examples are clear, relevant, and include code/diagrams
- [ ] Exercises are progressive (simple → complex, 2-3 exercises minimum)
- [ ] Assessment/self-check questions verify learning of each objective
- [ ] Markdown syntax is correct
- [ ] No broken links or references
- [ ] Writing is clear and accessible for the target audience

**Structure Check**:

- [ ] File naming: `lesson-[id]-[slug].md` (e.g., `lesson-001-functions.md`)
- [ ] File located in correct subject directory: `docs/lessons/[subject]/`
- [ ] YAML frontmatter correctly formatted (between `---` markers)
- [ ] Content follows template structure

---

### Phase 4: Create a Git Branch & Commit

**Time**: 5 minutes

1. **Clone the repository** (first time only)
   ```bash
   git clone https://github.com/[username]/[repo].git
   cd [repo]

   ```
2. **Create a new branch**
   ```bash
   git checkout -b add-lesson-[slug]
   # Example: git checkout -b add-lesson-python-functions

   ```
3. **Add your lesson file**
   ```bash
   git add docs/lessons/[subject]/lesson-[id]-[slug].md

   ```
4. **Commit your changes**
   ```bash
   git commit -m "Add lesson: [Title]"
   # Example: git commit -m "Add lesson: Introduction to Python Functions"

   ```
5. **Push to your fork**
   ```bash
   git push origin add-lesson-[slug]

   ```

---

### Phase 5: Submit a Pull Request

**Time**: 5 minutes

1. **Go to GitHub**
   - Navigate to the repository on GitHub
   - Click "Compare & pull request" (should appear after you push)
2. **Fill in PR details**
   - **Title**: "Add lesson: [Title]"
   - **Description**: Include:
     - Brief summary of what the lesson teaches
     - Difficulty level and estimated duration
     - Subject category
     - Any notes for reviewers
3. **Request review**
   - Assign to repository maintainers
   - Add label: "lesson-submission"
4. **Wait for feedback**
   - Maintainers will review for quality and compliance
   - May request changes (don't worry, this is normal!)
   - Approved lessons are merged and automatically published to GitHub Pages

---

## Using the LLM Template

### Quick Start

Copy and paste this template into your LLM, customizing the bracketed sections:

```
Create an educational lesson on [TOPIC] for [LEVEL] learners.
The lesson should take approximately [DURATION] to complete.

Use this exact Markdown structure:

---
title: "[LESSON TITLE]"
description: "[One-sentence summary]"
difficulty: "[LEVEL]"
duration: "[DURATION]"
tags: [tag1, tag2, tag3]
learning_objectives:
  - "Objective 1"
  - "Objective 2"
  - "Objective 3"
created: 2026-01-30
author: "[Your Name or 'LLM Assistant']"
status: "published"
---

# [LESSON TITLE]

## Learning Objectives

By the end of this lesson, you will be able to:
- [Objective 1]
- [Objective 2]
- [Objective 3]

## Introduction

[2-3 paragraphs introducing the topic, why it matters, and what problems it solves]

## [Main Concept 1]

[Explain this concept with examples and code]

## [Main Concept 2]

[Explain this concept with examples]

## Exercises

### Exercise 1: [Title]
[Beginner exercise - simple task to practice basic concept]

### Exercise 2: [Title]
[Intermediate exercise - apply concept in realistic scenario]

### Challenge (Optional)
[Advanced exercise for motivated learners]

## Assessment

### Self-Check Questions
1. [Question to verify understanding of Objective 1]
2. [Question to verify understanding of Objective 2]
3. [Question to verify understanding of Objective 3]

## Summary

[Recap the key points]

---

Important requirements:
- Explanations must be clear and accessible for [LEVEL] learners
- Include at least 2-3 practical examples with code or walkthroughs
- Make exercises progressive (easy → hard)
- Ensure the lesson is completable in [DURATION]
- Use plain language; explain technical terms
- Content should be ready to paste directly into a Markdown file
```

### Customization Tips

**For different levels**:

- **Beginner**: Assume no prior knowledge; explain every term; use analogies
- **Intermediate**: Assume basic understanding; focus on application; include best practices
- **Advanced**: Assume strong foundation; dive deep; discuss trade-offs and edge cases

**For different durations**:

- **30 minutes**: 1 main concept, 2 simple exercises
- **1 hour**: 2-3 concepts, 2-3 exercises of increasing difficulty
- **2+ hours**: Multiple concepts, exercises, project/capstone

**For different topics**:

- Replace [TOPIC] with specific skill (e.g., "REST API Design")
- Replace [LEVEL] with difficulty (e.g., "Intermediate")
- Replace [DURATION] with time estimate (e.g., "1 hour")

---

## Quality Checklist

Before submitting, verify:

### Content Quality

- [ ] Lesson teaches a clear, single concept (not multiple unrelated topics)
- [ ] Learning objectives are specific and achievable
- [ ] Content directly addresses each learning objective
- [ ] Examples are relevant to the topic and target audience
- [ ] Exercises reinforce learning objectives
- [ ] No outdated information or deprecated tools

### Completeness

- [ ] All required sections are present
- [ ] No placeholder text remaining (e.g., "[YOUR TOPIC HERE]")
- [ ] All links are correct and active
- [ ] Code examples are syntactically correct
- [ ] Formatting is consistent throughout

### Accessibility

- [ ] Language is clear and avoids jargon (or explains it)
- [ ] Concepts are explained before use
- [ ] Examples build from simple to complex
- [ ] Suggested prerequisite lessons are accurate
- [ ] Content is appropriate for stated difficulty level

### Technical

- [ ] Markdown syntax is valid
- [ ] YAML frontmatter is correctly formatted
- [ ] File is in correct location: `docs/lessons/[subject]/`
- [ ] File naming follows convention: `lesson-[id]-[slug].md`
- [ ] Metadata fields are complete and valid

---

## Submission & Review

### What Happens After You Submit?

1. **Automated Checks** (5-10 minutes)
   - GitHub Actions validates Markdown syntax
   - Checks for required metadata fields
   - Verifies file naming and location
   - Status appears in PR as a checkmark or ✗
2. **Maintainer Review** (24-48 hours)
   - Reviewers read your lesson
   - Verify accuracy and quality
   - Check alignment with repository style
   - May request changes (this is normal!)
3. **Feedback & Iteration** (as needed)
   - Respond to reviewer comments
   - Make requested changes
   - Push updates to your branch (PR updates automatically)
   - Reviewers re-check
4. **Approval & Merge** (24 hours after approval)
   - Lesson is merged into main branch
   - GitHub Actions builds and deploys site
   - Your lesson is live on GitHub Pages!

### Common Feedback

**"Please add an exercise"** → Add 2-3 exercises practicing key concepts  
**"This assumes too much prior knowledge"** → Add explanation or link to prerequisite  
**"Example code doesn't run"** → Test and fix the code  
**"Metadata incomplete"** → Add missing fields from template  
**"Tone doesn't match audience"** → Simplify or deepen depending on level

---

## FAQ

### Q: Can I use an LLM to generate the entire lesson?
**A**: Yes! Use the LLM template to prompt ChatGPT, Claude, etc. Always review the generated content for accuracy before submitting. You don't need to write content from scratch.

### Q: What if my lesson spans multiple subjects?
**A**: Place it in the primary subject and mention related subjects in the "Next Steps" section. We can add cross-references in future updates.

### Q: How long should a lesson be?
**A**: Aim for 30 minutes to 2 hours of content. If it's getting longer, consider breaking it into multiple lessons.

### Q: Can I use external links and resources?
**A**: Yes, but verify they work before submitting. Link to authoritative sources (docs, official guides, peer-reviewed content).

### Q: What if I want to update a lesson after it's published?
**A**: Submit a PR with changes. Maintainers will review and merge. The site auto-updates.

### Q: Can I delete a lesson?
**A**: Instead of deleting, set `status: "archived"` so it's hidden but retained in version control.

### Q: What if I don't know Git/GitHub?
**A**: GitHub has great tutorials. Alternatively, email your lesson to maintainers and they can submit it for you.

### Q: How many lessons can I submit?
**A**: As many as you'd like! One at a time or batch them. Each goes through review process.

### Q: Can I reuse content from my blog/course?
**A**: Yes, if you own the content or have permission. Provide original source in author field (e.g., "Adapted from my course on X").

---

## Next Steps

1. **Review the [Metadata Specification](metadata-reference.md)** for field details
2. **Choose your approach**: Write content or generate with LLM
3. **Create your lesson** using steps above
4. **Submit as a pull request** and wait for review
5. **Celebrate!** Your lesson is now part of the repository

Have questions? Open an issue on GitHub or email the maintainers.
