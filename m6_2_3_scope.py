"""Module demo global/local scope of module import

A module contain global var and function that can be invoked from 
within the program import this module.
"""
"""save this as m6_2_3_scope.py"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger("m6_2_3_scope")

import m6_1_circle

global_var = 'value set in m6_2_3_scope'
logger.debug(f"in module global scope, {globals() == locals()=}")

def module_level_local_namespace() -> None:
    """Demo func of local namespace in amodule"""
    logger.debug(f"in scope of module_level_local_ns, {globals() == locals()=}")
    local_var = 'value set in m6_2_3_scope.module_level_local_namespace'
    print("#==module_level_local_namespace globals:"
          , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
          , sep='\n#   ')
    print("#==module_level_local_namespace locals:"
          , *[(k, v) for k, v in locals().items() if not k.startswith('__')]
          , sep='\n#   ')
    print(f"#==module_level_local_namespace {dir()=}")
    print(f"#===submodule_level local_namespace {dir(m6_1_circle)=}")
