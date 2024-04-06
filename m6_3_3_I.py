"""Main script to demo import package.module"""
"""save this as m6_3_3_I.py"""
import m6_3_package.circle, m6_3_package.rectangle as rect

radius = 3

print(f"# area of r={radius} is {m6_3_package.circle.area(radius)}")
#area of r=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is {rect.perimeter(length)}")
# perimeter of square length=4 is 16
