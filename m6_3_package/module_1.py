"""Module 1 inside m6_3_package"""
var_mod_1 = "defined in module 1"
print("#   m6_3_package/module_1.py root level statements"
      , [d for d in dir() if not d.startswith("__")])

def func_in_mod_1()-> str:
    """func defined in module_1 under m6_3_package"""
    return func_in_mod_1.__doc__
