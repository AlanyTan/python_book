def func_side_effect(arg_1: bytearray, arg_2: bytearray) -> str:
    """Demonstrate side effect of passing arguments.

    Args:
        arg_1: any bytearray.
        arg_2: a bytearray to be changed by func_child.

    Returns:
        string representation of mutated arg_2.
    """
    arg_1.extend(b'changed by func')
    local_var = arg_1.copy()
    arg_1 = ord('2')
    arg_2[6]= arg_1
    arg_2[8:] = local_var
    return arg_2.decode()

var_1 = bytearray(0)
var_2 = bytearray(b'value 1, set by main')
print(f"# before func call {var_1=}, {var_2=}" )
# before func call var_1=bytearray(b''), var_2=bytearray(b'value 1, set by main')

print(f"# {func_side_effect(var_1, var_2)=}")
# func_side_effect(var_1, var_2)='value 2, changed by func'

print(f"# after func call {var_1=}, {var_2=}" )
# after func call var_1=bytearray(b'changed by func'), var_2=bytearray(b'value 2, changed by func')
