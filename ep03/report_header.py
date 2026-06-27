"""
Python from Zero — EP03: Strings & String Methods
Mini Project: Report Header Generator

Demonstrates:
- .strip()
- .title()
- .center()
- len()
- slicing
"""

raw_title = "   quarterly sales report   "

clean_title = raw_title.strip().title()
header = clean_title.center(40, "=")

print(header)
print(f"Length: {len(clean_title)} characters")
print(f"Short code: {clean_title[:9]}")
