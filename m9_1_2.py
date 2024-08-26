"""Introduction to classes - rudamentary Circle

Classes:
    Circle: defined by a radius
"""

from m8_2_2 import get_logger, logging_context as log_to
logger = get_logger(__name__, stream='DEBUG')


class Circle:
    """rudamentary Circle class to introduce class and methods"""
    PI = 3.14159265
    logger.debug("class Circle root level attribute PI=%s", PI)

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
    """demonstrate basic class"""
    logger.debug("main: defining circle_1")
    circle_1 = Circle()
    logger.debug("main: calling circle_1.circumference(2)")
    print(f"# {circle_1.circumference(2)=}")


if __name__ == "__main__":
    with log_to("main", stream=False):
        main()

#    DEBUG - m9_1_2.py:14 __main__.Circle() - class Circle root level attribute PI=3.14159265
#    DEBUG - m9_1_2.py:30 __main__.main() - main: defining circle_1
#    DEBUG - m9_1_2.py:32 __main__.main() - main: calling circle_1.circumference(2)
#    DEBUG - m9_1_2.py:24 __main__.circumference() -  class Circle method circumference()
# circle_1.circumference(2)=12.5663706
