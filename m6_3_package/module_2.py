"""Module 2 inside m6_3_package"""
var_mod_2 = 2
print("#  m6_3_package/module_2.py root level statements"
      , [d for d in dir() if not d.startswith("__")])

def func_in_mod_2()-> str:
    """func defined in module_2 under m6_3_package"""
    return func_in_mod_2.__doc__
