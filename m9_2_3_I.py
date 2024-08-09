"""Introduce __str__ and __repr__

Classes:
    Rectangle: opposite sides equal 90 dg angle
    Square: all 4 sides same length, all angles 90 degrees
"""

import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
from m9_2_1_I import Parallelogram


class Rectangle(Parallelogram):
    """Rectangle, ingerited from Parallelogram all angels are 90 degrees."""

    def __init__(self, l: int | float, s: int | float):
        """Construct a Rectangle object

        Args:
            l: length of long sides
            s: length of short sides
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__(l, s, 90)

    def height(self) -> int | float:
        """Overriding height to just return short_side"""
        return self.short_side

    def __repr__(self) -> str:
        """return string representation of Rectangle"""
        self.logger.info(f"__repr__() called.")
        return f"Rectangle({self.long_side}, {self.short_side})"


class Square(Rectangle):
    """Square, inherited from Rectangle all sides same length"""

    def __init__(self, l: int | float):
        """Construct a square object

        Args:
            l: length of sides
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__(l, l)

    def __str__(self):
        """return text desc of Square"""
        self.logger.info(f"__str__()called.")
        return f"Square({self.long_side})"


def main():
    rect_1 = Rectangle(3, 4)
    print(f"# {str(rect_1)=}, {repr(rect_1)=}")

    sq_1 = Square(5)
    print(f"# {sq_1}, {sq_1=}")


if __name__ == "__main__":
    main()

# INFO - Rectangle(m9_2_3_I.py:33) - __repr__() called.
# INFO - Rectangle(m9_2_3_I.py:33) - __repr__() called.
# str(rect_1)='Rectangle(4, 3)', repr(rect_1)='Rectangle(4, 3)'
# INFO - Square(m9_2_3_I.py:51) - __str__()called.
# INFO - Square(m9_2_3_I.py:33) - __repr__() called.
# Square(5), sq_1=Rectangle(5, 5)
