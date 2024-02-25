int_1 = 0x1f
str_1 = str(int_1)
print(f"# {type(int_1)} converted to {type(str_1)} {str_1}")
# <class 'int'> converted to <class 'str'> 31

float_2 = 1.732
str_2 = str(float_2)
print(f"# {type(float_2)} converted to {type(str_2)} {str_2}")
# <class 'float'> converted to <class 'str'> 1.732

complex_3 = 0x1f + 1.5j
str_3 = str(complex_3)
print(f"# {type(complex_3)} converted to {type(str_3)} {str_3}")
# <class 'complex'> converted to <class 'str'> (31+1.5j)

bool_4 = True
str_4 = str(bool_4)
print(f"# {type(bool_4)} converted to {type(str_4)} {str_4}")
# <class 'bool'> converted to <class 'str'> True

none_5 = None
str_5 = str(none_5)
print(f"# {type(none_5)} converted to {type(str_5)} {str_5}")
# <class 'NoneType'> converted to <class 'str'> None

bytes_6 = b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'
str_6 = str(bytes_6)
print(f"# {type(bytes_6)} converted to {type(str_6)} {str_6}")
# <class 'bytes'> converted to <class 'str'> b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'

str_decode_6 = str(bytes_6, 'utf-8')
print(f"# {type(bytes_6)} decoded to {type(str_decode_6)} {str_decode_6}")
# <class 'bytes'> decoded to <class 'str'> Python程序设计

str_0 = "a string"
print(f"# str(a_str) is itself: {str_0 is str(str_0)}")
# str(a_str) is itself: True
