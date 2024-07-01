ba_example = bytearray(b'abcdefg')
print(f"# 1st byte is {ba_example[0]}")
# 1st byte is 97

print(f"# 3rd to 5th bytes are {ba_example[2:5]}")
# 3rd to 5th bytes are bytearray(b'cde')

print(f"# every other bytes are {ba_example[::2]}")
# every other bytes are bytearray(b'aceg')

ba_example[0]=0xff
print(f"# mutate first byte\t\t: {ba_example}")
# mutate first byte		: bytearray(b'\xffbcdefg')

ba_example[3:5]=b'xyz'
print(f"# mutate 3rd to 5th bytes\t: {ba_example}")
# mutate 3rd to 5th bytes	: bytearray(b'\xffbcxyzfg')

ba_example[:0:-2]=range(len(ba_example[::2]))
print(f"# mutate every other byte from -1:{ba_example}")
# mutate every other byte from -1:bytearray(b'\xff\x03c\x02y\x01f\x00')

del ba_example[1::2]
print(f"# delete every other byte from 1: {ba_example}")
# delete every other byte from 1: bytearray(b'\xffcyf')

ba_copy = ba_example[::]
ba_copy[len(ba_copy):]=b'xyz'
print(f"# {ba_copy=}, {ba_example=}")
# ba_copy=bytearray(b'\xffcyfxyz'), ba_example=bytearray(b'\xffcyf')

ba_alias = ba_example
ba_alias[::]=b'abcxyz'
print(f"# {ba_alias=}, {ba_example=}")
# ba_alias=bytearray(b'abcxyz'), ba_example=bytearray(b'abcxyz')
