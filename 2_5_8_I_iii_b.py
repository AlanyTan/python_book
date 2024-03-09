string_unicode = 'Python\0\n\t程序设计'
string_escape_sequence = 'Python\x00\n\t\u7a0b\u5e8f\u8bbe\u8ba1'
string_r_string = r'Python\x00\n\t\u7a0b\u5e8f\u8bbe\u8ba1'
string_escape_slash = 'Python\\x00\\n\\t\\u7a0b\\u5e8f\\u8bbe\\u8ba1'

ascii_string = ascii(string_unicode)
print(f"# {ascii_string=}")
# ascii_string="'Python\\x00\\n\\t\\u7a0b\\u5e8f\\u8bbe\\u8ba1'"

print(f"# {string_unicode == string_escape_sequence=}")
# string_unicode == string_escape_sequence=True

print(f"# {string_r_string == string_escape_slash=}")
# string_r_string == string_escape_slash=True

print(f"# {'\'' + string_r_string + '\'' == ascii_string=}")
# ''' + string_r_string + ''' == ascii_string=True

print(f"# {string_escape_slash in ascii_string=}")
# string_escape_slash in ascii_string=True

print(f"# {string_unicode in ascii_string=}")
# string_unicode in ascii_string=False

print("#", 42, '42', ascii(42), ascii('42'))
# 42 42 42 '42'
print(f"# {42=}, {'42'=}, {ascii(42)=}, {ascii('42')=}")
# 42=42, '42'='42', ascii(42)='42', ascii('42')="'42'"
