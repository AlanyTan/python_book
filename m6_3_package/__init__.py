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
print("in m6_3_package __init__.py")
__all__ = ["module_1", "m6_3_2_geometry"]
