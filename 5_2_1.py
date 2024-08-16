ba_example = bytearray(b'abcdefg')
print(f"# 1st byte is {ba_example[0]=}, {b'abcdefg'[0]=}")
# 1st byte is ba_example[0]=97, b'abcdefg'[0]=97

print(f"# 3rd to 5th bytes are {ba_example[2:5]=}, {b'abcdefg'[2:5]=}")
# 3rd to 5th bytes are ba_example[2:5]=bytearray(b'cde'), b'abcdefg'[2:5]=b'cde'

print(f"# every other bytes are {ba_example[::2]=}, {b'abcdefg'[::2]=}")
# every other bytes are ba_example[::2]=bytearray(b'aceg'), b'abcdefg'[::2]=b'aceg'

ba_alias = ba_example
ba_copy = ba_example[::]

ba_example[0] = ord('A')
print(f"# mutate first byte:",
      f"{ba_example=}", f"{ba_alias=}", f"{ba_copy=}", sep="\n#\t")
# mutate first byte:
#       ba_example=bytearray(b'Abcdefg')
#       ba_alias=bytearray(b'Abcdefg')
#       ba_copy=bytearray(b'abcdefg')

ba_example[3:5] = b'DEFG'
print(f"# mutate the 3rd to 4th bytes, assign different length of bytes:",
      f"{ba_example=}", f"{ba_alias=}", f"{ba_copy=}", sep="\n#\t")
# mutate the 3rd to 4th bytes, assign different length of bytes:
#       ba_example=bytearray(b'AbcDEFGfg')
#       ba_alias=bytearray(b'AbcDEFGfg')
#       ba_copy=bytearray(b'abcdefg')

ba_example[::-2] = range(len(ba_example[::2]))
print(f"# mutate every other byte from last to first byte:",
      f"{ba_example=}", f"{ba_alias=}", f"{ba_copy=}", sep="\n#\t")
# mutate every other byte from last to first byte:
#       ba_example=bytearray(b'\x04b\x03D\x02F\x01f\x00')
#       ba_alias=bytearray(b'\x04b\x03D\x02F\x01f\x00')
#       ba_copy=bytearray(b'abcdefg')

ba_example[1::2] = b''
print(f"# replace every other byte with empty byte:",
      f"{ba_example=}", f"{ba_alias=}", f"{ba_copy=}", sep="\n#\t")
# delete every other byte from 1:
#       ba_example=bytearray(b'\x04\x03\x02\x01\x00')
#       ba_alias=bytearray(b'\x04\x03\x02\x01\x00')
#       ba_copy=bytearray(b'abcdefg')

del ba_example[::2]
print(f"# delete every other byte:",
      f"{ba_example=}", f"{ba_alias=}", f"{ba_copy=}", sep="\n#\t")
# delete every other byte from 1:
#       ba_example=bytearray(b'\x04\x02\x00')
#       ba_alias=bytearray(b'\x04\x02\x00')
#       ba_copy=bytearray(b'abcdefg')
