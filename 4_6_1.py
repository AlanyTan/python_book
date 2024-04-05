def func_side_effect(arg_p: str) -> str:
    """Demonstrate side effect.

    Args:
        arg_s: incoming string to be processed.

    Returns:
        arg_s repeated global_var_in times.
    """
    global global_var_out
    multiplier = global_var_in + 1
    global_var_out = multiplier
    return arg_p * multiplier

global_var_in = 1
global_var_out = 'old value'
print(f"# {func_side_effect('any')=}, {global_var_out=}" )
# func_side_effect('any')='anyany', global_var_out=2

global_var_in = 2
print(f"# {func_side_effect('any')=}, {global_var_out=}" )
# func_side_effect('any')='anyanyany', global_var_out=3
