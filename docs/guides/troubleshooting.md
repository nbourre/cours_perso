# Troubleshooting Guide

Common issues and solutions when creating and contributing lessons.

---

## 🛠️ Content & Writing Issues

### My lesson is too long

**Problem**: Lesson takes longer than intended or covers too many concepts.

**Solutions**:
- **Split into multiple lessons**: Break complex topics into separate, focused lessons
- **Focus on one core concept**: Each lesson should teach 1-2 main ideas
- **Move advanced content**: Save optional deep-dives for "Further Reading" section
- **Reduce examples**: Keep 3-4 best examples, remove redundant ones
- **Simplify exercises**: Focus on essential practice, not exhaustive coverage

**Duration Guidelines**:
- 30 min: 1 concept, 2 simple exercises
- 45 min: 1-2 concepts, 2-3 exercises
- 1 hour: 2-3 concepts, 3-4 exercises
- 1.5-2 hours: 3-4 concepts + project

### My lesson examples don't work

**Problem**: Code examples have errors or don't run.

**Solutions**:
- **Test every code example**: Run it yourself before submitting
- **Verify dependencies**: Are required libraries installed?
- **Check syntax carefully**: Python indentation, JavaScript semicolons, etc.
- **Add setup instructions**: If special setup needed, explain it
- **Provide expected output**: Show what successful code should output
- **Include error explanations**: If showing errors, explain them

**For Python**: Test in interactive shell (Python REPL or Jupyter)
**For JavaScript**: Test in browser console or Node.js
**For HTML/CSS**: Test in a browser

### Exercises are confusing

**Problem**: Students don't understand what exercises are asking.

**Solutions**:
- **Clear instructions**: Start each exercise with "Write a function that..." or "Create a program that..."
- **Specify input/output**: Show example inputs and expected outputs
- **Add hints**: For difficult exercises, provide hints after exercises
- **Progressive difficulty**: Easy → Medium → Hard
- **Include solutions**: Provide solutions/answers (in separate section)

### I'm using outdated information

**Problem**: Lesson references old versions or deprecated features.

**Solutions**:
- **Check version numbers**: Verify all library/framework versions are current
- **Search for deprecations**: Look for "[feature] deprecated" on documentation
- **Test on current version**: Ensure examples work with latest release
- **Add version notes**: If version-specific, specify it: "Python 3.10+"
- **Include migration notes**: For deprecated features, suggest alternatives

---

## 📝 Metadata & Structure Issues

### My YAML frontmatter has errors

**Problem**: Metadata validation fails or MkDocs won't build.

**Common errors**:
- **Colons in titles**: Wrap in quotes: `title: "Python: Functions & Organization"`
- **List syntax**: Use proper YAML list format:
  ```yaml
  tags:
    - python
    - functions
    - basics
  ```
- **Boolean values**: Use `true`/`false` not `True`/`False`
- **Escaped characters**: Use quotes if special characters: `description: "What's a variable?"`

**Solutions**:
- **Validate YAML**: Use online YAML validator (yamllint.com)
- **Check quotes**: Single/double quotes must be balanced
- **Verify indentation**: YAML is space-sensitive (use 2-space indentation)
- **Test locally**: Build MkDocs: `mkdocs serve`

### Missing required fields

**Problem**: Lesson missing metadata fields like `difficulty` or `learning_objectives`.

**Required fields** (all must be present):
- `title`: Lesson name
- `description`: 1-sentence summary
- `difficulty`: Beginner / Intermediate / Advanced
- `duration`: Time estimate with unit (30 minutes, 1 hour, etc.)
- `tags`: 1-5 topic tags
- `learning_objectives`: 3-5 specific outcomes
- `created`: Date created (YYYY-MM-DD)

**Solution**: Copy the [lesson template](../templates/lesson-template.md) and fill in all fields.

### Tags are inconsistent

**Problem**: Tags don't match existing tags or are formatted wrong.

**Solutions**:
- **Use lowercase**: `python` not `Python`
- **Use hyphens**: `machine-learning` not `machine_learning`
- **Check existing tags**: See [Tags Reference](tags-reference.md)
- **Be specific**: `web-development` better than `web`
- **Limit to 5**: Don't over-tag

**Available tags**: See [Tags Reference](tags-reference.md) for complete list and usage.

---

## 🔧 Technical Issues

### My lesson file isn't showing up on the site

**Problem**: File created but lesson doesn't appear after build.

**Checklist**:
- [ ] File is in correct location: `docs/lessons/[subject]/lesson-*.md`
- [ ] File name matches pattern: `lesson-NNN-slug.md`
- [ ] File has required frontmatter (YAML at top)
- [ ] MkDocs config includes this subject in navigation
- [ ] Build completed successfully: No errors in build output
- [ ] Site cache cleared: Hard refresh (Ctrl+Shift+R)

**Solutions**:
- **Check file path**: Ensure subject directory exists
- **Check frontmatter**: Verify YAML is valid (see YAML issues above)
- **Rebuild site**: Delete `site/` folder, run `mkdocs build`
- **Check navigation**: Verify `mkdocs.yml` includes your subject

### Links in my lesson are broken

**Problem**: Links in lesson don't work or appear as red links.

**Solutions**:
- **Verify link paths**: Links must be relative to `docs/` directory
- **Use correct syntax**: `[text](path/to/file.md)` for internal links
- **Test each link**: Click them to verify they work
- **Check file names**: Spelling, case, extensions must match exactly
- **Use absolute paths**: From `docs/` root, not current folder

**Examples**:
```markdown
# Correct - from docs/ root
[template](templates/lesson-template.md)
[guide](guides/quick-start.md)

# Incorrect - won't work
[template](./lesson-template.md)
[guide](../docs/guides/quick-start.md)
```

### Markdown formatting looks wrong

**Problem**: Formatting renders incorrectly (bold not working, lists broken, etc.).

**Common issues**:
- **Bold**: Use `**text**` or `__text__`, not `*text*`
- **Lists**: Must have blank line before first item
- **Code blocks**: Use triple backticks with language: ` ```python `
- **Quotes**: Use `>` for blockquotes
- **Escaping**: Use `\` to escape special characters: `\*not bold\*`

**Solutions**:
- **Test locally**: Build with `mkdocs serve` and check in browser
- **Compare with examples**: Look at working lessons in same subject
- **Use validator**: Online Markdown validator
- **Check spacing**: YAML, lists, and code blocks need proper spacing

### Images aren't displaying

**Problem**: Images in lesson aren't showing up.

**Solutions**:
- **Use correct path**: `![alt text](../../assets/image.png)`
- **Check relative paths**: Count `../` levels correctly
- **Verify file exists**: Image file actually in `docs/assets/`
- **Use supported formats**: PNG, JPG, SVG, GIF
- **Add alt text**: `![description of image](path)`

**Best practice**: Store images in `docs/assets/images/` organized by subject

---

## 🔄 Git & GitHub Issues

### I can't push my changes

**Problem**: Git push fails.

**Solutions**:
- **Check remote**: `git remote -v` (should show your fork)
- **Pull first**: `git pull origin main` before push
- **Check branch**: `git branch` (should show your branch)
- **Force if needed**: `git push -f origin your-branch-name`

**Preventive**: Always pull before pushing to avoid conflicts.

### My PR has merge conflicts

**Problem**: Pull request shows conflicts with main branch.

**Solutions** (in order of preference):
1. **Rebase on main**: 
   ```bash
   git fetch upstream
   git rebase upstream/main
   git push -f origin your-branch-name
   ```

2. **Merge main into your branch**:
   ```bash
   git fetch upstream
   git merge upstream/main
   git push origin your-branch-name
   ```

3. **Resolve manually**: Fix conflicts in your editor, commit, push

**Prevention**: Keep branch up-to-date, sync with main before submitting

### My branch is behind main

**Problem**: Branch is outdated compared to main.

**Solutions**:
```bash
# Update your local main
git fetch upstream
git checkout main
git merge upstream/main

# Rebase your branch
git checkout your-branch
git rebase main
git push -f origin your-branch
```

---

## 📚 LLM Generation Issues

### LLM generated content is too technical

**Problem**: ChatGPT/Claude content uses terminology above target difficulty.

**Solutions**:
- **Regenerate with better prompt**: Specify "Beginner" and "use simple language"
- **Rewrite sections**: Use your own simpler explanations
- **Add definitions**: Define technical terms when first introduced
- **Use analogies**: Explain complex ideas with everyday comparisons
- **Simplify examples**: Replace advanced examples with beginner-friendly ones

### LLM examples don't work

**Problem**: Code from ChatGPT/Claude has errors.

**Solutions**:
- **Test every example**: Run it before submitting
- **Verify versions**: Make sure code works with specified versions
- **Ask LLM to fix**: Paste error and ask for corrected version
- **Test in IDE**: Use proper IDE to catch errors early
- **Update dependencies**: Code may need newer libraries

### Content is too generic

**Problem**: Generated content doesn't match your course style.

**Solutions**:
- **Customize heavily**: Add your own examples and context
- **Replace generic sections**: Keep structure, personalize content
- **Add local references**: Reference your specific course/community
- **Include your insights**: Mix AI content with your expertise
- **Verify accuracy**: Make sure examples match your context

See [LLM Instructions](lesson-template-instructions.md) for better prompting techniques.

---

## 📊 Quality & Review Issues

### My lesson was rejected

**Problem**: PR was closed or asked for changes.

**Common reasons**:
- **Incomplete metadata**: Missing or incorrect YAML fields
- **Content quality**: Unclear writing, inaccurate info, or broken examples
- **Style mismatch**: Doesn't follow template or existing lessons
- **Outdated info**: References old versions or deprecated features
- **Insufficient testing**: Examples or exercises don't work

**Solutions**:
- **Read feedback**: Review reviewer comments carefully
- **Address all points**: Make requested changes
- **Resubmit as new PR**: After making fixes
- **Ask for clarification**: If feedback unclear, comment on PR or issue

### My lesson was merged but has issues

**Problem**: Lesson live but contains errors or needs updates.

**Solutions**:
- **Submit a new PR**: Fix issues in a new pull request
- **File an issue**: Report problems for others to fix
- **Quick fixes**: For typos, small issues, you can edit directly

---

## 🆘 Getting Help

**Can't find your issue?**

1. **Check existing issues**: Search GitHub issues for similar problems
2. **Ask in discussions**: Start a GitHub discussion for help
3. **Comment on relevant issues**: Your question might help others
4. **Check template docs**: See [Lesson Template Instructions](lesson-template-instructions.md)

**Still stuck?**

- **Create a minimal example**: Share just the code/content that's broken
- **Provide error messages**: Copy full error text
- **Describe what you tried**: Helps reviewers assist better
- **Include file paths**: Specify exactly what you're working on

---

## ✅ Quick Checklist Before Submitting

Before pushing your PR, verify:

- [ ] All YAML fields present and valid
- [ ] Code examples tested and working
- [ ] Exercises include clear instructions
- [ ] At least one self-check question included
- [ ] File in correct directory
- [ ] File named correctly: `lesson-NNN-slug.md`
- [ ] Markdown syntax valid (bold, lists, code blocks)
- [ ] All links tested and working
- [ ] No typos or formatting issues
- [ ] Follows template structure
- [ ] Reviewed [Quick Start Guide](quick-start.md)

**Ready?** Submit your PR! 🚀

---

## 📞 Need More Help?

- **Lessons Questions**: See [Lesson Creation Workflow](workflow-create-lesson.md)
- **Metadata Reference**: See [Metadata Reference](metadata-reference.md)
- **Tagging Help**: See [Tagging Guide](tagging-guide.md)
- **Contributing Process**: See [CONTRIBUTING.md](../CONTRIBUTING.md)
- **Quick Start**: See [Quick Start Guide](quick-start.md)

**Happy creating!** 📚✨
