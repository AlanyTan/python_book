list_1 = [1, 2, 3, 4]
ba_1 = bytearray(b'ABCDE')
tuple_1 = list_1, ba_1
print(f"# {tuple_1=}")
# tuple_1=([1, 2, 3, 4], bytearray(b'ABCDE'))

list_1.remove(3)
tuple_1[1][3:] = b''
print(f"# {list_1=}, {ba_1=}, {tuple_1=}")
# list_1=[1, 2, 4], ba_1=bytearray(b'ABC'), tuple_1=([1, 2, 4], bytearray(b'ABC'))
