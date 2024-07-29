"""Introduce __eq__, __lt__, and @total_ordering

Classes:
    Rectangle: opposite sides equal 90 dg angle
    Square: all 4 sides same length, all angles 90 degrees
"""

from functools import total_ordering
import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)
from m9_2_1_I import Parallelogram

@total_ordering
class Rectangle(Parallelogram):
    """Rectangle class ingerited from Parallelogram

    All angels are always 90 degrees."""
    def __init__(self, l: int|float, s: int|float):
        """initialize a Rectangle object

        Args:
            l: length of long sides
            s: length of short sides
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__(l, s, 90)

    def height(self) -> int|float:
        return self.short_side

    def __repr__(self) -> str:
        """return string representation of Rectangle"""
        return f"Rectangle({self.long_side}, {self.short_side})"

    def __eq__(self, other) -> bool:
        """compare area of 2 Rectangle objects"""
        return self.area() == other.area()

    def __lt__(self, other) -> bool:
        """compare area of 2 Rectangle objects"""
        return self.area() < other.area()
    

class Square(Rectangle):
    """Square, inherited from Rectangle AND Rhombus"""
    def __init__(self, l: int|float):
        """initialize a square object

        Args:
            l: length of sides
        """
        super().__init__(l, l)

    def __str__(self):
        """return text desc of Square"""
        return f"Square({self.long_side})"


def main():
    rect_1 = Rectangle(3, 4)
    rect_2 = Rectangle(2, 8)
    sq_1 = Square(4)
    try:
        print(f"# {sq_1} == {rect_2}: {sq_1 == rect_2}")
        print(f"# {rect_1} > {rect_2}: {rect_1 > rect_2}")
        print(f"# {sq_1} == {rect_2} >= {rect_1}: {sq_1 == rect_2 >= rect_1}")
    except ValueError as e:
        logger.error(f"{e} as line {e.__traceback__.tb_lineno}")

if __name__ == "__main__":
    main()

# Square(4) == Rectangle(8, 2): True
# Rectangle(4, 3) > Rectangle(8, 2): False
# Square(4) == Rectangle(8, 2) >= Rectangle(4, 3): True
