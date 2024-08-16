byte_arr_1 = bytearray(b'abc')

x = 0X44
byte_arr_1.append(x)
print(f"# byte_arr_1.append(x): {byte_arr_1}")
# byte_arr_1.append(x): bytearray(b'abcD')

print(f"# byte_arr_1.pop(): {byte_arr_1.pop()}, {byte_arr_1=}")
# byte_arr_1.pop(): 68, byte_arr_1=bytearray(b'abc')

byte_arr_1.insert(2, x)
print(f"# byte_arr_1.insert(2,x): {byte_arr_1}")
# byte_arr_1.insert(2,x): bytearray(b'abDc')

byte_arr_1.remove(x)
print(f"# byte_arr_1.remove(x): {byte_arr_1}")
# byte_arr_1.remove(x): bytearray(b'abc')

byte_arr_1.reverse()
print(f"# byte_arr_1.reverse(): {byte_arr_1}")
# byte_arr_1.reverse(): bytearray(b'cba')

byte_arr_1_alias = byte_arr_1
byte_arr_2 = byte_arr_1.copy()
byte_arr_1_alias.clear()
print(f"# byte_arr_1.clear: {byte_arr_1=}, {byte_arr_2=}")
# byte_arr_1.clear: byte_arr_1=bytearray(b''), byte_arr_2=bytearray(b'cba')
