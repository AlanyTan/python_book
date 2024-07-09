"""Part of demo of package structure, calculate rect area and perimeter.

Functions:
    perimeter(a, [b]): calculate the perimeter for a rectangle with given length a and width b.
    area(a, [b]): calculate the area for a rectangle with given length a and width b.
"""
"""save this as m6_3_package/m6_3_2_geometry/rectangle.py"""

def perimeter (a: int|float,b: int|float=None) -> int|float:
    """calculate rectangle perimeter

    Args:
        a: the length of the rectangle
        b: the width of the rectable, optional, if ommited, this is a square
    """
    if b == None:
        b = a
    return 2*(a+b)

def area (a: int|float,b: int|float=None) -> int|float:
    """calculate rectangle perimeter

    Args:
        a: the length of the rectangle
        b: the width of the rectable, optional, if ommited, this is a square
    """
    if b == None:
        b = a
    return a*b
