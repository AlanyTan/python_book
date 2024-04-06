"""
Main script demonstrating dir() and globals().
"""
"""save this as m6_2_3.py"""

import m6_2_scope

def beautify_output(obj: dict|list) -> None:
    """Print globals(), locals(), dir() return value one item per line

    Args:
        obj: either a dict or a list of names found by globals, locals or dir.

    Returns:
        None
    """
    if isinstance(obj, dict):
        start_bracket = '{'
        end_bracket = '}'
    else:
        start_bracket = '['
        end_bracket = ']'

    print("#", start_bracket)
    for item in obj:
        if item.startswith('__') and item.endswith('__'):
            pass
        else:
            if start_bracket == '{':
                print(f"#  {item}: {obj[item]},")
            else:
                print(f"#  {item},")
    print("#", end_bracket)

def first_layer_demo_locals() -> None:
    """Demo func #1 for locals()"""
    first_layer_var = 0
    def second_layer_demo_locals() -> None:
        second_layer_var = 1
        beautify_output(locals())

    beautify_output(locals())
    second_layer_demo_locals()

beautify_output(globals())
# {
#  m6_2_scope: <module 'm6_2_scope' from '/home/alan/Documents/Python.book/m6_2_scope.py'>,
#  beautify_output: <function beautify_output at 0x76c67d3955a0>,
#  first_layer_demo_locals: <function first_layer_demo_locals at 0x76c67d397d00>,
# }

beautify_output(dir())
# [
#  beautify_output,
#  first_layer_demo_locals,
#  m6_2_scope,
# ]

beautify_output(dir(m6_2_scope))
# [
#  check_global_var,
#  global_var,
#  len,
# ]

first_layer_demo_locals()
# {
#  first_layer_var: 0,
#  second_layer_demo_locals: <function first_layer_demo_locals.<locals>.second_layer_demo_locals at 0x7ab3f9161b40>,
# }
# {
#  second_layer_var: 1,
# }