"""Nested Package.

This package shows how to create sub-packages and organize modules using nested packages.

Modules:
    module_1: module include functions to demo nested package/module
"""
CONST_1='defined in package __init__.py'
print("in m_package __init__.py", dir())
def func_in_init() -> str:
    """func defined in sub package __init__.py"""
    return ("inside __init__.py func_in_init()")