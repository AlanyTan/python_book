string_2 = string_1 = "ABCD"
string_1 = string_1 + 'XYZ'
print(f"# {string_1=}, {string_2=}")
# string_1='ABCDEFG', string_2='ABCD'

string_2 = string_1 = "ABCD"
string_1 += "EFG"
print(f"# {string_1=}, {string_2=}")
# string_1='ABCDEFG', string_2='ABCD'

byte_arr_2 = byte_arr_1 = bytearray(b'ABCD')
byte_arr_1 = byte_arr_1 + b'EFG'
print(f"# {byte_arr_1=}, {byte_arr_2=}")
# byte_arr_1=bytearray(b'ABCDEFG'), byte_arr_2=bytearray(b'ABCD')

byte_arr_2 = byte_arr_1 = bytearray(b'ABCD')
byte_arr_1 += b'EFG'
print(f"# {byte_arr_1=}, {byte_arr_2=}")
# byte_arr_1=bytearray(b'ABCDEFG'), byte_arr_2=bytearray(b'ABCDEFG')

byte_arr_1 *= 2
print(f"# {byte_arr_1=}, {byte_arr_2=}")
# byte_arr_1=bytearray(b'ABCDEFGABCDEFG'), byte_arr_2=bytearray(b'ABCDEFGABCDEFG')
