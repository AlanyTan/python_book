"""Main script to demo import package"""
"""save this as m6_3_3_I.py"""
import m6_3_package
#  in m6_3_package __init__.py

print("#=root_level_local_namespace globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=root_level_local_namespace globals:
# ('m6_3_package', <module 'm6_3_package' from '/workspaces/python-book/m6_3_package/__init__.py'>)

print("#=root level dir(m6_3_package)", [d for d in dir(m6_3_package) if not d.startswith('__')])
#=root level dir(m6_3_package) ['m6_3_package']
print("#=root level", m6_3_package.func_in_init())
#=root level in func_in_init of m6_3_package

import m6_3_package.m6_3_2_geometry.circle
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
import m6_3_package.m6_3_2_geometry.rectangle as rect
print("#=root level dir(m6_3_package)", [d for d in dir(m6_3_package) if not d.startswith('__')])
#=root level dir(m6_3_package) ['func_in_init', 'm6_3_2_geometry']
print("#==package level dir(.m6_3_2_geometry)", 
      [d for d in dir(m6_3_package.m6_3_2_geometry) if not d.startswith('__')])
#==package level dir(.m6_3_2_geometry) ['CONST_1', 'circle', 'rectangle']
print("#===subpackage level dir(..circle)", 
      [d for d in dir(m6_3_package.m6_3_2_geometry.circle) if not d.startswith('__')])
#===subpackage level dir(..circle) ['PI', 'area', 'circumference', 'main']

radius = 3
print(f"# area of r={radius} is {m6_3_package.m6_3_2_geometry.circle.area(radius)}")
#area of r=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {rect.perimeter(length)}")
# perimeter of square length=4 is 16
