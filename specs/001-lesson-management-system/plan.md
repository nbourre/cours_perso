# Implementation Plan: Lesson Management System with LLM Template Support

**Branch**: `001-lesson-management-system` | **Date**: 2026-01-30 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/001-lesson-management-system/spec.md`

**Note**: This plan focuses on integrating lesson management features into the existing MkDocs documentation platform.

## Summary

Build a comprehensive lesson management and discovery system for MkDocs that enables users to organize, search, and create personalized LLM-generated courses. The system will organize lessons by subject, support tag-based discovery across subjects, provide clear lesson creation workflow documentation, and include reusable LLM prompt templates to accelerate content generation. All lessons are stored as Markdown files with consistent metadata (YAML frontmatter), built and deployed via GitHub Actions to GitHub Pages.

**Primary Requirements**:
- Subject-based lesson organization with homepage navigation
- Tag-based cross-subject search and filtering
- Lesson creation workflow documentation with LLM template
- Metadata support (title, description, difficulty, duration, tags)
- Automatic GitHub Actions deployment on changes

## Technical Context

**Language/Version**: Markdown content + YAML frontmatter (platform-agnostic)  
**Primary Dependencies**: MkDocs (open source), Material theme, pymdownx extensions (admonition, superfences, highlight, arithmatex, snippets, attr_list, md_in_html), MathJax for LaTeX, GitHub Pages, GitHub Actions  
**Storage**: Markdown files in git repository (file-based, version-controlled). See [data-model.md](data-model.md) for detailed directory structure: `docs/lessons/[subject]/lesson-[id]-[slug].md`  
**Testing**: GitHub Actions workflow validation (lint, build, deploy checks)  
**Target Platform**: Web (GitHub Pages, browser-based documentation site)
**Project Type**: Documentation site (static content generation with MkDocs)  
**Performance Goals**: Build and deploy site in <60 seconds; search/filter instantaneous (client-side); page load <2 seconds  
**Constraints**: File-based storage only; no database; no backend API (search is client-side via MkDocs plugins); no real-time notifications  
**Scale/Scope**: 10-100 lessons per subject, 5-10 subjects, ~50-100 tags total; support 10+ new lessons created monthly via LLM template

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Principle I: Markdown-First Documentation
✅ **PASS** - All lessons stored as Markdown (.md) files, no binary formats; MkDocs provides the documentation platform

### Principle II: Open Source Dependencies Only
✅ **PASS** - MkDocs (open source), Material theme (MIT license), all pymdownx extensions (open source), GitHub Actions (built-in, no cost), no proprietary tools required

### Principle III: User-Friendly Content Updates
✅ **PASS** - Users edit Markdown files directly; GitHub Actions handles build/deploy automatically; lesson creation workflow documented with templates; no complex build steps required

### Principle IV: Automated Deployment via GitHub Actions
✅ **PASS** - GitHub Actions workflow triggered on push to main branch; workflow builds MkDocs site and deploys to GitHub Pages; deployment status visible in Actions tab; build logs retained

### Principle V: Structural Consistency & Clarity
✅ **PASS** - MkDocs nav configuration enforces consistent structure; lesson template defines consistent Markdown structure; YAML frontmatter provides metadata; no orphaned pages (nav.yml controls all visibility)

**Overall Status**: ✅ **All 5 principles PASS** - No violations; feature aligns with constitution

## Project Structure

### Documentation (this feature)

```text
specs/001-lesson-management-system/
├── plan.md              # This file
├── spec.md              # Feature specification
├── research.md          # Phase 0 research findings (generated during planning)
├── data-model.md        # Phase 1 data model and lesson structure
├── quickstart.md        # Phase 1 quick start guide for users
├── contracts/           # Phase 1 interface contracts
│   ├── lesson-template.md     # Standard lesson Markdown template
│   ├── metadata-spec.md       # YAML frontmatter specification
│   └── workflow-guide.md      # Lesson creation workflow document
└── checklists/
    └── requirements.md   # Quality checklist (completed: 16/16 pass)
```

### Source Code (Repository root - Content Structure)

```text
docs/                                    # MkDocs root documentation directory
├── mkdocs.yml                          # MkDocs configuration (updated with lesson nav)
├── index.md                            # Homepage (updated with subject index)
├── lessons/                            # Main lessons directory
│   ├── python/                         # Subject: Python Basics
│   │   ├── index.md                    # Subject index (lesson listing page)
│   │   ├── lesson-001-intro.md         # Individual lesson (with metadata)
│   │   ├── lesson-002-functions.md
│   │   └── ...
│   ├── web-development/                # Subject: Web Development
│   │   ├── index.md
│   │   ├── lesson-001-html-basics.md
│   │   └── ...
│   ├── data-science/                   # Subject: Data Science
│   │   ├── index.md
│   │   └── ...
│   └── [additional subjects]/
├── guides/                             # User guides and documentation
│   ├── workflow-create-lesson.md       # ⭐ Lesson creation workflow (linked from main README)
│   ├── lesson-template-instructions.md # How to use the LLM template
│   └── tagging-guide.md                # How to add tags and metadata
├── templates/                          # Reusable templates
│   ├── lesson-template.md              # Standard lesson Markdown template
│   └── llm-prompt-template.txt         # LLM prompt template for content generation
├── stylesheets/
│   └── extra.css                       # Custom CSS (existing)
└── README.md                           # Root README (github display, links to workflow)

.github/
└── workflows/
    └── deploy-docs.yml                 # GitHub Actions workflow for MkDocs build/deploy
```

**Structure Decision**: 
- Lesson content organized into subject directories under `docs/lessons/[subject]/`
- Each subject has an `index.md` listing all lessons in that subject (addresses FR-002, FR-003)
- Lesson creation workflow prominently linked from main README and available in `docs/guides/workflow-create-lesson.md` (addresses FR-008)
- Lesson template and LLM prompt template stored in `docs/templates/` for easy discovery (addresses FR-006)
- `mkdocs.yml` nav configuration updated to reflect subject hierarchy (addresses FR-010)
- All lessons use consistent YAML frontmatter for metadata (addresses FR-009)
- GitHub Actions workflow validates and deploys on commit (addresses FR-012)
