int_positive = 42
bin_str_p = bin(int_positive)
print(f"# {type(int_positive)} converted to {type(bin_str_p)} {bin_str_p}")
# <class 'int'> converted to <class 'str'> 0b101010

bin_str_n = bin(-int_positive)
print(f"# {type(int_positive)} converted to {type(bin_str_n)} {bin_str_n}")
# <class 'int'> converted to <class 'str'> -0b101010

oct_str_p = oct(int_positive)
print(f"# {type(int_positive)} converted to {type(oct_str_p)} {oct_str_p}")
# <class 'int'> formatted to <class 'str'> 0o52

oct_str_fstr = f"{int_positive:#o}"
print(f"# {type(int_positive)} formatted to "
      f"{type(oct_str_fstr)} {oct_str_fstr}")
# <class 'int'> formatted to <class 'str'> 0o52

hex_str_n = hex(-int_positive)
print(f"# {type(int_positive)} converted to {type(hex_str_n)} {hex_str_n}")
# <class 'int'> converted to <class 'str'> -0x2a

hex_str_format = "{:#x}".format(-int_positive)
print(f"# {type(int_positive)} converted to "
      f"{type(hex_str_format)} {hex_str_format}")
# <class 'int'> converted to <class 'str'> -0x2a
