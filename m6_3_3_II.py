"""Main script to demo from package import module"""
"""save this as m6_3_3_II.py"""
from m6_3_package import circle, rectangle as rect
radius = 3

print(f"# area of {radius=} is {circle.area(radius)}")
# area of radius=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {rect.perimeter(length)}")
# perimeter of square length=4 is 16
