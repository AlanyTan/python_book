tuple_1 = ('a', 'b')
string_1 = 'cd'
int_1 = 101
byte_arr_1 = bytearray(b'ef')

set_1 = {tuple_1, int_1, string_1, *byte_arr_1}
print(f"# {set_1=}")
# set_1={('a', 'b'), 'cd', 101, 102}
