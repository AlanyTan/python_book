"""Main script to demo from package import *"""
"""save this as m6_3_3_III.py"""
from m6_3_package import *
#  in m6_3_package __init__.py
#  in m_package module_1.py ['var_mod_1']
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
print("#=root level dir()", [d for d in dir() if not d.startswith('__')])
#=root level dir() ['m6_3_2_geometry', 'module_1']

print("# ", module_1.func_in_mod_1())
#  inside module_1 func_in_mod_1

print("#=root_level_local_namespace globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=root_level_local_namespace globals:
# ('module_1', <module 'm6_3_package.module_1' from '/workspaces/python-book/m6_3_package/module_1.py'>)
# ('m6_3_2_geometry', <module 'm6_3_package.m6_3_2_geometry' from '/workspaces/python-book/m6_3_package/m6_3_2_geometry/__init__.py'>)
