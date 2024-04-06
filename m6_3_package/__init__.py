"""Learning Python Package.

This package provides basic concepts of how Python package
and its modules are organized.

Modules:
    circle: module include functions to calculate area and
            circumference of a circle
    rectangle: module include functions to calculate area
            and perimeter of a rectangle.

Usage:
    >>> from m6_3_package import circle
    >>> circle_area = circle.area(4)
    >>> from m6_3_package import rectangle
    >>> rect_perimeter = rectangle.perimeter(2,3)

For more details on each module, refer to the module docstring.
"""

from . import circle, rectangle

__all__ = ["circle", "rectangle"]
