str_1 = "12345"
int_1 = int(str_1)
print(f"# {type(str_1)} converted to {type(int_1)} {int_1}")
# <class 'str'> converted to <class 'int'> 12345

str_2 = "1a2f"
int_2 = int(str_2, 16)
print(f"# {type(str_2)} converted to {type(int_2)} {int_2}")
# <class 'str'> converted to <class 'int'> 6703

str_3 = "1z"
int_3 = int(str_3, 36)
print(f"# {type(str_3)} converted to {type(int_3)} {int_3}")
# <class 'str'> converted to <class 'int'> 71

float_4 = 4.99999
int_4 = int(float_4)
print(f"# {type(float_4)} converted to {type(int_4)} {int_4}")
# <class 'float'> converted to <class 'int'> 4

print(f"# bin, oct, hex are all int: {0b1010101 == 0o125 == 0x55 == int(85)}")
# bin, oct, hex are all int: True
