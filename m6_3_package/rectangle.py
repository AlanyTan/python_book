"""Part of demo of package structure, calculate rect area and perimeter.

Being a module within m6_3_package, includes two simple functions to
calculate the area and perimeter for a rectangle with given length and width.
"""
"""save this as m6_3_package/rectangle.py"""

def perimeter (a,b=None):
    if b == None:
        b = a
    return 2*(a+b)

def area (a,b=None):
    if b == None:
        b = a
    return a*b
