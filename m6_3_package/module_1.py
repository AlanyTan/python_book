"""Module 1 inside subpackage"""
var_mod_1 = "defined in module 1"
print("#  in m_package module_1.py", [d for d in dir() if not d.startswith("__")])

def func_in_mod_1()-> str:
    """func defined in module 1 under sub packagem"""
    return "inside module_1 func_in_mod_1"