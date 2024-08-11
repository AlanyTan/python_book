bytes_1 = b'\xe5\xd4\xc3\xb2\xa1'
int_1 = (0).from_bytes(bytes_1, "little")
print(f"# {bytes_1} converted as little-endian bytes to\n#  integer hex:"
      f"{int_1:#x}, or decimal:{int_1}")
# b'\xe5\xd4\xc3\xb2\xa1' converted as little-endian bytes to
#  integer hex:0xa1b2c3d4e5, or decimal:694488913125

bytes_2 = b'\x80\x00\x00\x00\x01'
int_2 = int.from_bytes(bytes_2, "big", signed=True)
print(f"# {bytes_2} converted as big-endian bytes to\n#  integer hex:"
      f"{int_2:#x}, or decimal:{int_2}")
# b'\x80\x00\x00\x00\x01' converted as big-endian bytes to
#  integer hex:-0x7fffffffff, or decimal:-549755813887
