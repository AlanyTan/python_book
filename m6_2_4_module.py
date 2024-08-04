"""Module demo import to current namespace"""
"""save this as m6_2_4_module"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger("m6_2_4_module")

logger.debug(f"entering module root level"
             f"{[d for d in dir() if not d.startswith("__")]}")

import m6_1_circle as circle

CONST_1 = "Module Constant"

def local_ns_func() -> str:
    """m6_2_4_module.local_ns_func() - demo from module import func"""
    logger.debug(f"local_ns_func() called")
    return local_ns_func.__doc__

logger.debug("exiting module root level"
             f"{[d for d in dir() if not d.startswith("__")]}")
