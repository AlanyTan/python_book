"""Main script to demo from package.module import func"""
"""save this as m6_3_3_IV.py"""
from m6_3_package.m6_3_2_geometry.circle import area as circle_area
#  in m6_3_package __init__.py
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
from m6_3_package.m6_3_2_geometry.rectangle import perimeter
c#=root level dir() ['circle_area', 'perimeter']

radius = 3
print(f"# area of {radius=} is {circle_area(radius)}")
# area of radius=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {perimeter(length)}")
# perimeter of square length=4 is 16
