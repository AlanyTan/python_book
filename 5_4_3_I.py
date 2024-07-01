tuple_example=(1, [2, 2.0], "3", "four", 5.0, (6,'six'))
print(f"#1st is {tuple_example[0]}")
#1st is 1

print(f"#2nd to 4th (inclusive) are {tuple_example[1:4]}")
#2nd to 4th (inclusive) are ([2, 2.0], '3', 'four')

print(f"#first 3 are {tuple_example[:3]}")
#first 3 are (1, [2, 2.0], '3')

print(f"#last 3 are {tuple_example[-3:]}")
#last 3 are ('four', 5.0, (6, 'six'))

print(f"#every other items are {tuple_example[::2]}")
#every other items are (1, '3', 5.0)

print(f"#list in tuple is mutable: {tuple_example[1].pop()=}")
#list in tuple is mutable: tuple_example[1].pop()=2.0

print(f"#after pop: {tuple_example=}")
#after pop: tuple_example=(1, [2], '3', 'four', 5.0, (6, 'six'))
