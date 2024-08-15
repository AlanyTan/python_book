"""
Main script demonstrating dir() and globals().
"""
"""save this as m6_2_3.py"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger("main_script")

import m6_2_3_scope
#DEBUG - m6_2_3_scope(m6_2_3_scope.py:16) - in module global scope, globals() == locals()=True

def first_level_local_namespace() -> None:
    """Demo func #1 for locals()"""
    logger.debug(f"in scope of first_level_local_ns, {globals() == locals()=}")
    first_level_var = 0
    def second_level_local_namespace() -> None:
        logger.debug(f"inside second_level_local_ns, {globals() == locals()=}")
        second_level_var = 1
        print("#===second level globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#   ')
        print("#===second level locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#   ')
        print(f"#===second_level_local_namespace {dir()=}")
        m6_2_3_scope.module_level_local_namespace()

    print("#==first level globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#  ')
    print("#==first level locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#  ')
    print(f"#==first_level_local_namespace {dir()=}")
    second_level_local_namespace()

logger.debug(f"in root level, {globals() == locals()=}")
#DEBUG - main_script(m6_2_3.py:39) - in root level, globals() == locals()=True

print("#=root level globals:"
      , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
      , sep='\n# ')
#=root level globals:
#=root level globals:
# ('logging', <module 'logging' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\logging\\__init__.py'>)
#   ('logger', <Logger main_script (DEBUG)>)
# ('m6_2_3_scope', <module 'm6_2_3_scope' from 'C:\\Users\\user\\Documents\\python_book\\m6_2_3_scope.py'>)
# ('first_level_local_namespace', <function first_level_local_namespace at 0x000001C1C8FF71A0>)

print(f"#=root level dir(): "
      ,[x for x in dir() if not x.startswith('__')])
#=root level dir():  ['first_level_local_namespace', 'logger', 'logging', 'm6_2_3_scope']

print(f"#=root level dir(m6_2_3_scope): "
      ,[x for x in dir(m6_2_3_scope) if not x.startswith('__')])
#=root level dir(m6_2_3_scope):  ['global_var', 'logger', 'logging', 'm6_1_circle', 'module_level_local_namespace']

first_level_local_namespace()
#DEBUG - main_script(m6_2_3.py:16) - in scope of first_level_local_ns, globals() == locals()=False
#==first level globals:
#  ('logging', <module 'logging' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\logging\\__init__.py'>)
#   ('logger', <Logger main_script (DEBUG)>)
#  ('m6_2_3_scope', <module 'm6_2_3_scope' from 'C:\\Users\\user\\Documents\\python_book\\m6_2_3_scope.py'>)
#  ('first_level_local_namespace', <function first_level_local_namespace at 0x00000206D89071A0>)
#==first level locals:
#  ('first_level_var', 0)
#  ('second_level_local_namespace', <function first_level_local_namespace.<locals>.second_level_local_namespace at 0x00000206D89420C0>)
#==first_level_local_namespace dir()=['first_level_var', 'second_level_local_namespace']
#DEBUG - main_script(m6_2_3.py:20) - inside second_level_local_ns, globals() == locals()=False
#===second level globals:
#   ('logging', <module 'logging' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\logging\\__init__.py'>)
#   ('logger', <Logger main_script (DEBUG)>)
#   ('m6_2_3_scope', <module 'm6_2_3_scope' from 'C:\\Users\\user\\Documents\\python_book\\m6_2_3_scope.py'>)
#   ('first_level_local_namespace', <function first_level_local_namespace at 0x00000206D89071A0>)
#===second level locals:
#   ('second_level_var', 1)
#===second_level_local_namespace dir()=['second_level_var']
#DEBUG - m6_2_3_scope(m6_2_3_scope.py:18) - in scope of module_level_local_ns, globals() == locals()=False
#==module_level_local_namespace globals:
#   ('logging', <module 'logging' from 'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\logging\\__init__.py'>)
#   ('logger', <Logger m6_2_3_scope (DEBUG)>)
#   ('m6_1_circle', <module 'm6_1_circle' from 'C:\\Users\\alan\\OneDrive\\Documents\\python_book\\m6_1_circle.py'>)
#   ('global_var', 'value set in m6_2_3_scope')
#   ('module_level_local_namespace', <function module_level_local_namespace at 0x00000206D8942160>)
#==module_level_local_namespace locals:
#   ('local_var', 'value set in m6_2_3_scope.module_level_local_namespace')
#==module_level_local_namespace dir()=['local_var']
#===submodule_level local_namespace dir(m6_1_circle)=['PI', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'area', 'circumference']

print(f"# accessing object in sub module: {m6_2_3_scope.m6_1_circle.PI=}")
# accessing object in sub module: m6_2_3_scope.m6_1_circle.PI=3.14159265
