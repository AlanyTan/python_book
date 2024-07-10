"""Main script to demo from package.module import func"""
"""save this as m6_3_3_IV.py"""
from m6_3_package.m6_3_2_geometry.circle import area as circle_area
#  in m6_3_package __init__.py
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
from m6_3_package.m6_3_2_geometry.rectangle import perimeter
print("#=1.root_level_local_namespace globals:"
        , *[(k, v) for k, v in globals().items() if not k.startswith('__')]
        , sep='\n# ')
#=1.root_level_local_namespace globals:
# ('circle_area', <function area at 0x7a841f229f80>)
# ('perimeter', <function perimeter at 0x7a841f22b600>)

radius = 3
print(f"# area of {radius=} is {circle_area(radius)}")
# area of radius=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {perimeter(length)}")
# perimeter of square length=4 is 16
