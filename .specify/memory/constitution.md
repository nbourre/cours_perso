<!-- 
## Sync Impact Report

**Version Change**: 0.0.0 → 1.0.0 (MAJOR)

**Rationale**: Initial constitution for LLM-generated personalized courses documentation repository. Core principles established for maintainability, ease of user updates, and automation.

**Modified Principles**: N/A (initial version)

**Added Sections**: 
- Core Principles (5 principles)
- Documentation Standards
- Automation & Deployment

**Removed Sections**: N/A

**Templates Status**:
- ✅ plan-template.md: Aligns with Markdown-first principle
- ✅ spec-template.md: Aligns with user story and clarity requirements
- ✅ tasks-template.md: Aligns with structured workflow principle
- ✅ README.md: Updated with workflow description

**Follow-up TODOs**: None
-->

# Personalized Courses Documentation Constitution

## Core Principles

### I. Markdown-First Documentation
All course content MUST be written in Markdown format to ensure ease of editing and portability. Documentation files must be self-contained, clearly structured, and human-readable. No binary or proprietary formats are permitted in course content. MkDocs is the standard format for organization and site generation.

**Rationale**: Markdown ensures accessibility for non-technical users, version control compatibility, and platform independence. MkDocs provides a lightweight, maintainable documentation structure without proprietary vendor lock-in.

### II. Open Source Dependencies Only
Every dependency, tool, and service MUST be open source with clear licensing. No proprietary or closed-source technologies are permitted. This ensures sustainability, transparency, and cost-free access for all users.

**Rationale**: Open source dependencies prevent vendor lock-in, allow community contribution, and ensure the project remains freely accessible and modifiable for educational purposes.

### III. User-Friendly Content Updates
The workflow for updating course content must be simple enough for non-technical users. Changes to Markdown files trigger automated deployment. No complex build steps or specialized tools are required of content editors.

**Rationale**: Lowering the barrier to content updates enables wider participation and faster iteration. Automated GitHub Actions workflows eliminate manual deployment steps, reducing errors and improving time-to-publication.

### IV. Automated Deployment via GitHub Actions
Every push to the repository MUST trigger a GitHub Action that automatically updates the GitHub Pages site. Deployment MUST be fast, reliable, and logged for transparency. No manual deployment steps are permitted.

**Rationale**: Automation removes human error, ensures consistency, and provides immediate feedback on deployment status. GitHub Actions provides cost-free, native CI/CD integration without external service dependencies.

### V. Structural Consistency & Clarity
All course documentation MUST follow a consistent structure defined in the MkDocs configuration. Course pages must have clear titles, logical sections, and navigation metadata. No orphaned or undocumented pages are permitted.

**Rationale**: Consistent structure improves user experience, makes content maintainable, and enables automated validation of documentation integrity.

## Documentation Standards

- Course content must use Markdown with `.md` extension
- Each course must include: overview, learning objectives, modules, and assessment guidance
- File naming must use lowercase with hyphens (e.g., `advanced-python-concepts.md`)
- Navigation structure must be defined in `mkdocs.yml`
- All external links must be valid and current (checked prior to deployment)

## Automation & Deployment

- GitHub Actions workflow triggers on every push to main/master branch
- Workflow builds MkDocs site and deploys to GitHub Pages
- Deployment status must be visible in repository (via badge or Actions tab)
- Failed deployments must halt publication and alert maintainers
- Build logs must be retained for debugging and audit purposes

## Governance

This constitution supersedes all prior practices. All contributions MUST comply with these five core principles and the documentation standards outlined above.

**Amendment Process**: Changes to the constitution require:
1. Documentation of the proposed amendment and rationale
2. Review and approval by project maintainers
3. Migration plan if existing content is affected
4. Version bump reflecting the scope of change (MAJOR/MINOR/PATCH)

**Compliance Review**: 
- Quarterly review of documentation structure and publishing workflow
- Annual assessment of tool versions and dependency updates
- PRs must verify compliance with Principles I–V before merge

**Version**: 1.0.0 | **Ratified**: 2026-01-30 | **Last Amended**: 2026-01-30
