str_1 = "False"
bool_1 = bool(str_1)
print(f"# {type(str_1)} converted to {type(bool_1)} {bool_1}")
# <class 'str'> converted to <class 'bool'> True

str_2 = ""
bool_2 = bool(str_2)
print(f"# {type(str_2)} converted to {type(bool_2)} {bool_2}")
# <class 'str'> converted to <class 'bool'> False

int_3 = 0x1f
bool_3 = bool(int_3)
print(f"# {type(int_3)} converted to {type(bool_3)} {bool_3}")
# <class 'int'> converted to <class 'bool'> True

float_4 = 0.0
bool_4 = bool(float_4)
print(f"# {type(float_4)} converted to {type(bool_4)} {bool_4}")
# <class 'float'> converted to <class 'bool'> False

none_5 = None
bool_5 = bool(none_5)
print(f"# {type(none_5)} converted to {type(bool_5)} {bool_5}")
# <class 'NoneType'> converted to <class 'bool'> False

bool_0 = True
print(f"# bool(a_bool) is itself: {bool_0 is bool(bool_0)}")
# bool(a_bool) is itself: True
