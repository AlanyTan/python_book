def func_side_effect(arg_p: str) -> str:
    global global_var_out
    multiplier = int(len(global_var_in)) % 5
    global_var_out = multiplier
    return arg_p[:3] * multiplier

global_var_in = 'value 1 from main'
global_var_out = 'old value'
print(f"# {func_side_effect("any")=}, {global_var_out=}" )
# func_side_effect("any")='anyany', global_var_out=2

global_var_in = 'value' * global_var_out 
global_var_out = 'old value'
print(f"# {func_side_effect("any")=}, {global_var_out=}" )
# func_side_effect("any")='', global_var_out=0
