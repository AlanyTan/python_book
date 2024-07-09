"""Nested Package.

This package shows how to create sub-packages and organize modules using nested packages.

Modules:
    circle: module include functions to calculate area and
            circumference of a circle
    rectangle: module include functions to calculate area
            and perimeter of a rectangle.
    irregular: module as placehold for functions not yet implemented

Usage:
    >>> from m6_3_2_geometry import circle
    >>> circle_area = circle.area(4)
    >>> from m6_3_2_geometry import rectangle
    >>> rect_perimeter = rectangle.perimeter(2,3)
"""
CONST_1='defined in sub package __init__.py'
print("in m6_3_2_geometry/__init__.py", [d for d in dir() if not d.startswith("__")])
def func_in_init() -> str:
    """func defined in sub package __init__.py"""
    return ("inside sub package __init__.py func_in_init()")