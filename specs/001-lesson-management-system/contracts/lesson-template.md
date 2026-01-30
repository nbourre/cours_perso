# Lesson Template Contract

**Purpose**: Standard Markdown structure for all lessons  
**Location**: `docs/templates/lesson-template.md` (user-facing template)  
**Required**: All lessons MUST follow this structure

---

## Template Structure

```markdown
---
title: "[Lesson Title]"
description: "[One-sentence summary of what learners will learn]"
difficulty: "Beginner"  # Options: Beginner, Intermediate, Advanced
duration: "30 minutes"  # Include unit (minutes, hours, days)
tags: [tag1, tag2, tag3]  # 1-5 lowercase, hyphenated tags
prerequisites: []  # Optional: lesson IDs that should be completed first
learning_objectives:
  - "Learning objective 1"
  - "Learning objective 2"
  - "Learning objective 3"
created: 2026-01-30
author: "Your Name or LLM Assistant"
status: "published"  # Options: draft, published, archived
---

# [Lesson Title]

## Learning Objectives

By the end of this lesson, you will be able to:
- [Learning objective 1]
- [Learning objective 2]
- [Learning objective 3]

## Prerequisites

[If applicable, list any prerequisites or link to prerequisite lessons]

**Note**: It's recommended to complete [Lesson Name] before starting this lesson.

## Introduction

[Provide context and motivation. Why should learners care about this topic? What problem does it solve?]

## [Main Concept/Module 1]

[Explain the first key concept with clear examples and explanations]

### Example 1: [Specific Example]

[Provide a concrete, relatable example]

### Example 2: [Another Example]

[Provide another example demonstrating a different aspect]

## [Main Concept/Module 2]

[Explain the second key concept]

### Example 1: [Specific Example]

[Provide examples with code, diagrams, or walkthroughs]

## [Main Concept/Module 3] (Optional)

[Add more modules as needed]

## Exercises

### Exercise 1: [Descriptive Title]

**Difficulty**: Beginner  
**Time**: 5-10 minutes

[Describe the exercise and what learners should do]

**Expected outcome**: [What should the learner be able to do/create]

### Exercise 2: [Descriptive Title]

**Difficulty**: Intermediate  
**Time**: 15-20 minutes

[Describe a more challenging exercise]

### Challenge Exercise (Optional)

[Advanced exercise for motivated learners]

## Assessment

### Self-Check Questions

1. [Question 1 to verify understanding]
2. [Question 2]
3. [Question 3]

### Project or Capstone

[Optional: Describe a project that integrates all concepts from the lesson]

## Summary

[Recap the key points learned in this lesson]

## Additional Resources

- [Link 1: Related documentation]
- [Link 2: Tutorial or tool]
- [Link 3: Reference material]

## Next Steps

After completing this lesson, you may want to explore:
- [Suggested follow-up lesson 1]
- [Suggested follow-up lesson 2]
- [Related concept or skill]

---

## Metadata Validation Checklist

- [ ] All required metadata fields present (title, description, difficulty, duration, tags, learning_objectives)
- [ ] Title is clear and descriptive
- [ ] Description is 1 sentence, non-technical
- [ ] Difficulty is one of: Beginner, Intermediate, Advanced
- [ ] Duration includes unit (minutes, hours, days)
- [ ] Tags are 1-5 items, lowercase, hyphenated
- [ ] Learning objectives are 3-5 specific, measurable outcomes
- [ ] Status is one of: draft, published, archived
- [ ] Created date is in YYYY-MM-DD format

## Content Validation Checklist

- [ ] All required sections present: Learning Objectives, Introduction, Main Concepts, Exercises, Assessment
- [ ] Learning objectives are referenced and addressed in content
- [ ] Examples are clear, relevant, and include code/diagrams where appropriate
- [ ] Exercises are progressive (simple → complex)
- [ ] Assessment verifies learning of all objectives
- [ ] Links to prerequisites and related lessons are correct
- [ ] No broken links or references
- [ ] Markdown syntax is correct (renders properly in MkDocs)
```

---

## Usage Instructions

### For Content Creators

1. Copy this template to a new file: `lesson-[id]-[slug].md`
2. Fill in all metadata fields (title, description, difficulty, tags, etc.)
3. Replace placeholder sections with your content
4. Ensure all required sections are present
5. Add examples and exercises specific to your topic
6. Test by running `mkdocs serve` and viewing the rendered lesson
7. Submit a pull request with your new lesson

### For LLM Prompt Generation

When using an LLM (ChatGPT, Claude, etc.) to generate lesson content:

1. Fill in only the metadata section with your lesson details
2. Provide the template structure to the LLM with instruction to fill in sections
3. Paste the following prompt into your LLM:

**LLM Prompt Template**:
```
I want you to create an educational lesson following this exact Markdown structure.
The lesson should be for [audience/level] and teach [topic/concept].

Use this template:
[Paste template here]

Important requirements:
- Keep explanations clear and accessible for the target audience
- Include 2-3 practical examples with code/diagrams
- Create 2-3 exercises (progressive difficulty)
- Include self-check questions for assessment
- Use plain language, avoid jargon (or explain it)
- Ensure the lesson can be completed in approximately [duration]

Generated content should be ready to paste directly into a Markdown file.
```

4. Copy the generated content into the template file
5. Review for accuracy and alignment with learning objectives
6. Submit for publication

---

## Compliance Notes

- Every published lesson MUST conform to this template
- Lessons missing required sections will be marked as "draft" status until completed
- Automated validation (GitHub Actions) will check compliance before deployment
- Template updates are backward-compatible (existing lessons will still render)
