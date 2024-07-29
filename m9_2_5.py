"""Demo Abstract Base Class definition and usage

Class:
    Shape: abc, with premiter(), area()
    Polygon: abc, with premiter(), area() and sides property
    Quadrilateral: abc, sintermediate class
    Rectangle: normal class
"""

from abc import ABC, abstractmethod
import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

class Shape(ABC):
    """-first base Abstract Base Class of Shapes"""
    @abstractmethod
    def area(self):
        """abstract method for culculating area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """abstract method for calculating perimeter of the shape"""
        pass

class Polygon(Shape):
    """-second abstract class, inherited from Shape, multiple straight sides"""
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

    @property
    def logger(self):
        """logger: regular property return a logger named after the class"""
        return logging.getLogger(self.__class__.__name__)
            
    def perimeter(self) -> float:
        """override method return sum of length of all sides"""
        return sum(self.sides)

class Quadrilateral(Polygon):
    @property
    def no_of_sides(self):
        """override property set no_of_sides to 4"""
        return 4

class Rectangle(Quadrilateral):
    """-two opposing sides equal, all angles 90"""
    @property
    def sides(self) -> tuple:
        """tuple: override property - store length of all sides"""
        return tuple(self._sides)

    @sides.setter
    def sides(self, s: tuple[int|float]) -> None:
        if len(s) == 4 and s[0] == s[2] and s[1] == s[3]:
            self._sides = list(s)
        else:
            self.logger.error(f"given {s} can't form a rectangle.")
            raise ValueError(f"{s} do not meet rectangle sides requirement.")

    def area(self) -> float:
        """override method return product of adjacent two sides"""
        return self.sides[0] * self.sides[1]

    def __init__(self, l: int|float, s: int|float):
        """regular constructor"""
        self.sides = ((l, s, l, s))
        

def main():
    """showing Shape, Quadrilater are abstract; Rectangle can be instantiated"""
    try:
        shape_1 = Shape()
    except TypeError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")

    try:
        quad_1 = Quadrilateral()
    except TypeError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")

    rect_1 = Rectangle(1,2)
    print(f"# {rect_1.sides=}, {rect_1.area()=}")

    try:
        rect_1.sides = (1, 2,3, 4)
    except ValueError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")        
    

if __name__ == "__main__":
    main()

#ERROR - __main__(m9_2_5.py:86) - Can't instantiate abstract class Shape without an implementation for abstract methods 'area', 'perimeter' at line 84
#ERROR - __main__(m9_2_5.py:91) - Can't instantiate abstract class Quadrilateral without an implementation for abstract methods 'area', 'sides' at line 89
# rect_1.sides=(1, 2, 1, 2), rect_1.area()=2
#ERROR - Rectangle(m9_2_5.py:69) - given (1, 2, 3, 4) can't form a rectangle.
#ERROR - __main__(m9_2_5.py:99) - (1, 2, 3, 4) do not meet rectangle sides requirement. at line 97
