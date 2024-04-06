"""Main script to demo from package.module import func"""
"""save this as m6_3_3_IV.py"""
from m6_3_package.circle import area as circle_area
from m6_3_package.rectangle import perimeter

radius = 3

print(f"# area of {radius=} is {circle_area(radius)}")
# area of radius=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {perimeter(length)}")
# perimeter of square length=4 is 16
