#!/usr/bin/env python3
"""Debug version of fix_list_spacing to see what'shappening."""

import re
from pathlib import Path


def is_list_item(line: str) -> bool:
    """Check if a line is a list item (bullet or numbered)."""
    stripped = line.strip()
    if re.match(r'^[-*+]\s', stripped):
        return True
    if re.match(r'^\d+[.)]\s', stripped):
        return True
    if re.match(r'^[-*+]\s+\[[ xX]\]\s', stripped):
        return True
    return False


def is_blank_line(line: str) -> bool:
    """Check if a line is blank."""
    return line.strip() == ''


# Read file
file_path = Path('docs/guides/troubleshooting-fr.md')
content = file_path.read_text(encoding='utf-8')

# Normalize line endings
content = content.replace('\r\n', '\n').replace('\r', '\n')
lines = content.split('\n')

# Find the first Solutions section
for i, line in enumerate(lines):
    if '**Solutions**:' in line:
        print(f"\nFound Solutions at line {i}")
        print(f"Line {i}: {repr(line)}")
        print(f"Line {i+1}: {repr(lines[i+1])}")
        
        # Check what the script would do
        is_list = is_list_item(lines[i+1])
        is_blank = is_blank_line(lines[i])
        
        print(f"\nLine {i} is_blank: {is_blank}")
        print(f"Line {i+1} is_list_item: {is_list}")
        
        # This should trigger adding a blank line
        print(f"\nShould add blank line before line {i+1}: {is_list and not is_blank}")
        break
