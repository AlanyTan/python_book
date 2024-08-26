"""Introduce __str__ and __repr__

Classes:
    Rectangle: opposite sides equal 90 dg angle
    Square: all 4 sides same length, all angles 90 degrees
"""

from m8_2_2 import get_logger, logging_context as log_to
from m9_2_1_I import Parallelogram, logger
logger.setLevel('INFO')


class Rectangle(Parallelogram):
    """Rectangle, ingerited from Parallelogram all angels are 90 degrees."""

    def __init__(self, l: int | float, s: int | float) -> None:
        """Construct a Rectangle object

        Args:
            l: length of long sides
            s: length of short sides
        """
        self.logger = get_logger(self.__class__.__name__)
        super().__init__(l, s, 90)

    def height(self) -> int | float:
        """Overriding height to just return short_side"""
        return self.short_side

    def __repr__(self) -> str:
        """return string representation of Rectangle"""
        self.logger.info("repr() is called.")
        return f"Rectangle({self.long_side}, {self.short_side})"


class Square(Rectangle):
    """Square, inherited from Rectangle all sides same length"""

    def __init__(self, l: int | float) -> None:
        """Construct a square object

        Args:
            l: length of sides
        """
        super().__init__(l, l)

    def __str__(self):
        """return text desc of Square"""
        self.logger.info("str() is called.")
        return f"Square({self.long_side})"


def main() -> None:
    """demonstrate repr and str overloading"""
    rect_1 = Rectangle(3, 4)
    print(f"# {str(rect_1)=}, {repr(rect_1)=}")

    sq_1 = Square(5)
    print(f"# {sq_1}, {sq_1=}")


if __name__ == "__main__":
    with log_to("main", stream=False):
        main()

#    DEBUG - m9_2_1_I.py:20 m9_2_1_I.Parallelogram() - defining class
#    DEBUG - m9_2_1_I.py:136 m9_2_1_I.Rectangle() - defining class based on Parallelogram
#     INFO - m9_2_3_I.py:32 Rectangle.__repr__() - repr() is called.
#     INFO - m9_2_3_I.py:32 Rectangle.__repr__() - repr() is called.
# str(rect_1)='Rectangle(4, 3)', repr(rect_1)='Rectangle(4, 3)'
#     INFO - m9_2_3_I.py:49 Square.__str__() - str() is called.
#     INFO - m9_2_3_I.py:32 Square.__repr__() - repr() is called.
# Square(5), sq_1=Rectangle(5, 5)
