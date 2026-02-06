# Contributing to the Lesson Management System

Thank you for your interest in contributing to this personalized lesson repository! We welcome lesson contributions, bug fixes, documentation improvements, and feature ideas from the community.

---

## 🎯 How to Contribute

### 1. Create a Lesson (Most Common)

**For creating and submitting lessons**, see the detailed guide:

👉 **[Lesson Creation Workflow Guide](guides/workflow-create-lesson.md)** ← Start here!

The workflow guide covers:
- Planning your lesson
- Writing or generating content with LLM
- Testing and quality checking
- Submitting via GitHub pull request

**TL;DR**: Copy [lesson template](templates/lesson-template.md) → Write content → Submit PR

### 2. Report Issues or Request Features

- **Found a bug?** → [Open a GitHub Issue](../../issues/new?labels=bug)
- **Want a new feature?** → [Open a GitHub Issue](../../issues/new?labels=enhancement)
- **Have a question?** → [Open a GitHub Discussion](../../discussions/new)

### 3. Improve Documentation

- Spotted a typo or unclear explanation?
- Have a better way to explain a concept?
- Want to add examples or clarifications?

Just submit a pull request with your improvements!

---

## 📋 Submission Checklist

Before submitting your lesson pull request, verify:

### Content Quality
- [ ] Lesson teaches a clear, single concept
- [ ] Learning objectives are specific and achievable
- [ ] Content addresses each learning objective
- [ ] Examples are relevant and clear
- [ ] At least 2-3 exercises included
- [ ] Self-assessment questions included
- [ ] No outdated or deprecated information

### Metadata
- [ ] All required YAML fields present: `title`, `description`, `difficulty`, `duration`, `tags`, `learning_objectives`, `created`
- [ ] Title is 3-100 characters
- [ ] Description is 1 sentence, 10-200 characters
- [ ] `difficulty` is: Beginner, Intermediate, or Advanced
- [ ] `duration` includes number and unit (minutes/hours/days)
- [ ] `tags` are 1-5 items, lowercase, hyphenated
- [ ] `learning_objectives` are 3-5 specific outcomes

### Technical
- [ ] File named: `lesson-[id]-[slug].md`
- [ ] File in correct subject directory: `docs/lessons/[subject]/`
- [ ] Markdown syntax is valid
- [ ] All links work and are properly formatted
- [ ] Code examples are syntactically correct
- [ ] No broken image references

---

## 🚀 Quick Start: Creating Your First Lesson

1. **Read the 10-minute overview**: [Quick Start Guide](guides/quick-start.md)

2. **Choose your approach**:
   - **Manual**: Write your own using the [Lesson Template](templates/lesson-template.md)
   - **AI-Generated**: Use the [LLM Prompt Template](templates/llm-prompt-template.txt) with ChatGPT, Claude, or similar

3. **Save your lesson**:
   - Create file: `docs/lessons/[subject]/lesson-[id]-[slug].md`
   - Example: `docs/lessons/python/lesson-001-variables.md`

4. **Submit via GitHub**:
   - Fork the repository
   - Create a branch: `git checkout -b add-lesson-your-topic`
   - Add your lesson file
   - Commit: `git commit -m "Add lesson: Your Lesson Title"`
   - Push and create a pull request

---

## 📝 Git Workflow

### Setup

```bash
# Fork repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/cours_perso.git
cd cours_perso
git remote add upstream https://github.com/ORIGINAL-OWNER/cours_perso.git
```

### Create a Lesson

```bash
# Create a new branch
git checkout -b add-lesson-your-topic

# Create your lesson in the right location
# Example: docs/lessons/python/lesson-001-variables.md

# Stage and commit
git add docs/lessons/[subject]/lesson-*.md
git commit -m "Add lesson: Your Lesson Title"

# Push to your fork
git push origin add-lesson-your-topic
```

### Submit Pull Request

1. Go to the [original repository](../../)
2. Click "New Pull Request"
3. Select your branch
4. Fill in the PR template (see below)
5. Submit!

---

## 📄 Pull Request Template

When you submit a PR, use this template:

```markdown
## Lesson Information

**Lesson Title**: [Your Lesson Title]
**Subject**: [Python Basics / Web Development / Data Science]
**Difficulty**: [Beginner / Intermediate / Advanced]
**Duration**: [30 minutes / 1 hour / etc.]

## Description

[Brief summary of what the lesson teaches and why it's valuable]

## Checklist

- [ ] Lesson follows template structure
- [ ] Metadata is complete and valid
- [ ] All required sections present
- [ ] Examples are tested and work correctly
- [ ] Exercises are clear and progressive
- [ ] Self-check questions verify learning objectives
- [ ] Markdown syntax is valid
- [ ] Links are working

## Changes

- Added: `docs/lessons/[subject]/lesson-*.md`

## Related Issues

[Reference any related issues, if applicable]
```

---

## 🏷️ Lesson Standards

### Difficulty Levels

**Beginner**: No prior knowledge assumed
- Explain all concepts and terms
- Use simple, concrete examples
- Build from basics
- Include helpful analogies

**Intermediate**: Basic understanding assumed
- Move faster through concepts
- Focus on application
- Show best practices and patterns
- Include some advanced techniques

**Advanced**: Strong foundation required
- Assume significant prior knowledge
- Deep technical dive
- Discuss trade-offs and edge cases
- Include optimization and performance

### Duration Estimates

- **30 minutes**: 1 concept, 2 simple exercises
- **45 minutes**: 1-2 concepts, 2-3 exercises
- **1 hour**: 2-3 concepts, 2-3 exercises
- **1.5-2 hours**: 3-4 concepts, project or capstone

### File Naming

```
lesson-[id]-[slug].md

Examples:
lesson-001-variables.md
lesson-002-functions.md
lesson-003-lists-and-loops.md
lesson-010-async-await.md
```

- **[id]**: Sequential number (3 digits, zero-padded)
- **[slug]**: URL-friendly name (lowercase, hyphens)

---

## 🤖 Using LLM to Generate Content

See [LLM Template Instructions](guides/lesson-template-instructions.md) for:
- How to use ChatGPT, Claude, or other LLMs
- Prompt templates for different topics
- How to review and refine generated content
- Quality checklist for LLM-generated lessons

---

## 💡 Lesson Ideas & Inspiration

**What makes a good lesson?**
- Teaches one clear concept or skill
- Includes practical, working examples
- Provides hands-on exercises
- Tests understanding with assessments
- Connects to real-world use cases
- Follows our template structure

**Need ideas?**
- Teaching a skill from your job?
- Learned something new recently?
- Want to help someone understand a tricky concept?
- Found a great tutorial and want to adapt it?

All are welcome! Submit as an issue to discuss first if unsure.

---

## 🔍 Code Review Process

When you submit a PR:

1. **Automated Checks** (5-10 minutes)
   - GitHub Actions validates Markdown syntax
   - Checks for required metadata fields
   - Verifies file naming and structure
   - Status appears as checkmark or ✗

2. **Maintainer Review** (24-48 hours)
   - Reviewers read your lesson
   - Verify accuracy and quality
   - Check alignment with style
   - May request improvements

3. **Feedback & Iteration**
   - Respond to review comments
   - Make requested changes
   - Push updates to your branch (PR auto-updates)
   - Reviewers re-check

4. **Approval & Merge**
   - Lesson approved and merged
   - GitHub Actions rebuilds and deploys site
   - Your lesson is live! 🎉

---

## 📚 Resources

- [Quick Start Guide](guides/quick-start.md) — 10-minute overview
- [Lesson Creation Workflow](guides/workflow-create-lesson.md) — Detailed step-by-step guide
- [Lesson Template](templates/lesson-template.md) — Template to copy and use
- [LLM Instructions](guides/lesson-template-instructions.md) — How to use AI to generate content
- [Metadata Reference](guides/metadata-reference.md) — Complete field specifications
- [Tagging Guide](guides/tagging-guide.md) — How to tag lessons
- [Tags Reference](guides/tags-reference.md) — Available tags and their usage

---

## ❓ FAQ

### Q: Can I reuse content from my blog or course?

**A**: Yes, if you own it or have permission. Include the source in the author field.
Example: `author: "Adapted from my course on REST APIs"`

### Q: What if I want to create multiple lessons?

**A**: Great! Submit them one at a time or in separate PRs. Each will be reviewed and merged independently.

### Q: Can I use content from other sources?

**A**: Yes, with attribution. Make sure you have rights to use it, and credit the original author.

### Q: What if my lesson is rejected?

**A**: Don't worry! We'll provide clear feedback on what needs to change. Most rejections are minor fixes. Resubmit after making requested changes.

### Q: How long does review take?

**A**: Usually 24-48 hours for initial review. Some lessons need more discussion and may take longer.

### Q: Can I be a regular contributor?

**A**: Absolutely! If you contribute regularly, we can discuss giving you maintainer status for faster merges.

### Q: How do I update a lesson after it's published?

**A**: Submit a new PR with changes. Maintainers review and merge. The site auto-updates.

---

## 📞 Questions?

- **Stuck on something?** → [Open a discussion](../../discussions/new)
- **Found an issue?** → [Report it](../../issues/new)
- **Want to chat?** → Create an issue with label `discussion`

---

## 🙏 Thank You!

Thank you for contributing to the lesson repository! Your work helps others learn and grow. We appreciate your effort in:
- Creating quality educational content
- Making complex topics accessible
- Helping build a learning community
- Supporting others in their educational journey

---

**Ready to create your first lesson?** Start with the [Quick Start Guide](guides/quick-start.md)! 🚀
