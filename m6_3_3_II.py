"""Main script to demo from package import module"""
"""save this as m6_3_3_II.py"""
from m6_3_package import module_1
#  in m6_3_package __init__.py
print("#=root level dir()", [d for d in dir() if not d.startswith('__')])
#=root level dir() ['module_1']

from m6_3_package.m6_3_2_geometry import circle
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
print("#=root level dir()", [d for d in dir() if not d.startswith('__')])
#=root level dir() ['circle', 'module_1']

print("# ", module_1.func_in_mod_1())
#  inside module_1 func_in_mod_1

radius = 3
print(f"# area of {radius=} is {circle.area(radius)}")
# area of radius=3 is 28.27433385

print("#=root_level_local_namespace globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=root_level_local_namespace globals:
# ('module_1', <module 'm6_3_package.module_1' from '/workspaces/python-book/m6_3_package/module_1.py'>)
# ('circle', <module 'm6_3_package.m6_3_2_geometry.circle' from '/workspaces/python-book/m6_3_package/m6_3_2_geometry/circle.py'>)
# ('radius', 3)