# Using LLM Templates for Lesson Generation

**Purpose**: Learn how to use AI assistants to generate high-quality lesson content efficiently  
**Audience**: Content creators who want to use ChatGPT, Claude, or other LLMs  
**Time**: 15-30 minutes from prompt to publishable lesson

---

## Overview

Instead of writing lessons from scratch, you can use Large Language Models (LLMs) like ChatGPT, Claude, or Gemini to generate lesson content that follows our template. This guide shows you how to get the best results.

**Key Benefits**:

- ✅ Generate complete lessons in 15-30 minutes
- ✅ Consistent structure every time
- ✅ LLM handles repetitive parts (examples, exercises)
- ✅ You focus on review and refinement
- ✅ No coding required

---

## Quick Start: 5-Minute Example

### Step 1: Prepare Your Topic
```
Topic: "Python Functions for Beginners"
Level: Beginner
Duration: 45 minutes
Preferred LLM: ChatGPT 4
```

### Step 2: Copy the LLM Prompt Template
See [Workflow Guide - Using the LLM Template](workflow-create-lesson.md#using-the-llm-template) for the full template.

### Step 3: Customize & Paste
Replace the placeholders:

- [TOPIC] → "Python Functions"
- [LEVEL] → "Beginner"
- [DURATION] → "45 minutes"

### Step 4: Run in Your LLM

- ChatGPT: Paste into chat
- Claude: Paste into new conversation
- Gemini: Paste into compose

### Step 5: Review Output

- Read through for accuracy
- Check examples work
- Verify exercises are clear
- Fix any issues

### Step 6: Save & Submit
Save as `lesson-001-python-functions.md` and submit via PR.

---

## Detailed Workflow

### 1. Choose Your LLM

**ChatGPT (GPT-4)**:

- Pros: Fast, creative, good at explanations
- Cons: Requires paid account
- Best for: Narrative content, examples

**Claude (Sonnet 3)**:

- Pros: Long context, precise, handles code well
- Cons: Requires account
- Best for: Code examples, technical accuracy

**Gemini (Google)**:

- Pros: Free option, integrates with Google docs
- Cons: May vary in quality
- Best for: Quick generation, drafts

**Local LLMs** (Ollama, LLaMA):

- Pros: Free, private, fast
- Cons: May need tweaking
- Best for: Draft generation, testing

**Recommendation**: Start with ChatGPT 4 or Claude for best results.

---

### 2. Prepare Your Lesson Brief

Before using the template, gather these details:

**Topic Details**:

- [ ] Specific topic name (not too broad, not too narrow)
- [ ] Example: "Python List Comprehensions" (good) vs. "Python" (too broad)

**Target Audience**:

- [ ] Difficulty: Beginner, Intermediate, or Advanced
- [ ] Prior knowledge assumed
- [ ] Example: "Beginner Python learners who know loops and lists"

**Time Constraint**:

- [ ] Duration: 30 min, 45 min, 1 hour, 1.5 hours, 2 hours
- [ ] Includes exercises and self-assessment
- [ ] Example: "1 hour including exercises"

**Subject Category**:

- [ ] Which subject: Python, Web Development, Data Science, etc.
- [ ] Example: "Python Basics"

**Tags** (optional, you can add later):

- [ ] 3-5 keywords for discovery
- [ ] Example: [python, lists, functional-programming, syntax]

---

### 3. Use the LLM Prompt Template

### Format: Structured Prompt with Clear Requirements

```
Create an educational lesson on [TOPIC] for [LEVEL] learners.
The lesson should take approximately [DURATION] to complete.

Use this exact Markdown structure:

[FULL TEMPLATE HERE]

Important requirements:

- Explanations must be clear and accessible for [LEVEL] learners
- Include at least 2-3 practical examples with code or walkthroughs
- Make exercises progressive (easy → hard)
- Ensure the lesson is completable in [DURATION]
- Use plain language; explain technical terms
- Content should be ready to paste directly into a Markdown file
```

### Example: Real Prompt

```
Create an educational lesson on JavaScript Async/Await for Intermediate learners.
The lesson should take approximately 1 hour to complete.

Use this exact Markdown structure:

---
title: "Mastering Async/Await in JavaScript"
description: "Learn to write clean asynchronous JavaScript using async/await syntax"
difficulty: "Intermediate"
duration: "1 hour"
tags: [javascript, async, promises, es2017]
learning_objectives:
  - "Understand how async/await works"
  - "Convert Promises to async/await"
  - "Handle errors in async functions"
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# Mastering Async/Await in JavaScript

[... rest of template ...]

Important requirements:

- Explanations must be clear for Intermediate learners
- Include 2-3 practical examples with runnable code
- Make exercises progressive (easy → hard)
- Ensure completable in 1 hour
- Use plain language
- Content should be ready to paste into Markdown
```

---

### 4. Review the Generated Content

After the LLM generates the lesson, review carefully:

**Accuracy Check**:

- [ ] Are code examples correct and runnable?
- [ ] Are explanations accurate for the topic?
- [ ] Are there any outdated or deprecated concepts?
- [ ] Do prerequisites make sense?

**Structure Check**:

- [ ] All sections present (objectives, intro, concepts, exercises, assessment)?
- [ ] Markdown formatting correct?
- [ ] YAML metadata valid?
- [ ] Learning objectives addressed in content?

**Content Quality Check**:

- [ ] Explanations are clear for target audience?
- [ ] Examples are relevant and useful?
- [ ] Exercises are progressively harder?
- [ ] Assessment checks understanding?

**Completeness Check**:

- [ ] Lesson completable in stated duration?
- [ ] No placeholder text remaining?
- [ ] Links are proper Markdown format?

---

### 5. Common Edits Needed

### After generation, you may need to:

**Fix Code Examples**:
```
❌ Original (may have errors):
def process(data):
    return data.filter(x -> x > 0)

✅ Fixed:
def process(data):
    return [x for x in data if x > 0]
```

**Clarify Explanations**:
```
❌ Too technical:
"Leveraging functional paradigms enables leveraging composition patterns"

✅ Clear:
"Using functions as values lets you combine simpler functions into more complex ones"
```

**Make Examples Runnable**:
```
❌ Pseudo-code:
response = call API

✅ Real code:
import requests
response = requests.get('https://api.example.com/data')
```

**Fix Formatting Issues**:

- Extra blank lines
- Inconsistent indentation
- Wrong heading levels
- Missing code block markers

---

### 6. Add Personal Touch

After LLM generation, consider:

**Add Your Expertise**:

- Correct any topic-specific errors
- Add your own examples if more relevant
- Adjust tone to your style
- Add warnings or tips from experience

**Add Local Context**:

- Link to your organization's standards
- Reference local tools or systems
- Add company-specific examples
- Link to internal resources

**Add Interactivity** (if platform supports):

- Interactive code samples
- Embedded videos
- Discussion questions
- Challenges with hints

---

## Tips for Best Results

### Choose Specific Topics

**Good Topics**:

- "Python List Comprehensions" ✅
- "Building REST APIs with Flask" ✅
- "CSS Grid Layout" ✅
- "Data Cleaning with Pandas" ✅

**Too Broad**:

- "Python" ❌
- "Web Development" ❌
- "JavaScript" ❌

### Be Explicit About Level

**Beginner**:

- No assumptions about prior knowledge
- Explain basic concepts
- Use analogies
- Simple, concrete examples

**Intermediate**:

- Assume basic understanding
- Focus on application
- Include best practices
- Show common patterns

**Advanced**:

- Assume strong foundation
- Deep technical dive
- Discuss edge cases
- Include optimization

### Match Duration to Content

**30 minutes**: 1 concept, 2 simple exercises  
**45 minutes**: 1-2 concepts, 2-3 exercises  
**1 hour**: 2-3 concepts, 2-3 exercises  
**2+ hours**: 4+ concepts, project/capstone

---

## Troubleshooting LLM Output

### Issue: Generated content is too simple
**Solution**: Request "for experienced developers" or "advanced techniques"

### Issue: Code examples don't work
**Solution**: Test them yourself, then provide feedback: "This syntax is wrong for Python 3.9+"

### Issue: Content is too long for the duration
**Solution**: Ask LLM to "focus on core concepts and omit advanced topics"

### Issue: Too many placeholder sections
**Solution**: Regenerate with more specific prompt: "Include specific examples of [X]"

### Issue: Doesn't match your teaching style
**Solution**: This is normal! Edit to match your voice and approach

---

## Example: Full Workflow

### Input
```
Topic: React Hooks for Beginners
Level: Beginner (knows React basics)
Duration: 1 hour
```

### LLM Prompt
```
Create an educational lesson on "React Hooks" for Beginner 
React developers who already know components and state.
The lesson should take approximately 1 hour to complete.

[Full template provided]

Important requirements:

- Explain what Hooks are for beginners
- Include 3-4 practical examples with full code
- Progressive exercises from basic hooks to combining hooks
- Accessible language, explain all technical terms
```

### Review & Edit

1. ✅ Content structure is correct
2. ❌ Code example for useState has syntax error → Fix
3. ❌ Exercise 3 assumes knowledge of useContext → Add context explanation
4. ✅ Metadata is complete
5. ✅ Duration realistic

### Final Result
Publish-ready lesson in ~30 minutes (10 min prompt + 10 min generation + 10 min review/edit)

---

## Quality Checklist for LLM Content

Before submitting any LLM-generated lesson:

### Content Accuracy

- [ ] All code examples are correct
- [ ] Explanations are accurate
- [ ] No deprecated patterns used
- [ ] Links to docs are current

### Completeness

- [ ] All required sections present
- [ ] No placeholder text
- [ ] Learning objectives match content
- [ ] Assessment questions test all objectives

### Clarity

- [ ] Explanations use simple language
- [ ] Examples clearly demonstrate concepts
- [ ] Jargon is explained
- [ ] Content is appropriate for difficulty level

### Structure

- [ ] Markdown is properly formatted
- [ ] YAML metadata is valid
- [ ] File naming follows convention
- [ ] File in correct directory

### Technical

- [ ] Code snippets are syntactically correct
- [ ] Code is runnable (tested if possible)
- [ ] Examples follow best practices
- [ ] No broken links

---

## See Also

- [Lesson Workflow Guide](workflow-create-lesson.md) - Full creation guide
- [Metadata Reference](metadata-reference.md) - Field specifications
- [Lesson Template](../templates/lesson-template.md) - Template structure
- [Quick Start Guide](quick-start.md) - 10-minute overview

---

## Next Steps

1. **Choose your LLM** (ChatGPT, Claude, Gemini, etc.)
2. **Prepare your lesson brief** (topic, level, duration)
3. **Copy the prompt template** from [Workflow Guide](workflow-create-lesson.md#using-the-llm-template)
4. **Generate your lesson** (10-15 minutes)
5. **Review and edit** (10-15 minutes)
6. **Submit as pull request** → Published!

Ready to create your first lesson? 🚀
