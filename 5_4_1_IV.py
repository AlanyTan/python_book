list_1 = [1, [2], 3, [], 4]
list_2 = [list('abc'), list(range(3)), [1.0, "abc", 3]]
list_3 = [list_1, list_2]
print(f"# {list_3=}")
# list_3=[[1, [2], 3, [], 4], [['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]]

list_1.append("Z")
print(f"# {list_1=}, {list_3=}")
# list_1=[1, [2], 3, [], 4, 'Z'], list_3=[[1, [2], 3, [], 4, 'Z'], [['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]]

list_1=["a", "different", "list"]
print(f"# {list_1=}, {list_3=}")
# list_1=[1, [2], 3, [], 4, 'Z'], list_3=[[1, [2], 3, [], 4, 'Z'], [['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]]

str_1 = 'abc'
ba_1 = bytearray(b'xyz')
list_4 = [str_1, str_1, ba_1, ba_1]
str_1 *= 2
ba_1 *= 2
print(f"# {list_4=}")
# list_4=['abc', 'abc', bytearray(b'xyzxyz'), bytearray(b'xyzxyz')]
