"""Main script to demo from package import module"""
"""save this as m6_3_3_II.py"""

from m6_3_package.m6_3_2_geometry import circle
#  in m6_3_package __init__.py
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
print("#=1.root level dir()", [d for d in dir() if not d.startswith('__')])
#=1.root level dir() ['circle']

from m6_3_package import m6_3_2_geometry
print("#=2.root level dir()", [d for d in dir() if not d.startswith('__')])
#=2.root level dir() ['circle', 'm6_3_2_geometry']
print(f"#=2.root level {circle is m6_3_2_geometry.circle=}")
#=2.root level circle is m6_3_2_geometry.circle=True

print(f"#=2.root level use obj from package: {m6_3_2_geometry.CONST_1=}")
#=2.root level use obj from package: m6_3_2_geometry.CONST_1='defined in sub package __init__.py'

from m6_3_package import module_1
#  in m_package module_1.py ['var_mod_1']
print("#=3.root level dir()", [d for d in dir() if not d.startswith('__')])
#=3.root level dir() ['circle', 'm6_3_2_geometry', 'module_1']
print("# ", module_1.func_in_mod_1())
#  inside module_1 func_in_mod_1

radius = 3
print(f"# area of {radius=} is {circle.area(radius)}")
# area of radius=3 is 28.27433385

print("#=4.root_level_local_namespace globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=4.root_level_local_namespace globals:
# ('circle', <module 'm6_3_package.m6_3_2_geometry.circle' from '/workspaces/python-book/m6_3_package/m6_3_2_geometry/circle.py'>)
# ('m6_3_2_geometry', <module 'm6_3_package.m6_3_2_geometry' from '/workspaces/python-book/m6_3_package/m6_3_2_geometry/__init__.py'>)
# ('module_1', <module 'm6_3_package.module_1' from '/workspaces/python-book/m6_3_package/module_1.py'>)
# ('radius', 3)