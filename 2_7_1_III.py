str_1 = "1"
complex_1 = complex(str_1)
print(f"# {type(str_1)} converted to {type(complex_1)} {complex_1}")
# <class 'str'> converted to <class 'complex'> (1+0j)

str_2 = "3+4j"
complex_2 = complex(str_2)
print(f"# {type(str_2)} converted to {type(complex_2)} {complex_2}")
# <class 'str'> converted to <class 'complex'> (3+4j)

int_3 = 0x1f
complex_3 = complex(int_3)
print(f"# {type(int_3)} converted to {type(complex_3)} {complex_3}")
# <class 'int'> converted to <class 'complex'> (31+0j)

float_4 = 1.414
complex_4 = complex(float_4, int_3)
print(f"# {type(float_4)} converted to {type(complex_4)} {complex_4}")
# <class 'float'> converted to <class 'complex'> (1.414+31j)

complex_0 = 6.5 + 1.1j
complex_5 = complex(complex_0, complex_2)
print(f"# {type(complex_0)} converted to {type(complex_5)} {complex_5}")
# <class 'complex'> converted to <class 'complex'> (2.5+4.1j)

print(f"# complex(a_complex) is itself: {complex_0 is complex(complex_0)}")
# complex(a_complex) is itself: True
