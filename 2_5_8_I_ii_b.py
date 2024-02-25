int_1 = 80
int_2 = 31243
int_3 = 10


char_1 = chr(int_1)
print(f"# {char_1=}")
# char_1='P'

char_2 = chr(int_2)
s_2 = '\u7a0b'
fs_2 = f"{int_2:c}"
print(f"# {char_2=}, {char_2 == s_2 == fs_2=}")
# char_2='程', char_2 == s_2 == fs_2=True

char_3 = chr(int_3)
s_3 = '\012'
fs_3 = f"{int_3:c}"
print(f"# {char_3=}, {char_3 == s_3 == fs_3=}")
# char_3='\n', char_3 == s_3 == fs_3=True
