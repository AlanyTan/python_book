"""
Main script demonstrating module scope.
"""
"""save this as m6_2_2.py"""

import m6_2_scope

def func_demo_scope():
    print(f"# before changing global_var: {m6_2_scope.check_global_var()=}")
    m6_2_scope.global_var = 'value changed in func_demo_scope'
    print(f"# after changing global_var: {m6_2_scope.check_global_var()=}")

func_demo_scope()
# before changing global_var: m6_2_scope.check_global_var()='value set in m6_2_scope'
# after changing global_var: m6_2_scope.check_global_var()='value changed in func_demo_scope'

print(f"# because of namespace prefix, no conflict with len(): {m6_2_scope.len(1234)=}")
# because of namespace prefix, no conflict with len(): m6_2_scope.len(1234)='LEN1234'
