list_1 = [1, [2], 3, [], 4]
list_2 = [list('abc'), list(range(3)), [1.0, "abc", 3]]
list_3 = [list_1, list_2]
print(f"# {list_3=}")
# list_3=[[1, [2], 3, [], 4], [['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]]

list_1.append("Z")
print(f"# {list_1=}\n# {list_3=}")
# list_1=[1, [2], 3, [], 4, 'Z']
# list_3=[[1, [2], 3, [], 4, 'Z'], [['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]]

list_1 = ["a", "different", "list"]
print(f"# {list_1=}\n# {list_3=}")
# list_1=['a', 'different', 'list']
# list_3=[[1, [2], 3, [], 4, 'Z'], [['a', 'b', 'c'], [0, 1, 2], [1.0, 'abc', 3]]]

list_2[1] = ['a', 'new', 'sub list']
print(f"# {list_2=}\n# {list_3=}")
# list_2=[['a', 'b', 'c'], ['a', 'new', 'sub list'], [1.0, 'abc', 3]]
# list_3=[[1, [2], 3, [], 4, 'Z'], [['a', 'b', 'c'], ['a', 'new', 'sub list'], [1.0, 'abc', 3]]]

str_1 = 'abc'
ba_1 = bytearray(b'xyz')
list_4 = [str_1, str_1, ba_1, ba_1]
str_1 *= 2
list_4[2] *= 2
print(f"# {str_1=}, {ba_1=}\n# {list_4=}")
# str_1='abcabc', ba_1=bytearray(b'xyzxyz')
# list_4=['abc', 'abc', bytearray(b'xyzxyz'), bytearray(b'xyzxyz')]
