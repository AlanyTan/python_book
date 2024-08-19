"""Module 1 inside m6_3_package"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger("m6_3_package")

var_mod_1 = "defined in module 1"
logger.debug("   m6_3_package/module_1.py root level, %s",
             [d for d in dir() if not d.startswith('__')])


def func_in_mod_1() -> str:
    """func defined in module_1 under m6_3_package"""
    return func_in_mod_1.__doc__
