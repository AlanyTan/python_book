"""Learning Python Package.

This package provides basic concepts of how Python package
and its modules are organized.

Modules:
    module_1: module 1 include functions to demo nested package/module
    module_2: module 2 include functions to demo nested package/module

Usage:
    >>> from m6_3_package import module_1
    >>> result = module_1.func_in_mod_1()


For more details on each module, refer to the module docstring.
"""
"""Be caurious of using this constant"""
__all__ = ["module_1", "m6_3_2_geometry"]

"""the following statments are for educational purpose only,
    print() and non-initialization related functions are not recommended in __init__.py"""
print("#  in m6_3_package __init__.py")
def func_in_init() -> str:
    """demo function inside __init__.py"""
    return "in func_in_init of m6_3_package"