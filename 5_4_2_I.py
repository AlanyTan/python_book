list_example=[1,2,"3","four",5.0, ['a', 'b']]
print(f"#1st is {list_example[0]}")
#1st is 1

print(f"#last is {list_example[-1]}")
#last is ['a', 'b']

print(f"#2nd to 4th (inclusive) are {list_example[1:4]}")
#2nd to 4th are [2, '3', 'four']

print(f"#first 3 are {list_example[:3]}")
#first 3 are [1, 2, '3']

print(f"#last 3 are {list_example[-3:]}")
#last 3 are ['four', 5.0, ['a', 'b']]

print(f"#every other items are {list_example[::2]}")
#every other items are [1, '3', 5.0]
