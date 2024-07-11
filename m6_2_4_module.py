"""Module demo import to current namespace
"""
"""save this as m6_2_4_module"""

import m6_1_circle as circle

CONST_1 = "Module Constant"

def local_ns_func() -> str:
    """m6_2_4_module.local_ns_func() - demo from {} import {}"""
    return local_ns_func.__doc__.format(local_ns_func.__module__
                                        ,local_ns_func.__name__) 
