def func_side_effect(arg_1: int, arg_2: bytearray) -> str:
    arg_1 = 57
    arg_2[6]= arg_1
    return str(arg_2)[12:19]

var_int = 0
var_bytearray = bytearray(b'value 1 from main')
print(f"# {func_side_effect(var_int, var_bytearray)=}")
# func_side_effect(var_int, var_bytearray)='value 9'

print(f"# after func call {var_int=}, {var_bytearray=}" )
# after func call var_int=0, var_bytearray=bytearray(b'value 9 from main')
