ba_1 = bytearray(4)
print(f"# {ba_1=}")
# ba_1=bytearray(b'\x00\x00\x00\x00')

ba_2 = bytearray(b'\tabcd\n')
print(f"# {ba_2=}")
# ba_2=bytearray(b'\tabcd\n')

ba_3 = bytearray([0, 1, 2, 3, 4, 5])
print(f"# {ba_3=}")
# ba_3=bytearray(b'\x00\x01\x02\x03\x04\x05')

ba_4 = bytearray('Python程序设计', 'utf-8')
print(f"# {ba_4=}")
# ba_4=bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1')
