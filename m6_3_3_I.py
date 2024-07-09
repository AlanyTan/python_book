"""Main script to demo import package"""
"""save this as m6_3_3_I.py"""
import m6_3_package
#  in m6_3_package __init__.py

print("#=1.root level globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=1.root level globals:
# ('m6_3_package', <module 'm6_3_package' from '/workspaces/python-book/m6_3_package/__init__.py'>)
print("#=1.root level dir(m6_3_package)", [d for d in dir(m6_3_package) if not d.startswith('__')])
#=1.root level dir(m6_3_package) ['func_in_init']
print("#=1.root level call func_in_init:", m6_3_package.func_in_init())
#=1.root level call func_in_init: in func_in_init of m6_3_package

import m6_3_package.module_1 as mod_1
#  in m_package module_1.py ['var_mod_1']
print("#=2.root level globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=2.root level globals:
# ('m6_3_package', <module 'm6_3_package' from '/workspaces/python-book/m6_3_package/__init__.py'>)
# ('mod_1', <module 'm6_3_package.module_1' from '/workspaces/python-book/m6_3_package/module_1.py'>)
print("#=2.root level dir(m6_3_package)", [d for d in dir(m6_3_package) if not d.startswith('__')])
#=root level dir(m6_3_package) ['func_in_init', 'module_1']
print("#=2.root level dir(mod_1)", [d for d in dir(mod_1) if not d.startswith('__')])
#=root level dir(mod_1) ['func_in_mod_1', 'var_mod_1']
print(f"#=2.root level {mod_1.func_in_mod_1 is m6_3_package.module_1.func_in_mod_1=}")
#=root level mod_1.func_in_mod_1 is m6_3_package.module_1.func_in_mod_1=True

import m6_3_package.m6_3_2_geometry.circle
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
import m6_3_package.m6_3_2_geometry.rectangle as rect
print("#=3.root level dir(m6_3_package)", [d for d in dir(m6_3_package) if not d.startswith('__')])
#=root level dir(m6_3_package) ['func_in_init', 'm6_3_2_geometry', 'module_1']
print("#==3.package level dir(.m6_3_2_geometry)", 
      [d for d in dir(m6_3_package.m6_3_2_geometry) if not d.startswith('__')])
#==package level dir(.m6_3_2_geometry) ['CONST_1', 'circle', 'rectangle']
print("#===3.subpackage level dir(..circle)", 
      [d for d in dir(m6_3_package.m6_3_2_geometry.circle) if not d.startswith('__')])
#===subpackage level dir(..circle) ['PI', 'area', 'circumference', 'main']

radius = 3
print(f"# area of r={radius} is {m6_3_package.m6_3_2_geometry.circle.area(radius)}")
#area of r=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {rect.perimeter(length)}")
# perimeter of square length=4 is 16
