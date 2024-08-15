"""Main script to demo from package import *"""
"""save this as m6_3_3_III.py"""

from m6_3_package import *
#DEBUG - m6_3_package(__init__.py:26) - m6_3_package/__init__.py Initializing package
#DEBUG - m6_3_package(module_1.py:9) -    m6_3_package/module_1.py root level, ['logger', 'logging', 'var_mod_1']
#DEBUG - m6_3_2_geometry(__init__.py:29) -     in m6_3_2_package/m6_3_2_geometry/__init__.py, ['CONST_1', 'circle', 'logger', 'logging', 'perimeter', 'rectangle']

print("#=root level dir()", [d for d in dir() if not d.startswith('__')])
#=root level dir() ['m6_3_2_geometry', 'module_1']

print("# ", module_1.func_in_mod_1())
#  func defined in module_1 under m6_3_package

print("#", m6_3_2_geometry.CONST_1)
# defined in sub package __init__.py

print("#=root_level_local_namespace globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=root_level_local_namespace globals:
# ('module_1', <module 'm6_3_package.module_1' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\module_1.py'>)
# ('m6_3_2_geometry', <module 'm6_3_package.m6_3_2_geometry' from 'C:\\Users\\user\\Documents\\python_book\\m6_3_package\\m6_3_2_geometry\\__init__.py'>)
