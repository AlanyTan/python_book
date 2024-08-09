"""Introduce static method, class method

Classes:
    Tiangle:defined by the length of three sides
"""

import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


class Triangle:
    """Triangle class to demo properties"""
    _instances = []

    @staticmethod
    def is_valid_sides(*sides: tuple) -> bool:
        """validate if provided arguments can form a triangle

        Args:
            any number of arguments: representing length of 3 sides

        Returns:
            True if the there are 3 args and sum of two smaller number is
                greater than the larger number.
            Flase if not 3 args, or some args can't be converted to numbers
                or the sum of two smaller numbers less than the large number
        """
        try:
            temp_sides = sorted(map(float, sides))
        except Exception as e:
            logger.warning(f" {sides} contain element(s) that is not numeric")
            return False

        if len(sides) != 3:
            logger.warning(f" {sides} does not have 3 numbers.")
            return False
        elif temp_sides[0] + temp_sides[1] < temp_sides[2]:
            logger.warning(f" {sides} two short sides < than long side")
            return False
        else:
            return True

    @classmethod
    def count(cls, threshold: float = 0) -> None:
        """count Triangles bigger (or smaller) than the given threshold

        Args:
            threshold: if positive, only count triangles bigger than threshold
                       if negative, only count triangles smaller than abs of it
        """
        sign = (threshold > 0) - (threshold < 0)
        filtered_instance = [
            tri for tri in cls._instances if threshold <= (tri.area() * sign)]
        return len(filtered_instance)

    @property
    def sides(self) -> tuple:
        """tuple: length of 3 sides of the Triangle, a tuple"""
        return tuple(self._sides)

    @sides.setter
    def sides(self, s: tuple[int | float]) -> None:
        if self.is_valid_sides(*s):
            self._sides = list(map(float, s))
            self.logger.debug(f".sides setter called with {s=}")
        else:
            self.logger.error(f"Invalid lenths {s=}, a+b must >= c")
            raise ValueError(f"Invalid lenths {s}! ")

    def __init__(self, *sides: tuple):
        """Initialize a triangle with lengths of three sides

        Args:
            s1, s2, s3: three numbers represent length of 3 sides, or
            iterable: with 3 items each can be converted a number
        """
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(f".__init__() called with {sides=}")
        self.sides = sides
        self._instances.append(self)

    def __repr__(self) -> str:
        """return string representation of a Triangle obj"""
        return f"Triangle{self.sides}"

    def perimeter(self) -> float:
        """return the total length of all three sides"""
        return sum(self.sides)

    def area(self) -> float:
        """calculate the area of the triangle using Heron formula"""
        half_perimeter = self.perimeter() / 2
        temp_calc = half_perimeter
        for s in self.sides:
            temp_calc *= (half_perimeter - s)

        return (temp_calc) ** (1 / 2)

    def isright(self) -> bool:
        """if the 3 sides meet Pythagorean Theorem a^2+b^2=c^2"""
        sorted_sides = sorted(self.sides)
        return sorted_sides[2]**2 == sorted_sides[0]**2 + sorted_sides[1]**2

    def isisosceles(self) -> bool:
        """if at least 2 side are equal length"""
        sorted_sides = sorted(self.sides)
        return (sorted_sides[0] == sorted_sides[1]
                or sorted_sides[1] == sorted_sides[2])

    def isequilateral(self) -> bool:
        """if all three sides are equal length"""
        return self.sides[0] == self.sides[1] == self.sides[2]


def main():
    """main func demo calling static and class methods from outside of class"""
    try:
        sides_list = [(2, 3, 4), (3, 4, 5), (1, 2, 4),
                      ('a', 'b', 'c'), (3, 4, '8'), (4, 5)]
        for sides in sides_list:
            print(f"# {sides=}, {Triangle.is_valid_sides(*sides)=}")

        tris = []
        for sides in sides_list:
            tris.append(Triangle(*sides))
            print(f"# {tris[-1]=}")

    except ValueError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")

    print(f"# {Triangle.count()=}")


if __name__ == "__main__":
    main()

# sides=(2, 3, 4), Triangle.is_valid_sides(*sides)=True
# sides=(3, 4, 5), Triangle.is_valid_sides(*sides)=True
# WARNING - __main__(m9_2_4.py:40) -  (1, 2, 4) two short sides < than long side
# sides=(1, 2, 4), Triangle.is_valid_sides(*sides)=False
# WARNING - __main__(m9_2_4.py:33) -  ('a', 'b', 'c') contain element(s) that is not numeric
# sides=('a', 'b', 'c'), Triangle.is_valid_sides(*sides)=False
# WARNING - __main__(m9_2_4.py:40) -  (3, 4, '8') two short sides < than long side
# sides=(3, 4, '8'), Triangle.is_valid_sides(*sides)=False
# WARNING - __main__(m9_2_4.py:37) -  (4, 5) does not have 3 numbers.
# sides=(4, 5), Triangle.is_valid_sides(*sides)=False
# tris[-1]=Triangle(2.0, 3.0, 4.0)
# tris[-1]=Triangle(3.0, 4.0, 5.0)
# WARNING - __main__(m9_2_4.py:40) -  (1, 2, 4) two short sides < than long side
# ERROR - Triangle(m9_2_4.py:69) - Invalid lenths s=(1, 2, 4), a+b must >= c
# ERROR - __main__(m9_2_4.py:131) - Invalid lenths (1, 2, 4)!  at line 127
# Triangle.count()=2
