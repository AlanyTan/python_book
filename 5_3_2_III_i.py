list_sub = ['a', 'b', 'c']
list_alias = list_example = [1, 2.0, "3", "four", list_sub]

list_example[0] = "10"
print(f"# {list_alias=}")
# list_alias=['10', 2.0, '3', 'four', ['a', 'b', 'c']]

list_example[1:3] = ["two & III"]
print(f"# {list_alias=}")
# list_alias=['10', 'two & III', 'four', ['a', 'b', 'c']]

list_sub[-1] = ['y', 'z']
print(f"# {list_alias=}")
# list_alias=['10', 'two & III', 'four', ['a', 'b', ['y', 'z']]]

list_example[-1][-1][-1:] = []
print(f"# {list_alias=}")
# list_alias=['10', 'two & III', 'four', ['a', 'b', ['y']]]
print(f"# {list_sub=}")
# list_sub=['a', 'b', ['y']]

list_example[-1] = [1, 2]
print(f"# {list_alias=}")
# list_alias=['10', 'two & III', 'four', [1, 2]]
print(f"# {list_sub=}")
# list_sub=['a', 'b', ['y']]

list_example[len(list_example):] = ['additional', 'items']
print(f"# {list_alias=}")
# list_alias=['10', 'two & III', 'four', [1, 2], 'additional', 'items']

list_alias[1:6:2] = ['B', 'D', 'F']
print(f"# {list_example=}")
# list_example=['10', 'B', 'four', 'D', 'additional', 'F']
