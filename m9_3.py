"""demo help documentation for modules with class"""

import m9_2_5


def main() -> None:
    """print out docstring of two classes"""
    print('"""')
    help(m9_2_5.Polygon)
    help(m9_2_5.Rectangle)
    print('"""')


if __name__ == "__main__":
    main()

"""
Help on class Polygon in module m9_2_5:

class Polygon(Shape)
 |  -second abstract class, inherited from Shape, multiple straight sides
 |
 |  Method resolution order:
 |      Polygon
 |      Shape
 |      abc.ABC
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __repr__(self) -> str
 |      return the string representation of self
 |
 |  perimeter(self) -> float
 |      override method return sum of length of all sides
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties defined here:
 |
 |  logger
 |      logger: regular property return a logger named after the class
 |
 |  no_of_sides
 |      abstract property # of sides in this polygon
 |
 |  sides
 |      abstract property - tuple of length of all sides
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset({'area', 'no_of_sides', 'sides'})
 |
 |  __annotations__ = {'_logger': logging.Logger | None}
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Shape:
 |
 |  area(self) -> float
 |      abstract method for culculating area of the shape
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Shape:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object


Help on class Rectangle in module m9_2_5:

class Rectangle(Quadrilateral)
 |  Rectangle(l: int | float, s: int | float)
 |
 |  -two opposing sides equal, all angles 90
 |
 |  Method resolution order:
 |      Rectangle
 |      Quadrilateral
 |      Polygon
 |      Shape
 |      abc.ABC
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self, l: int | float, s: int | float)
 |      regular constructor
 |
 |  area(self) -> float
 |      override method return product of adjacent two sides
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  sides
 |      tuple: override property - store length of all sides
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __abstractmethods__ = frozenset()
 |
 |  __annotations__ = {}
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from Quadrilateral:
 |
 |  no_of_sides
 |      override property set no_of_sides to 4
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from Polygon:
 |
 |  __repr__(self) -> str
 |      return the string representation of self
 |
 |  perimeter(self) -> float
 |      override method return sum of length of all sides
 |
 |  ----------------------------------------------------------------------
 |  Readonly properties inherited from Polygon:
 |
 |  logger
 |      logger: regular property return a logger named after the class
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from Shape:
 |
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object
"""
