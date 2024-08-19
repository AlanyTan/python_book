"""Main script demonstrating importing into current namespace.

No functions, just demo from module import obj will bring obj into 
current namespace.
"""
"""save this as m6_2_4.py"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger("main_script")

from m6_2_4_module import circle, CONST_1
#DEBUG - m6_2_4_module(m6_2_4_module.py:8) - entering module root level['logger', 'logging']
#DEBUG - m6_2_4_module(m6_2_4_module.py:22) - exiting module root level['CONST_1', 'circle', 'local_ns_func', 'logger', 'logging']

print("#=root level globals:", *
      [(k, v) for k, v in globals().items() if not k.startswith('__')], sep='\n#  ')
#=root level globals:
#  ('logging', <module 'logging' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\logging\\__init__.py'>)
#  ('logger', <Logger main_script (DEBUG)>)
#  ('circle', <module 'm6_1_circle' from 'C:\\Users\\user\\Documents\\python_book\\m6_1_circle.py'>)
#  ('CONST_1', 'Module Constant')

print("# dir(circle):", [d for d in dir(circle) if not d.startswith("__")])
# dir(circle): ['PI', 'area', 'circumference']


def import_in_func() -> None:
    """Demo import can be done inside a function"""
    logger.debug(f"import_in_func() called {dir()=}")
    from m6_2_4_module import local_ns_func
    print("#==first level globals:", *
          [(k, v) for k, v in globals().items() if not k.startswith('__')],
          sep='\n#  ')
    print("#==first level locals:", *
          [(k, v) for k, v in locals().items() if not k.startswith('__')],
          sep='\n#  ')
    print("#:", local_ns_func())
    logger.debug(f"import_in_func() ending {dir()=}")


import_in_func()
#DEBUG - main_script(m6_2_4.py:31) - import_in_func() called dir()=[]
#==first level globals:
#  ('logging', <module 'logging' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\logging\\__init__.py'>)
#  ('logger', <Logger main_script (DEBUG)>)
#  ('circle', <module 'm6_1_circle' from 'C:\\Users\\user\\Documents\\python_book\\m6_1_circle.py'>)
#  ('CONST_1', 'Module Constant')
#  ('import_in_func', <function import_in_func at 0x000001D0009D71A0>)
#==first level locals:
#  ('local_ns_func', <function local_ns_func at 0x000001D000A12160>)
#DEBUG - m6_2_4_module(m6_2_4_module.py:18) - local_ns_func() called
#: m6_2_4_module.local_ns_func() - demo from module import func
#DEBUG - main_script(m6_2_4.py:40) - import_in_func() ending dir()=['local_ns_func']

print("#=root level locals:", *
      [(k, v) for k, v in locals().items() if not k.startswith('__')], sep='\n#  ')
#=root level locals:
#  ('logging', <module 'logging' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\logging\\__init__.py'>)
#  ('logger', <Logger main_script (DEBUG)>)
#  ('circle', <module 'm6_1_circle' from 'C:\\Users\\user\\Documents\\python_book\\m6_1_circle.py'>)
#  ('CONST_1', 'Module Constant')
#  ('import_in_func', <function import_in_func at 0x000001D0009D71A0>)
