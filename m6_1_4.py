"""
Main script demonstrating importing a module with an alias.
"""
"""save this as m6_1_4.py"""

import m6_1_circle as circle
print(f"# module set PI to: {circle.PI}")
# module set PI to: 3.14159265

radius = 3

print(f"# area of {radius=} is {circle.area(radius)}")
# area of radius=3 is 28.27433385

print(f"# circumference of {radius=} is"
      f" {circle.circumference(radius)}")
# circumference of radius=3 is 18.849555900000002
