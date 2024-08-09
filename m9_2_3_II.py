"""Introduce __add__ overloading

Classes:
    Rectangle: opposite sides equal 90 dg angle
    Square: all 4 sides same length, all angles 90 degrees
"""

import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m9_2_1_I import Parallelogram


class Rectangle(Parallelogram):
    """Rectangle, ingerited from Parallelogram all angels are 90 degrees."""

    def __init__(self, l: int | float, s: int | float):
        """initialize a Rectangle object

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
        return f"Rectangle({self.long_side}, {self.short_side})"

    def __add__(self, other):
        """Overloading '+' add two Rectangles if at least one side equal"""
        sl = self.long_side
        ss = self.short_side
        ol = other.long_side
        os = other.short_side
        if sl == ol:
            return Rectangle(sl, ss + os)
        elif sl == os:
            return Rectangle(sl, ss + ol)
        elif ss == ol:
            return Rectangle(ss, sl + os)
        elif ss == os:
            return Rectangle(ss, sl + ol)
        else:
            self.logger.error(f"cannot add {self} and {other}, "
                              "no sides are equal")
            raise ValueError(f"none of the sides of {self} and {other} are "
                             "equal, can't add.")

    def __iadd__(self, other):
        """Overloading '+=' add two Rectangles if at least one side equal"""
        sl = self.long_side
        ss = self.short_side
        ol = other.long_side
        os = other.short_side
        if sl == ol:
            self.short_side = ss + os
        elif sl == os:
            self.short_side = ss + ol
        elif ss == ol:
            self.long_side = sl + os
        elif ss == os:
            self.long_side = sl + ol
        else:
            self.logger.error(f"cannot add {self} and {other}, "
                              "no sides are equal")
            raise ValueError(f"none of the sides of {self} and {other} are "
                             "equal, can't add.")
        return self


class Square(Rectangle):
    """Square, inherited from Rectangle AND Rhombus"""

    def __init__(self, l: int | float):
        """initialize a square object

        Args:
            l: length of sides
        """
        super().__init__(l, l)

    def __str__(self):
        """return text desc of Square"""
        return f"Square({self.long_side})"

    def __iadd__(self, other):
        sl = self.long_side
        ss = self.short_side
        ol = other.long_side
        os = other.short_side
        if ol in [sl, ss, 0] and os == 0:
            return self
        else:
            self.logger.error(f"adding a non-zero {other} rectangle to {self}"
                              " will make it a non-square rectangle!")
            raise TypeError(f"Self-add result won't be a Square: adding {other}"
                            f" onto {self} resulting in non-square.")


def main():
    rect_1 = Rectangle(3, 4)
    rect_2 = Rectangle(7, 5)
    sq_1 = Square(3)
    try:
        print(f"# {sq_1 + rect_1}")
        print(f"# {sq_1 + rect_1 + rect_2}")
        print(f"# {sq_1 + rect_2 + rect_1}")
    except ValueError as e:
        logger.error(f"{e} line {e.__traceback__.tb_lineno}")

    try:
        rect_1_alias = rect_1
        rect_1 += sq_1
        print(f"# {rect_1=}, {rect_1_alias is rect_1=}")

        sq_1 += rect_1
    except TypeError as e:
        logger.error(f"{e} line {e.__traceback__.tb_lineno}")


if __name__ == "__main__":
    main()

# Rectangle(7, 3)
# Rectangle(8, 7)
# ERROR - Square(m9_2_3_II.py:52) - cannot add Square(3) and Rectangle(7, 5), no sides are equal
# ERROR - __main__(m9_2_3_II.py:117) - none of the sides of Square(3) and Rectangle(7, 5) are equal, can't add. line 115
# rect_1=Rectangle(7, 3), rect_1_alias is rect_1=True
# ERROR - Square(m9_2_3_II.py:102) - adding a non-zero Rectangle(7, 3) rectangle to Square(3) will make it a non-square rectangle!
# ERROR - __main__(m9_2_3_II.py:126) - Self-add result won't be a Square: adding Rectangle(7, 3) onto Square(3) resulting in non-square. line 124
