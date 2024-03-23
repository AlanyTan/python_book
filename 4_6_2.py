def func_side_effect(arg_1: bytearray, arg_2: bytearray) -> str:
    arg_1.extend(b'child')
    arg_1 = ord('9')
    arg_2[6]= arg_1
    arg_2 += b"'s child"
    return arg_2.decode()

var_1 = bytearray(1)
var_2 = bytearray(b'value 1 from main')
print(f"# {func_side_effect(var_1, var_2)=}")
# func_side_effect(var_1, var_2)="value 9 from main's child"

print(f"# after func call {var_1=}, {var_2=}" )
# after func call var_1=bytearray(b'\x00child'), var_2=bytearray(b"value 9 from main\'s child")
