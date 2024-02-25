def counter():
    print(f"# first yield.")
    yield 1
    print(f"# second yield.")
    yield 2
    print(f"# third yield.")
    yield 3

seq_nos = counter()
print(f"#seq_nos is a {type(seq_nos)}")

for seq_no in seq_nos:
    print(f"#main received:{seq_no}")
    
#seq_nos is a <class 'generator'>
# first yield.
#main received:1
# second yield.
#main received:2
# third yield.
#main received:3
