"""Introduce class inheritance using Parallelogram family

Classes:
    Parallelogram: Opposite sides parallel and equal
    Rectangle: opposite sides equal 90 dg angle
"""

from m8_2_2 import get_logger, logging_context as log_to
logger = get_logger(__name__, stream='DEBUG')


class Parallelogram:
    """base class for 4 sides, two parallel pairs

        Parallelogram have a pair of long sides, same length and parallel
        and a pair of short sides, same length and parallel
        The two opposing angles are the same, and the sum of adjacent angles
        is 180 degrees.
    """
    logger.debug("defining class")

    @property
    def long_side(self) -> int | float:
        """int|float: the long_side of the parallelogram, should be >= 0"""
        return self._long_side

    @long_side.setter
    def long_side(self, l: int | float) -> None:
        if l < 0:
            logger.error("Parallelogram.long_side setter: invalid length %s!",
                         l)
            raise ValueError(f"Provided {l=} is negative,"
                             "a parallelogram sides need to be >= 0")
        elif l < self._short_side:
            logger.warning("Parallelogram.long_side setter: called with %s"
                           "< %s, swapping...", l, self.short_side)
            self._long_side = self.short_side
            self._short_side = l
        else:
            logger.debug("Parallelogram setter: called with l=%s", l)
            self._long_side = l

    @property
    def short_side(self) -> int | float:
        """int|float: the short_side of the parallelogram, should be >= 0"""
        return self._short_side

    @short_side.setter
    def short_side(self, s: int | float) -> None:
        if s < 0:
            logger.error(
                "Parallelogram setter: invalid length s=%s", s)
            raise ValueError(f"Provided {s=} is negative,"
                             "a parallelogram sides need to be >= 0")
        elif self._long_side < s:
            logger.warning("Parallelogram setter: called with s=%s"
                           "> %s, swapping...", s, self.long_side)
            self._long_side = self._short_side
            self.short_side = s
        else:
            logger.debug("Parallelogram setter: called with s=%s", s)
            self._short_side = s

    @property
    def acute_angle(self) -> int | float:
        """int|float: the sharper angle in degrees"""
        return self._acute_angle

    @acute_angle.setter
    def acute_angle(self, aa: int | float) -> None:
        if 0 <= aa <= 90:
            logger.debug("Parallelogram setter: called with aa=%s", aa)
            self._acute_angle = aa
            self._obtuse_angle = 180 - aa
        else:
            logger.error("Parallelogram setter: invalid angle aa=%s", aa)
            raise ValueError(f"Provided {aa=} is invalid, "
                             f"acute angle should be between 0 and 90 degrees")

    @property
    def obtuse_angle(self) -> int | float:
        """int|float: the obtuse angle in degrees"""
        return self._obtuse_angle

    @obtuse_angle.setter
    def obtuse_angle(self, oa: int | float) -> None:
        if 90 <= oa <= 180:
            logger.debug("Parallelogram setter: called with oa=%s", oa)
            self._obtuse_angle = oa
            self._acute_angle = 180 - oa
        else:
            logger.error("Parallelogram setter: invalid angle oa=%s", oa)
            raise ValueError(f"Provided {oa=} is invalid, obtuse angle "
                             f" should be between 90 and 180 degrees")

    def __init__(self, l: int | float, s: int | float,
                 aa: int | float, oa: int | float | None = None):
        """Construct a parallogram object

        Args:
            l: the length of the long sides
            s: the length of the short sides
            aa: the degrees of the acute angle
            oa: the degrees of the obtuse angle (optional)
        """
        logger.debug("Parallelogram constructor called")
        self._short_side = -1
        self.long_side = max(l, s)
        self.short_side = min(l, s)
        if oa is None or oa + aa == 180:
            self.acute_angle = aa if aa <= 90 else 180 - aa
        else:
            logger.debug("Parallelogram: invalue angles %s, %s", aa, oa)
            raise ValueError(f"Provided {aa=}+{oa=} do not equal 180. Parallel"
                             f"ogram require sum of the two angles to be 180.")

    def perimeter(self) -> float:
        """returns the sum of all four sides"""
        return 2 * (self.long_side + self.short_side)

    def height(self) -> float:
        """return the height against the long_side"""
        import math
        logger.debug("- Parallelogram.height() calculated using sin()")
        return math.sin(math.radians(self.acute_angle)) * self.short_side

    def area(self) -> float:
        """return the area calculated by long_side*height"""
        return self.long_side * self.height()


class Rectangle(Parallelogram):
    """Rectangle class inherited from Parallelogram

    All angels are always 90 degrees."""
    logger.debug("defining class based on Parallelogram")

    def __init__(self, l: int | float, s: int | float):
        """Construct a Rectangle object"""
        logger.debug("Rectangle constructor called")
        super().__init__(l, s, 90)

    def height(self) -> int | float:
        logger.debug("Rectangle.height() return short_side directly")
        return self.short_side


def main():
    """main func for demo simplest classes"""
    try:
        para_1 = Parallelogram(3, 4, 30)
        print(f"# {para_1.area()=}")

        rect_1 = Rectangle(3, 4)
        print(f"# {rect_1.area()=}")

    except ValueError as e:
        logger.error("%r at line %s", e, e.__traceback__.tb_lineno)
        print("# ERROR:", e)


if __name__ == "__main__":
    with log_to("main", stream=False):
        main()

#    DEBUG - m9_2_1_I.py:20 __main__.Parallelogram() - defining class
#    DEBUG - m9_2_1_I.py:136 __main__.Rectangle() - defining class based on Parallelogram
#    DEBUG - m9_2_1_I.py:106 __main__.__init__() - Parallelogram constructor called
#    DEBUG - m9_2_1_I.py:40 __main__.long_side() - Parallelogram setter: called with l=4
#    DEBUG - m9_2_1_I.py:61 __main__.short_side() - Parallelogram setter: called with s=3
#    DEBUG - m9_2_1_I.py:72 __main__.acute_angle() - Parallelogram setter: called with aa=30
#    DEBUG - m9_2_1_I.py:124 __main__.height() - - Parallelogram.height() calculated using sin()
# para_1.area()=5.999999999999999
#    DEBUG - m9_2_1_I.py:140 __main__.__init__() - Rectangle constructor called
#    DEBUG - m9_2_1_I.py:106 __main__.__init__() - Parallelogram constructor called
#    DEBUG - m9_2_1_I.py:40 __main__.long_side() - Parallelogram setter: called with l=4
#    DEBUG - m9_2_1_I.py:61 __main__.short_side() - Parallelogram setter: called with s=3
#    DEBUG - m9_2_1_I.py:72 __main__.acute_angle() - Parallelogram setter: called with aa=90
#    DEBUG - m9_2_1_I.py:144 __main__.height() - Rectangle.height() return short_side directly
# rect_1.area()=12
