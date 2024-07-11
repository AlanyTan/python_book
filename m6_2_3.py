"""
Main script demonstrating dir() and globals().
"""
"""save this as m6_2_3.py"""

import m6_2_3_scope
# at module global scope, globals() == locals()=True

def first_level_local_namespace() -> None:
    """Demo func #1 for locals()"""
    first_level_var = 0
    def second_level_local_namespace() -> None:
        second_level_var = 1
        print("#===second level globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#   ')
        print("#===second level locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#   ')
        print(f"#===second_level_local_namespace {dir()=}")

    print(f"# at local scope, {globals() == locals()=}")
    print("#==first level globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#  ')
    print("#==first level locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#  ')
    print(f"#==first_level_local_namespace {dir()=}")
    second_level_local_namespace()

print(f"# at root level, {globals() == locals()=}")
# at root level, globals() == locals()=True
print("#=root level globals:"
      , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
      , sep='\n# ')
#=root level globals:
# ('m6_2_3_scope', <module 'm6_2_3_scope' from 'C:\\Users\\user\\Documents\\python_book\\m6_2_3_scope.py'>)
# ('first_level_local_namespace', <function first_level_local_namespace at 0x0000016C9D47E5C0>)

print(f"#=root level dir(): "
      ,[x for x in dir() if not x.startswith('__')])
#=root level dir():  ['first_level_local_namespace', 'm6_2_3_scope']

print(f"#=root level dir(m6_2_3_scope): "
      ,[x for x in dir(m6_2_3_scope) if not x.startswith('__')])
#=root level dir(m6_2_3_scope):  ['global_var', 'module_level_local_namespace']

first_level_local_namespace()
# at local scope, globals() == locals()=False
#==first level globals:
#  ('m6_2_3_scope', <module 'm6_2_3_scope' from 'C:\\Users\\user\\Documents\\python_book\\m6_2_3_scope.py'>)
#  ('first_level_local_namespace', <function first_level_local_namespace at 0x000002787164E5C0>)
#==first level locals:
#  ('first_level_var', 0)
#  ('second_level_local_namespace', <function first_level_local_namespace.<locals>.second_level_local_namespace at 0x00000278716A74C0>)
#==first_level_local_namespace dir()=['first_level_var', 'second_level_local_namespace']
#===second level globals:
#   ('m6_2_3_scope', <module 'm6_2_3_scope' from 'C:\\Users\\user\\Documents\\python_book\\m6_2_3_scope.py'>)
#   ('first_level_local_namespace', <function first_level_local_namespace at 0x000002787164E5C0>)
#===second level locals:
#   ('second_level_var', 1)
#===second_level_local_namespace dir()=['second_level_var']

m6_2_3_scope.module_level_local_namespace()
# at module local scope, globals() == locals()=False
#==module_level_local_namespace globals:
#   ('global_var', 'value set in m6_2_3_scope')
#   ('module_level_local_namespace', <function module_level_local_namespace at 0x000001D43C8B7240>)
#==module_level_local_namespace locals:
#   ('local_var', 'value set in m6_2_3_scope.module_level_local_namespace')
#==module_level_local_namespace dir()=['local_var']
