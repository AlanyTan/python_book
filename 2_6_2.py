string_unicode = 'Python\0\n\t程序设计'

ascii_string = ascii(string_unicode)

reverse_ascii = ascii_string.strip("'").encode('ascii').decode('unicode_escape')
print(f"# {reverse_ascii == string_unicode=}")
# reverse_ascii == string_unicode=True
