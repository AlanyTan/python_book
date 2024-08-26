"""Introduce __eq__, __lt__, and @total_ordering

Classes:
    Rectangle: opposite sides equal 90 dg angle
    Square: all 4 sides same length, all angles 90 degrees
"""

from functools import total_ordering
from m8_2_2 import get_logger, logging_context as log_to
from m9_2_1_I import Parallelogram, logger as logger_m9_2_1_I
logger_m9_2_1_I.setLevel('INFO')


@total_ordering
class Rectangle(Parallelogram):
    """Rectangle class ingerited from Parallelogram

    All angels are always 90 degrees."""

    def __init__(self, l: int | float, s: int | float):
        """initialize a Rectangle object

        Args:
            l: length of long sides
            s: length of short sides
        """
        self.logger = get_logger(self.__class__.__name__)
        super().__init__(l, s, 90)

    def height(self) -> int | float:
        """overriding height method to return short_side directly."""
        return self.short_side

    def __repr__(self) -> str:
        """return string representation of Rectangle"""
        return f"Rectangle({self.long_side}, {self.short_side})"

    def __eq__(self, other) -> bool:
        """compare area of 2 Rectangle objects"""
        self.logger.info("__eq__ called to compare %s and %s", self, other)
        return self.area() == other.area()

    def __lt__(self, other) -> bool:
        """compare area of 2 Rectangle objects"""
        self.logger.info("__lt__ called to compare %s and %s", self, other)
        return self.area() < other.area()


class Square(Rectangle):
    """Square, inherited from Rectangle only"""

    def __init__(self, l: int | float) -> None:
        """initialize a square object

        Args:
            l: length of sides
        """
        super().__init__(l, l)

    def __str__(self):
        """return text desc of Square"""
        return f"Square({self.long_side})"


def main() -> None:
    """demonstrate comparison overloading"""
    rect_1 = Rectangle(3, 4)
    rect_2 = Rectangle(2, 8)
    sq_1 = Square(4)
    try:
        print(f"# {sq_1} == {rect_2}: {sq_1 == rect_2}")
        print(f"# {rect_1} > {rect_2}: {rect_1 > rect_2}")
        print(f"# {sq_1} == {rect_2} >= {rect_1}: {sq_1 == rect_2 >= rect_1}")
    except ValueError as e:
        logger.error("%r as line %s", e, e.__traceback__.tb_lineno)


if __name__ == "__main__":
    with log_to("main") as logger:
        main()

#    DEBUG - m9_2_1_I.py:20 m9_2_1_I.Parallelogram() - defining class
#    DEBUG - m9_2_1_I.py:136 m9_2_1_I.Rectangle() - defining class based on Parallelogram
#     INFO - m9_2_3_III.py:40 Square.__eq__() - __eq__ called to compare Square(4) and Rectangle(8, 2)
# Square(4) == Rectangle(8, 2): True
#     INFO - m9_2_3_III.py:45 Rectangle.__lt__() - __lt__ called to compare Rectangle(4, 3) and Rectangle(8, 2)
# Rectangle(4, 3) > Rectangle(8, 2): False
#     INFO - m9_2_3_III.py:40 Square.__eq__() - __eq__ called to compare Square(4) and Rectangle(8, 2)
#     INFO - m9_2_3_III.py:45 Rectangle.__lt__() - __lt__ called to compare Rectangle(8, 2) and Rectangle(4, 3)
# Square(4) == Rectangle(8, 2) >= Rectangle(4, 3): True
#     INFO - m8_2_2.py:67 main.logging_context() - shutting down the logging facility...
