"""Main script demonstrating importing into current namespace.

No functions, just demo from module import obj will bring obj into 
current namespace.
"""
"""save this as m6_2_4.py"""
from m6_2_scope import len as m6_2_scope_len, check_global_var

print(f"# {'global_var' in dir()=}")
# 'global_var' in dir()=False

print(f"# {'check_global_var' in dir()=}, {check_global_var()=}")
# 'check_global_var' in dir()=True, check_global_var()='value set in m6_2_scope'

print(f"# {'len' in __builtins__=}, {'len' in dir()=}, {'m6_2_scope_len' in dir()=},"
      f" {m6_2_scope_len(1.2)=}")
# 'len' in __builtins__=True, 'len' in dir()=False, 'm6_2_scope_len' in dir()=True, m6_2_scope_len(1.2)='LEN1.2'

def import_in_func() -> None:
      """Demo import can be done inside a function"""
      from m6_2_scope import global_var
      print(f"# {'global_var' in locals()=},{'global_var' in globals()=}, {global_var=}")

import_in_func()
# 'global_var' in locals()=True,'global_var' in globals()=False, global_var='value set in m6_2_scope'
