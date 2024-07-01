expression_string="x/(12*x^(2+y)+x)"
open_parenthesis=[]
pos = 0
for char in expression_string:
    if char == '(':
        open_parenthesis.append(pos)
    elif char == ')':
        matching_open_pos = open_parenthesis.pop()
        print (f"# found matching () {matching_open_pos} and {pos}")
    pos+=1

if open_parenthesis:
    print(f"# Error: some open ( were not closed: {open_parenthesis}") 
# found matching () 8 and 12
# found matching () 2 and 15
