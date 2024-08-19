"""Test functions within this package

Usage:
    python -m m6_3_package.m6_3_2_geometry
"""

if __package__:
    from . import logger
    from .m6_3_2_geometry.rectangle import perimeter
    from .module_1 import func_in_mod_1
    from . import module_2
    logger.debug("running as part of %s, import using relative path.",
                 __package__)
else:
    from __init__ import logger
    from m6_3_2_geometry.rectangle import perimeter
    from module_1 import func_in_mod_1
    import module_2
    logger.debug(" running as script, import using absolute path")
#DEBUG - m6_3_package(__init__.py:26) - m6_3_package/__init__.py Initializing package
#DEBUG - m6_3_2_geometry(__init__.py:29) -     in m6_3_2_package/m6_3_2_geometry/__init__.py, ['CONST_1', 'circle', 'logger', 'logging', 'perimeter', 'rectangle']
#DEBUG - m6_3_package(module_1.py:9) -    m6_3_package/module_1.py root level, ['logger', 'logging', 'var_mod_1']
#DEBUG - m6_3_package(module_2.py:9) -    m6_3_package/module_2.py root level, ['logger', 'logging', 'var_mod_2']
#DEBUG - m6_3_package(m6_3_3_IV.py:19) -  running as script, import using absolute path

logger.info("# testing %s", f"{perimeter(3)=}")
#INFO - m6_3_package(m6_3_3_IV.py:26) - # testing perimeter(3)=12

logger.info("# testing %s", f"{func_in_mod_1()=}")
#INFO - m6_3_package(m6_3_3_IV.py:29) - # testing func_in_mod_1()='func defined in module_1 under m6_3_package'

logger.info("# testing %s", f"{module_2.func_in_mod_2()=}")
#INFO - m6_3_package(m6_3_3_IV.py:32) - # testing module_2.func_in_mod_2()='func defined in module_2 under m6_3_package'
