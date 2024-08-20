list_1_alias = list_1 = [1, 2.0, ["3"]]
list_2_alias = list_2 = list('abc')
print(f"# list_1 + list_2 = {list_1 + list_2}")
# list_1 + list_2 = [1, 2.0, ['3'], 'a', 'b', 'c']

print(f"# list_1 *3 = {list_1 * 3} ")
# list_1 *3 = [1, 2.0, ['3'], 1, 2.0, ['3'], 1, 2.0, ['3']]

list_1 += list_2
print(f"# list_1 += list_2 : {list_1}, {list_1 is list_1_alias=}")
# list_1 += list_2 : [1, 2.0, ['3'], 'a', 'b', 'c'], list_1 is list_1_alias=True

list_2 *= 3
print(f"# list_2 *= 3 : {list_2}, {list_2 is list_2_alias=}")
# list_2 *= 3 : ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c'], list_2 is list_2_alias=True
