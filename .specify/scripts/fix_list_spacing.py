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


def is_sublist_item(line: str) -> bool:
    """Check if a line is an indented sublist item (4+ spaces before list marker)."""
    # Must have at least 4 spaces of indentation before list marker
    if re.match(r'^\s{4,}[-*+]\s', line):
        return True
    if re.match(r'^\s{4,}\d+[.)]\s', line):
        return True
    if re.match(r'^\s{4,}[-*+]\s+\[[ xX]\]\s', line):
        return True
    return False


def get_indent_level(line: str) -> int:
    """Get the indentation level of a line (number of leading spaces)."""
    return len(line) - len(line.lstrip())


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
    """Fix list spacing in markdown content according to .speckit.yml rules:
    - list_spacing: always (blank line before and after lists)
    - list_item_spacing: compact (no blank lines between items)
    - sublist_spacing:
        before: always (blank line before sublist)
        between: compact (no blank lines between sublist items)
        after: always (blank line after sublist)
    """
    # Normalize line endings to Unix style for consistent processing
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    lines = content.split('\n')
    fixed_lines = []
    in_list = False
    in_sublist = False
    in_yaml = False
    in_code_block = False
    yaml_delimiters = 0
    list_base_indent = 0  # Track the base indentation of current list
    pending_blank_lines = []  # Track blank lines we might need to remove
    
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
            # Flush any pending blank lines first
            fixed_lines.extend(pending_blank_lines)
            pending_blank_lines = []
            fixed_lines.append(line)
            continue
        
        is_current_list_item = is_list_item(line)
        is_current_sublist_item = is_sublist_item(line)
        current_indent = get_indent_level(line)
        is_blank = is_blank_line(line)
        
        # Handle blank lines specially - we might keep or remove them
        if is_blank:
            if in_list or in_sublist:
                # Don't add blank immediately - wait to see what comes next
                pending_blank_lines.append(line)
            else:
                # Not in a list, keep blank lines as-is
                fixed_lines.append(line)
            continue
        
        # Non-blank line processing
        
        # Starting a new list (parent level only)
        if is_current_list_item and not in_list:
            # Clear any pending blank lines first
            pending_blank_lines = []
            
            # Ensure blank line before list (list_spacing: always)
            if fixed_lines:
                last_line = fixed_lines[-1]
                last_line_is_blank = is_blank_line(last_line)
                
                # Don't add blank line after YAML frontmatter end or if already blank
                if not last_line_is_blank:
                    is_yaml_end = last_line.strip() == '---' and yaml_delimiters == 2
                    if not is_yaml_end:
                        fixed_lines.append('')
            
            in_list = True
            in_sublist = False
            list_base_indent = current_indent
            fixed_lines.append(line)
        
        # Parent list item while in list
        elif is_current_list_item and in_list and not in_sublist:
            # We know pending_blank_lines should be removed (they're between parent items)
            pending_blank_lines = []
            fixed_lines.append(line)
        
        # Transition to sublist
        elif is_current_sublist_item and in_list and not in_sublist:
            # Add a blank line BEFORE the sublist starts (sublist_spacing: before: always)
            if not is_blank_line(fixed_lines[-1] if fixed_lines else ''):
                fixed_lines.append('')
            # Clear pending blanks
            pending_blank_lines = []
            in_sublist = True
            fixed_lines.append(line)
        
        # Continue in sublist
        elif is_current_sublist_item and in_list and in_sublist:
            # Remove pending blank lines between sublist items (compact spacing)
            pending_blank_lines = []
            fixed_lines.append(line)
        
        # End of sublist, back to parent level
        elif not is_current_sublist_item and in_list and in_sublist:
            if is_current_list_item:
                # Next parent item - add blank line AFTER sublist
                if fixed_lines and not is_blank_line(fixed_lines[-1]):
                    fixed_lines.append('')
                in_sublist = False
                pending_blank_lines = []
                fixed_lines.append(line)
            else:
                # Continuation text or other content - check indent
                if current_indent > list_base_indent:
                    # Still part of sublist area, keep it
                    pending_blank_lines = []
                    fixed_lines.append(line)
                else:
                    # Ending the entire list
                    in_list = False
                    in_sublist = False
                    list_base_indent = 0
                    # Add blank line after list
                    if fixed_lines and not is_blank_line(fixed_lines[-1]):
                        fixed_lines.append('')
                    pending_blank_lines = []
                    fixed_lines.append(line)
        
        # Non-list content while in a list (no sublist)
        elif in_list and not in_sublist:
            # Check if this is continuation text (indented under a list item)
            if current_indent > list_base_indent:
                # This is continuation text
                pending_blank_lines = []
                fixed_lines.append(line)
            else:
                # Not continuation - we're ending the list
                in_list = False
                list_base_indent = 0
                # Add blank line after list, then the current line
                if fixed_lines and not is_blank_line(fixed_lines[-1]):
                    fixed_lines.append('')
                # Clear pending blanks (we just ended the list)
                pending_blank_lines = []
                fixed_lines.append(line)
        
        # Not in a list
        else:
            # Add any pending blank lines first
            fixed_lines.extend(pending_blank_lines)
            pending_blank_lines = []
            fixed_lines.append(line)
    
    # Don't forget any pending blank lines at the end
    fixed_lines.extend(pending_blank_lines)
    
    return '\n'.join(fixed_lines)


def process_file(file_path: Path) -> bool:
    """Process a single markdown file. Returns True if file was modified."""
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Detect original line ending style
        has_crlf = '\r\n' in content
        
        fixed_content = fix_list_spacing(content)
        
        # Restore original line ending style
        if has_crlf:
            fixed_content = fixed_content.replace('\n', '\r\n')
        
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
