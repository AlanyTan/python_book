"""Introduction to classes - rudamentary Circle

Classes:
    Circle: defined by a radius
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s "
                    "- %(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


class Circle:
    """rudamentary Circle class to introduce class and methods"""
    PI = 3.14159265
    logger.debug(f"class Circle root level attribute {PI=}")

    def circumference(self, radius: int | float) -> float:
        """calculate circumference by 2*PI*r

        Args:
            radius: the radius of the circle
        Returns:
            the circumference of the circle
        """
        logger.debug(" class Circle method circumference()")
        return 2 * self.PI * radius


def main():
    logger.debug("main: defining circle_1")
    circle_1 = Circle()
    logger.debug("main: calling circle_1.circumference(2)")
    print(f"# {circle_1.circumference(2)=}")


if __name__ == "__main__":
    main()

# DEBUG - __main__(m9_1_2.py:16) - class Circle root level attribute PI=3.14159265
# DEBUG - __main__(m9_1_2.py:31) - main: defining circle_1
# DEBUG - __main__(m9_1_2.py:33) - main: calling circle_1.circumference(2)
# DEBUG - __main__(m9_1_2.py:26) -  class Circle method circumference()
# circle_1.circumference(2)=12.5663706
