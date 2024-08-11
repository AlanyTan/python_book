int_1 = 0xa1b2c3d4e5
bytes_1 = int_1.to_bytes(5, "little")
print(f"# {int_1}, as hex {int_1:#x} converted to little-endian bytes:{bytes_1}")
# 694488913125, as hex 0xa1b2c3d4e5 converted to little-endian bytes: b'\xe5\xd4\xc3\xb2\xa1'

int_2 = -0x7fffffffff
bytes_2 = int_2.to_bytes(5, "big", signed=True)
print(f"# {int_2}, as hex {int_2:#x} converted to  big-endian bytes:{bytes_2}")
# -549755813887, as hex -0x7fffffffff converted to big-endian bytes: b'\x80\x00\x00\x00\x01'
