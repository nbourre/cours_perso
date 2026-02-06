#!/usr/bin/env python3
"""
Fix list spacing in markdown files according to .speckit.yml rules:
- list_spacing: always (blank line before and after lists)
- list_item_spacing: compact (no blank lines between list items)
"""

import re
from pathlib import Path
from typing import List


def is_list_item(line: str) -> bool:
    """Check if a line is a list item (bullet or numbered)."""
    stripped = line.strip()
    # Bullet list: starts with -, *, +
    if re.match(r'^[-*+]\s', stripped):
        return True
    # Numbered list: starts with number followed by . or )
    if re.match(r'^\d+[.)]\s', stripped):
        return True
    # Checkbox list: - [ ] or - [x]
    if re.match(r'^[-*+]\s+\[[ xX]\]\s', stripped):
        return True
    return False


def is_blank_line(line: str) -> bool:
    """Check if a line is blank."""
    return line.strip() == ''


def is_yaml_frontmatter_delimiter(line: str, line_num: int) -> bool:
    """Check if line is YAML frontmatter delimiter (---)."""
    return line.strip() == '---' and line_num < 20


def is_code_fence(line: str) -> bool:
    """Check if line is a code fence."""
    stripped = line.strip()
    return stripped.startswith('```') or stripped.startswith('~~~')


def fix_list_spacing(content: str) -> str:
    """Fix list spacing in markdown content."""
    lines = content.split('\n')
    fixed_lines = []
    in_list = False
    in_yaml = False
    in_code_block = False
    yaml_delimiters = 0
    
    for i, line in enumerate(lines):
        # Track YAML frontmatter
        if is_yaml_frontmatter_delimiter(line, i):
            yaml_delimiters += 1
            if yaml_delimiters <= 2:
                in_yaml = yaml_delimiters == 1
        
        # Track code blocks
        if is_code_fence(line):
            in_code_block = not in_code_block
        
        # Skip processing inside YAML frontmatter or code blocks
        if in_yaml or in_code_block:
            fixed_lines.append(line)
            continue
        
        is_current_list_item = is_list_item(line)
        
        # Starting a new list
        if is_current_list_item and not in_list:
            # Ensure blank line before list (unless at start or after blank line)
            if fixed_lines and not is_blank_line(fixed_lines[-1]):
                # Don't add blank line after YAML frontmatter end
                if not (fixed_lines[-1].strip() == '---' and yaml_delimiters == 2):
                    fixed_lines.append('')
            in_list = True
            fixed_lines.append(line)
        
        # Continuing a list
        elif is_current_list_item and in_list:
            # Remove blank lines between list items (compact spacing)
            if fixed_lines and is_blank_line(fixed_lines[-1]):
                # Keep the blank line if previous was also blank (preserve intentional spacing)
                if len(fixed_lines) >= 2 and not is_blank_line(fixed_lines[-2]):
                    fixed_lines.pop()  # Remove the blank line
            fixed_lines.append(line)
        
        # Ending a list
        elif not is_current_list_item and in_list:
            in_list = False
            # Ensure blank line after list (unless next line is blank or we're at end)
            if not is_blank_line(line):
                fixed_lines.append('')
            fixed_lines.append(line)
        
        # Not in a list
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def process_file(file_path: Path) -> bool:
    """Process a single markdown file. Returns True if file was modified."""
    try:
        content = file_path.read_text(encoding='utf-8')
        fixed_content = fix_list_spacing(content)
        
        if content != fixed_content:
            file_path.write_text(fixed_content, encoding='utf-8')
            return True
        return False
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """Main function to process all markdown files."""
    docs_dir = Path(__file__).parent.parent.parent / 'docs'
    
    if not docs_dir.exists():
        print(f"Error: docs directory not found at {docs_dir}")
        return
    
    # Find all markdown files
    md_files = list(docs_dir.rglob('*.md'))
    
    print(f"Found {len(md_files)} markdown files")
    print("Processing files...\n")
    
    modified_files = []
    
    for md_file in sorted(md_files):
        if process_file(md_file):
            rel_path = md_file.relative_to(docs_dir.parent)
            modified_files.append(str(rel_path))
            print(f"✓ Fixed: {rel_path}")
        else:
            rel_path = md_file.relative_to(docs_dir.parent)
            print(f"  Skip:  {rel_path} (no changes needed)")
    
    print(f"\n{'='*60}")
    print(f"Summary: Modified {len(modified_files)} of {len(md_files)} files")
    
    if modified_files:
        print("\nModified files:")
        for f in modified_files:
            print(f"  - {f}")


if __name__ == '__main__':
    main()
