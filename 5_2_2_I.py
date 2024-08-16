ba_1 = bytearray(b'012345')
list_1 = [0, 1, 2, 3, 4, 5]

ba_1[1] = ord('a')
list_1[1] = ba_1
print(f"# {ba_1=}, {list_1=}")
# ba_1=bytearray(b'0a2345'), list_1=[0, bytearray(b'0a2345'), 2, 3, 4, 5]

list_1[2] = ['a', 'b']
print(f"# {list_1=}")
# list_1=[0, bytearray(b'0a2345'), ['a', 'b'], 3, 4, 5]

ba_1[3:5] = b'xyz'
list_1[3:5] = ['x', 'y', 'z']
print(f"# {list_1=}")
# list_1=[0, bytearray(b'0a2xyz5'), ['a', 'b'], 'x', 'y', 'z', 5]

list_1[3:5] = [['x', 'y', 'z']]
print(f"# {list_1=}")
# list_1=[0, ['a', 'b'], ['x', 'y', 'z'], 'z', 4, 5]

ba_1[1::2] = b'-' * int(len(ba_1) / 2)
list_1[::2] = "-" * int(len(list_1) / 2)
print(f"# {list_1=}")
# list_1=['-', bytearray(b'0-2-y-5'), '-', ['x', 'y', 'z'], '-', 5]

list_1[1][1] = ord('&')
list_1[3][1:1] = '&'
print(f"# {ba_1=}, {list_1=}")
# ba_1=bytearray(b'0&2-y-5'), list_1=['-', bytearray(b'0&-2-y-5'), '-', ['x', '&', 'y', 'z'], '-', 5]
