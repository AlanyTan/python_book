expression_string = "x/(12*x^(2+y)+x)"
open_parenthesis = []
for idx, char in enumerate(expression_string):
    if char == '(':
        open_parenthesis.append(idx)
    elif char == ')':
        matching_open_pos = open_parenthesis.pop()
        print(f"# found matching () {matching_open_pos} and {idx}")

if open_parenthesis:
    print(f"# Error: some open ( were not closed: {open_parenthesis}")
# found matching () 8 and 12
# found matching () 2 and 15
