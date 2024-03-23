list_1 = [1, [2], 3, [], 4]
print(f"# {list_1=}")
# list_1=[1, [2], 3, [], 4]

list_2 = [list('abc'), list(range(3)), [1.0, "abc", 3]]
print(f"# {list_2=}")
# list_2=[['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]

list_3 = [list_1, list_2]
print(f"# {list_3=}")
# list_3=[[1, [2], 3, [], 4], [['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]]
