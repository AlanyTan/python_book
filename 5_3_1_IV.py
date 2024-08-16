list_1 = [1, [2], '3', 4]
list_1_alias = list_1
list_2 = list('abc')
list_3 = [list_1, list_2, list_1_alias]

print(f"# {list_3=}")
# list_3=[[1, [2], '3', 4], ['a', 'b', 'c'], [1, [2], '3', 4]]

list_1.append("Z")
print(f"# {list_3=}")
# list_3=[[1, [2], '3', 4, 'Z'], ['a', 'b', 'c'], [1, [2], '3', 4, 'Z']]

list_2 = ["a", "different", "list"]
print(f"# {list_1=}, {list_1_alias=}\n# {list_2=},\n# {list_3=}")
# list_1=[1, [2], '3', 4, 'Z'], list_1_alias=[1, [2], '3', 4, 'Z']
# list_2=['a', 'different', 'list'],
# list_3=[[1, [2], '3', 4, 'Z'], ['a', 'b', 'c'], [1, [2], '3', 4, 'Z']]

list_1[1] = ['a', 'new', 'sub list']
print(f"# {list_1=}, {list_1_alias=}\n# {list_2=},\n# {list_3=}")
# list_1=[1, ['a', 'new', 'sub list'], '3', 4, 'Z'], list_1_alias=[1, ['a', 'new', 'sub list'], '3', 4, 'Z']
# list_2=['a', 'different', 'list'],
# list_3=[[1, ['a', 'new', 'sub list'], '3', 4, 'Z'], ['a', 'b', 'c'], [1, ['a', 'new', 'sub list'], '3', 4, 'Z']]
