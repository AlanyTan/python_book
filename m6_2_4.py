"""Main script demonstrating importing into current namespace.

No functions, just demo from module import obj will bring obj into 
current namespace.
"""
"""save this as m6_2_4.py"""

from m6_2_4_module import circle, CONST_1
print("#=root level globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#  ')
#=root level globals:
#  ('circle', <module 'm6_1_circle' from 'C:\\Users\\user\\Documents\\python_book\\m6_1_circle.py'>)
#  ('CONST_1', 'Module Constant')

print("# dir():", [d for d in dir(circle) if not d.startswith("__")])
# dir(): ['PI', 'area', 'circumference']

def import_in_func() -> None:
    """Demo import can be done inside a function"""
    from m6_2_4_module import local_ns_func
    print("#==first level globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#  ')
    print("#==first level locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#  ')
    print("#:", local_ns_func())

import_in_func()
#==first level globals:
#  ('local_ns_func', <function local_ns_func at 0x000001BA842F7240>)
#  ('CONST_1', 'Module Constant')
#  ('import_in_func', <function import_in_func at 0x000001BA842F71A0>)
#==first level locals:
#  ('circle', <module 'm6_1_circle' from 'C:\\Users\\user\\Documents\\python_book\\m6_1_circle.py'>)
#: executed local_ns_func

print("#=root level locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#  ')
#=root level locals:
#  ('local_ns_func', <function local_ns_func at 0x00000222A1E67240>)
#  ('CONST_1', 'Module Constant')
#  ('import_in_func', <function import_in_func at 0x00000222A1E671A0>)
