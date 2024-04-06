"""Part of demo of package structure, calculate circle area and circumference.

Being a module within m6_3_package, includes two simple functions to
calculate the area and circumference for a circle with given radius.
"""
"""save this as m6_3_package/circle.py"""

PI = 3.14159265

def circumference (r):
    return r * 2 * PI

def area (r):
    return r**2 * PI
