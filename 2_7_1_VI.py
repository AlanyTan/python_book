int_1 = 10
bytes_1 = bytes(int_1)
print(f"# {type(int_1)} converted to {type(bytes_1)} {bytes_1}")
# <class 'int'> converted to <class 'bytes'> b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00

str_2 = 'Python程序设计'
bytes_2 = bytes(str_2,'utf-8')
print(f"# {type(bytes_2)} converted to {type(bytes_2)} {bytes_2}")
# <class 'bytes'> converted to <class 'bytes'> b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'

list_of_int_3 = [0b1010000, 0o171, 0x74, 104, 111, 110]
bytes_3 = bytes(list_of_int_3)
print(f"# {type(list_of_int_3)} decoded to {type(bytes_3)} {bytes_3}")
# <class 'list'> decoded to <class 'bytes'> b'Python'

bytes_0 = b"a bytes"
print(f"# bytes(a_bytes) is itself: {bytes_0 is bytes(bytes_0)}")
# bytes(a_bytes) is itself: True
