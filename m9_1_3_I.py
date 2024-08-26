"""Introducing attribute and constructor

Classes:
    Circle: defined by a radius
"""

from m8_2_2 import get_logger, logging_context as log_to
logger = get_logger(__name__, stream='DEBUG')


class Circle:
    """a better Circle class with attributes and constructor

    defines radius as an object attribute, calc area and circumference from it

    Attributes:
        PI (float): Class attribute for the constant PI
        radius(float): instance attribute represents the radius of the circle
    """

    PI = 3.14159265
    logger.debug("class attribute PI=%r", PI)

    def __init__(self, r: int | float):
        """Initialize Circle object with given args

        Args:
            r: the radius of the circle
        """
        if r < 0:
            logger.error(" class Circle init can't create circle "
                         "with negative radius %r!", r)
            raise ValueError(
                f"can't create circle with negative {r=}!"
                "a circle's radius has to be >= 0")
        logger.debug("creating circle with %r...", r)
        self.radius = r

    def circumference(self) -> float:
        """calculate circumference by 2*PI*self.radius"""
        logger.debug(" calculating Circle circumference...")
        return 2 * self.PI * self.radius

    def area(self) -> float:
        """calculate area of this by PI*self.radius**2"""
        logger.debug(" calculating Circle area...")
        return self.PI * self.radius**2


def main() -> None:
    """demo class with constructor"""
    try:
        circle_1 = Circle(1)
        print(f"# {circle_1.PI=}, {circle_1.radius=}")
        print(f"# {circle_1.circumference()=}")
        print(f"# {circle_1.area()=}")

        circle_2 = Circle(2)
        Circle.PI = 3.14
        print(f"# {Circle.PI=}, {circle_1.PI=}, {circle_2.PI=}")

        circle_3 = Circle(-1)
    except ValueError as e:
        logger.error("%r at line %s", e, e.__traceback__.tb_lineno)


if __name__ == "__main__":
    with log_to("main", stream=False):
        main()

#    DEBUG - m9_1_3_I.py:22 __main__.Circle() - class attribute PI=3.14159265
#    DEBUG - m9_1_3_I.py:36 __main__.__init__() - creating circle with 1...
# circle_1.PI=3.14159265, circle_1.radius=1
#    DEBUG - m9_1_3_I.py:41 __main__.circumference() -  calculating Circle circumference...
# circle_1.circumference()=6.2831853
#    DEBUG - m9_1_3_I.py:46 __main__.area() -  calculating Circle area...
# circle_1.area()=3.14159265
#    DEBUG - m9_1_3_I.py:36 __main__.__init__() - creating circle with 2...
# Circle.PI=3.14, circle_1.PI=3.14, circle_2.PI=3.14
#    ERROR - m9_1_3_I.py:31 __main__.__init__() -  class Circle init can't create circle with negative radius -1!
#    ERROR - m9_1_3_I.py:64 __main__.main() - ValueError("can't create circle with negative r=-1!a circle's radius has to be >= 0") at line 62
