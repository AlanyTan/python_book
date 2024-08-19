"""Module 2 inside m6_3_package"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger("m6_3_package")

var_mod_2 = 2
logger.debug("   m6_3_package/module_2.py root level, %s",
             [d for d in dir() if not d.startswith('__')])


def func_in_mod_2() -> str:
    """func defined in module_2 under m6_3_package"""
    return func_in_mod_2.__doc__
