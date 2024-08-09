"""Introducing property of class.

Classes:
    Circle: defined by a radius
    Polygon:defined by the length of a series of straight sides
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


class Circle:
    """improved circle class to introduce properties

    Attributes:
        PI(float): (Class Attribute) constant PI used by this class
    """
    PI = 3.14159265
    logger.debug(f"class Circle being defined.")

    @property
    def radius(self) -> int | float:
        """float|int: the radius of the circle, should be >= 0"""
        return self._radius

    @radius.setter
    def radius(self, r: int | float) -> None:
        if r < 0:
            logger.error(
                " class Circle radius property can't be negative {r=}")
            raise ValueError(
                f"can't assign circle with negative {r=}!"
                "a circle's radius has to be >= 0")
        logger.debug(f" class Circle radius property setter called with {r=}")
        self._radius = r

    def __init__(self, r: int | float):
        """Initialize a Circle object

        Args:
            r: the radius of the circle
        """
        logger.debug(f"Circle.__init__() construct a Circle object with {r=}")
        self.radius = r

    def circumference(self) -> float:
        """returns the circumference of this circle"""
        return 2 * self.PI * self.radius

    def area(self) -> float:
        """return the area of this circle"""
        return self.PI * self.radius ** 2


class Polygon:
    """Multi-sides shape class to demo mutable properties"""
    logger.debug(f"class Polygon being defined.")

    @property
    def sides(self) -> list:
        """iterable: each element is a number representing length of a side"""
        return self._sides[:]

    @sides.setter
    def sides(self, s: list[int | float]) -> None:
        longest_side = max(s)
        sum_of_all_sides = sum(s)
        if longest_side <= sum_of_all_sides - longest_side:
            self._sides = list(s)
            logger.debug(f"Polygon.sides setter called with {s=}")
        else:
            logger.error(f"Invalid lenths {s=}, max length {max(s)} violates "
                         "polygon inequality theorem!")
            raise ValueError(f"Invalid lenths {s}! The sum of the "
                             "shorter sides must >= the longest side.")

    def __init__(self, *sides):
        """Construct a polygon using args representing the lengths of n sides

        Args:
            s1, s2, ...: any numbers represent length of the sides
        """
        logger.debug(f"Polygon.__init__() constructing with {sides=}")
        self.sides = sides

    def add_side(self, length: int | float, idx: int = None) -> None:
        """add a new side to Polygon

        Args:
            length: the length of the new side
            idx: the index of where the new side should be inserted in front of
        """
        if length < self.perimeter():
            new_side_idx = len(self.sides) if idx is None else idx
            logger.debug(f"Adding {length=} at {new_side_idx} to {self.sides}")
            self._sides[new_side_idx:new_side_idx] = [length]
        else:
            logger.error(f"{length=}, violates polygon inequality theorem!")
            raise ValueError(f"Invalid lenths {length}! The sum of the "
                             "shorter sides must >= the longest side.")

    def perimeter(self) -> float:
        """return the total length of all sides"""
        return sum(self.sides)

    def area(self) -> float:
        """return the area of the triangle using Heron's formula
        or raise an error for shapes with more sides for insufficient info
        """
        if len(self.sides) == 3:
            half_perimeter = self.perimeter() / 2
            temp_calc = half_perimeter
            for s in self.sides:
                temp_calc *= (half_perimeter - s)

            return (temp_calc) ** (1 / 2)
        else:
            logger.error(f"cannot calculate area of a polygon with "
                         f"{len(self.sides)} sides: {self.sides}")
            raise ValueError("Insuffcient info to calculate the area of a "
                             "polygon with {len(self.sides)} sides.")

    def istriangle(self) -> bool:
        """If there are 3 sides, 3 angles"""
        return len(self.sides) == 3


def main():
    try:
        circle_1 = Circle(1)
        print(f"# {circle_1.PI=}, {circle_1.radius=}, {circle_1.area()=}")

        circle_2 = Circle(2)
        circle_3 = circle_1
        circle_1.radius = 3
        print(f"# {circle_1.radius=}, {circle_2.radius=}, {circle_3.radius=}")

        poly_1 = Polygon(3, 4, 5)
        print(f"# {poly_1.sides=}, {poly_1.istriangle()=}, {poly_1.area()=}")
        poly_1.sides[0] = 5
        poly_1.sides.append(5)
        print(f"# {poly_1.sides=}, {poly_1.istriangle()=}")

        poly_1.add_side(6)
        print(f"# {poly_1.sides=}, {poly_1.istriangle()=}")

        poly_1.sides = [1, 2, 10, 3]

    except ValueError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")


if __name__ == "__main__":
    main()

# DEBUG - __main__(m9_1_3_II.py:21) - class Circle being defined.
# DEBUG - __main__(m9_1_3_II.py:59) - class Polygon being defined.
# DEBUG - __main__(m9_1_3_II.py:45) - Circle.__init__() construct a Circle object with r=1
# DEBUG - __main__(m9_1_3_II.py:36) -  class Circle radius property setter called with r=1
# circle_1.PI=3.14159265, circle_1.radius=1, circle_1.area()=3.14159265
# DEBUG - __main__(m9_1_3_II.py:45) - Circle.__init__() construct a Circle object with r=2
# DEBUG - __main__(m9_1_3_II.py:36) -  class Circle radius property setter called with r=2
# DEBUG - __main__(m9_1_3_II.py:36) -  class Circle radius property setter called with r=3
# circle_1.radius=3, circle_2.radius=2, circle_3.radius=3
# DEBUG - __main__(m9_1_3_II.py:85) - Polygon.__init__() constructing with sides=(3, 4, 5)
# DEBUG - __main__(m9_1_3_II.py:72) - Polygon.sides setter called with s=(3, 4, 5)
# poly_1.sides=[3, 4, 5], poly_1.istriangle()=True, poly_1.area()=6.0
# poly_1.sides=[3, 4, 5], poly_1.istriangle()=True
# DEBUG - __main__(m9_1_3_II.py:97) - Adding length=6 at 3 to [3, 4, 5]
# poly_1.sides=[3, 4, 5, 6], poly_1.istriangle()=False
# ERROR - __main__(m9_1_3_II.py:74) - Invalid lenths s=[1, 2, 10, 3], max length 10 violates polygon inequality theorem!
# ERROR - __main__(m9_1_3_II.py:152) - Invalid lenths [1, 2, 10, 3]! The sum of the shorter sides must >= the longest side. at line 149
