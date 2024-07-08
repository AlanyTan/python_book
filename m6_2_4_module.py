"""Module demo import to current namespace
"""
"""save this as m6_2_4_module"""

import m6_1_circle as circle

CONST_1 = "Module Constant"

def local_ns_func() -> str:
    """demo func be imported into """
    return "executed local_ns_func"
