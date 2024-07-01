byte_arr_1 = bytearray(b'ABCDEF')
list_1 = [0, 1, 2, 3, 4, 5]

byte_arr_1[1] = ord('b')
print(f"# {byte_arr_1=}")
# byte_arr_1=bytearray(b'AbCDEF')
list_1[1] = 'a'
print(f"# {list_1=}")
# list_1=[0, 'a', 2, 3, 4, 5]
list_1[1] = ['a', 'b']
print(f"# {list_1=}")
# list_1=[0, ['a', 'b'], 2, 3, 4, 5]

byte_arr_1[2:4]=b'xyz'
print(f"# {byte_arr_1=}")
# byte_arr_1=bytearray(b'AbxyzEF')
list_1[2:4] = ['x', 'y', 'z']
print(f"# {list_1=}")
# list_1=[0, ['a', 'b'], 'x', 'y', 'z', 4, 5]
list_1[2:4] = [['x', 'y', 'z']]
print(f"# {list_1=}")
# list_1=[0, ['a', 'b'], ['x', 'y', 'z'], 'z', 4, 5]

byte_arr_1[1::2]=b'-' * int(len(byte_arr_1)/2)
print(f"# {byte_arr_1=}")
# byte_arr_1=bytearray(b'A-x-z-F')
list_1[::2] = ['x', 'y', 'z']
print(f"# {list_1=}")
# list_1=['x', ['a', 'b'], 'y', 'z', 'z', 5]

del byte_arr_1[1:5:2]
print(f"# {byte_arr_1=}")
# byte_arr_1=bytearray(b'Axz-F')
del list_1[2]
print(f"# {list_1=}")
# list_1=['x', ['a', 'b'], 'z', 'z', 5]
del list_1[0:4]
print(f"# {list_1=}")
# list_1=[5]
