"""Module 2 inside subpackage"""
var_mod_2 = 2
print("in m_package module_2.py", [d for d in dir() if not d.startswith("__")])

def func_in_mod_2()-> str:
    """func defined in module 2 under sub packagem"""
    return "inside module_2 func_in_mod_2"