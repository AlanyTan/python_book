"""Module demo global/local scope of module import

A module contain global var and function that can be invoked from 
within the program import this module.
"""
"""save this as m6_2_3_scope.py"""

global_var = 'value set in m6_2_3_scope'
print(f"# at module global scope, {globals() == locals()=}")

def module_level_local_namespace() -> None:
    """Demo func of local namespace in amodule"""
    local_var = 'value set in m6_2_3_scope.module_level_local_namespace'
    print(f"# at module local scope, {globals() == locals()=}")
    print("#==module_level_local_namespace globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#   ')
    print("#==module_level_local_namespace locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#   ')
    print(f"#==module_level_local_namespace {dir()=}")
