"""Demo Abstract Base Class definition and usage

Class:
    Shape: abc, with premiter(), area()
    Polygon: abc, with premiter(), area() and sides property
    Quadrilateral: abc, sintermediate class
    Rectangle: normal class
"""

from abc import ABC, abstractmethod
from logging import Logger
from m8_2_2 import get_logger, logging_context as log_to


class Shape(ABC):
    """-first base Abstract Base Class of Shapes"""
    @abstractmethod
    def area(self) -> float:
        """abstract method for culculating area of the shape"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """abstract method for calculating perimeter of the shape"""
        pass


class Polygon(Shape):
    """-second abstract class, inherited from Shape, multiple straight sides"""
    _logger: Logger | None = None

    @property
    def logger(self) -> Logger:
        """logger: regular property return a logger named after the class"""
        if self.__class__._logger is None:
            self.__class__._logger = get_logger(self.__class__.__name__,
                                                stream="DEBUG")
        return self.__class__._logger

    @property
    @abstractmethod
    def sides(self) -> tuple:
        """abstract property - tuple of length of all sides"""
        pass

    @property
    @abstractmethod
    def no_of_sides(self) -> int:
        """abstract property # of sides in this polygon"""
        pass

    def perimeter(self) -> float:
        """override method return sum of length of all sides"""
        return sum(self.sides)

    def __repr__(self) -> str:
        """return the string representation of self"""
        self.logger.debug("representing sides %s as string", self.sides)
        return f"{self.__class__.__name__}{self.sides}"


class Triangle(Polygon):
    """first concrete class (rudamentary Triangle)"""
    @property
    def no_of_sides(self) -> int:
        """override property set no_of_sides to 3"""
        return 3

    @property
    def sides(self) -> tuple[int | float, int | float, int | float]:
        """provide setter for overriden sides property"""
        return self._sides

    @sides.setter
    def sides(self, s: tuple[int | float, int | float, int | float]) -> None:
        if len(s) == 3:
            self._sides = s
        else:
            self.logger.error("%r does not have %s sides to form a Triangle",
                              s, self.no_of_sides)
            raise ValueError(f"{s} does not have 3 sides")

    def area(self) -> float:
        """override to implement method area"""
        half_perimeter = self.perimeter() / 2
        temp_calc = half_perimeter
        for s in self.sides:
            temp_calc *= (half_perimeter - s)

        return (temp_calc) ** (1 / 2)

    def __init__(self, a: int | float, b: int | float, c: int | float) -> None:
        """constructing a Triangle"""
        self.logger.debug("constructing Triangle with %s, %s, %s", a, b, c)
        self.sides = (a, b, c)


class Quadrilateral(Polygon):
    """third abstract class, still have abstract methods not implemented"""
    @property
    def no_of_sides(self) -> int:
        """override property set no_of_sides to 4"""
        return 4


class Rectangle(Quadrilateral):
    """-two opposing sides equal, all angles 90"""
    @property
    def sides(self) -> tuple:
        """tuple: override property - store length of all sides"""
        return tuple(self._sides)

    @sides.setter
    def sides(self, s: tuple[int | float, int | float,
                             int | float, int | float]) -> None:
        if len(s) == 4 and s[0] == s[2] and s[1] == s[3]:
            self._sides = list(s)
        else:
            self.logger.error(f"given {s} can't form a rectangle.")
            raise ValueError(f"{s} do not meet rectangle sides requirement.")

    def area(self) -> float:
        """override method return product of adjacent two sides"""
        return self.sides[0] * self.sides[1]

    def __init__(self, l: int | float, s: int | float):
        """regular constructor"""
        self.sides = ((l, s, l, s))


def main():
    """demo Shape, Quadrilater are abstract; Rectangle can be instantiated"""
    shapes = []
    try:
        shape_1 = Shape()
    except TypeError as e:
        logger.error("%r at line %s", e, e.__traceback__.tb_lineno)

    shapes.append(Triangle(2, 3, 4))

    try:
        quad_1 = Quadrilateral()
    except TypeError as e:
        logger.error("%r at line %s", e, e.__traceback__.tb_lineno)

    shapes.append(Rectangle(1, 2))

    for s in shapes:
        print(f"# {s=}, {s.perimeter()=}, {s.area()=}")


if __name__ == "__main__":
    with log_to("main", stream="DEBUG") as logger:
        main()

#    ERROR - m9_2_5.py:137 main.main() - TypeError("Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter'") at line 135
#    DEBUG - m9_2_5.py:94 Triangle.__init__() - constructing Triangle with 2, 3, 4
#    ERROR - m9_2_5.py:144 main.main() - TypeError("Can't instantiate abstract class Quadrilateral without an implementation for abstract methods 'area', 'sides'") at line 142
#    DEBUG - m9_2_5.py:58 Triangle.__repr__() - representing sides (2, 3, 4) as string
# s=Triangle(2, 3, 4), s.perimeter()=9, s.area()=2.9047375096555625
#    DEBUG - m9_2_5.py:58 Rectangle.__repr__() - representing sides (1, 2, 1, 2) as string
# s=Rectangle(1, 2, 1, 2), s.perimeter()=6, s.area()=2
#     INFO - m8_2_2.py:67 main.logging_context() - shutting down the logging facility...
