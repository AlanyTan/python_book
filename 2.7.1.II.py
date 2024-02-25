str_1 = "3.14159"
float_1 = float(str_1)
print(f"# {type(str_1)} converted to {type(float_1)} {float_1}")
# <class 'str'> converted to <class 'float'> 3.14159

str_2 = "3"
float_2 = float(str_2)
print(f"# {type(str_2)} converted to {type(float_2)} {float_2}")
# <class 'str'> converted to <class 'float'> 3.0

int_3 = 4
float_3 = float(int_3)
print(f"# {type(int_3)} converted to {type(float_3)} {float_3}")
# <class 'int'> converted to <class 'float'> 4.0

int_4 = 0x1f
float_4 = float(int_4)
print(f"# {type(int_4)} converted to {type(float_4)} {float_4}")
# <class 'int'> converted to <class 'float'> 31.0

float_4 = 2.17
print(f"# float(a_float) is itself: {float_4 is float(float_4)}")
# float(a_float) is itself: True
