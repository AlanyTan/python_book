"""Demo Factory Method Pattern using Shaps

Classes:
    Vehicle: device with wheels that can move
    Car: vehicle with engine and can be driven
    LicensePlate: the license required for driving the vehicle on the road
    DMV: Department of Motor Vehicle - centralized 
"""
import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m9_2_5 import Shape, Polygon, Quadrilateral, Rectangle


class Triangle(Polygon):
    """Triangle class to demo factory"""
    @property
    def no_of_sides(self):
        """override property set no_of_sides to 3"""
        return 3

    @property
    def sides(self) -> tuple:
        """tuple: length of 3 sides of the Triangle, a tuple"""

        return tuple(self._sides)

    @sides.setter
    def sides(self, s: tuple[int | float]) -> None:
        self._sides = list(map(float, s))
        self.logger.debug(f".sides setter called with {s=}")

    def __init__(self, *sides: tuple):
        """Initialize a triangle with lengths of three sides

        Args:
            s1, s2, s3: three numbers represent length of 3 sides, or
            iterable: with 3 items each can be converted a number
        """
        # self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.debug(f".__init__() called with {sides=}")
        self.sides = sides

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


class Square(Rectangle):
    """Square, inherited from Rectangle to demo factory"""

    def __init__(self, l: int | float):
        """initialize a square object

        Args:
            l: length of sides
        """
        super().__init__(l, l)


class ShapeFactory:
    """the factory class to generate different shapes"""

    def create_shape(self, *args: tuple[int | float]) -> Shape:
        """the Factory Method to construct and return shapes based on args"""
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(f"{args}")
        type_, *rest = args
        match type_:
            case 'Triangle':
                for i in range(3 - len(rest)):
                    rest.append(1)
                return Triangle(rest[0], rest[1], rest[2])
            case 'Rectangle':
                for i in range(2 - len(rest)):
                    rest.append(1)
                return Rectangle(rest[0], rest[1])
            case 'Square':
                for i in range(1 - len(rest)):
                    rest.append(1)
                return Square(rest[0])
            case _:
                raise ValueError(f"Not yet implemented: {len(args)}-sides.")


def main():
    """showing Shape, Quadrilater are abstract; Rectangle can be instantiated"""
    shapes_to_create = [('Triangle', 2, 3, 4),
                        ('Square', 5),
                        ('Rectangle', 8, 9),
                        ('Triangle',)]
    shapes_created = []
    shape_creator = ShapeFactory()
    try:
        for stc in shapes_to_create:
            shapes_created.append(shape_creator.create_shape(*stc))

    except ValueError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")

    print(f"# the created list of shapes:[", *shapes_created, ']', sep='\n#  ')


if __name__ == "__main__":
    main()

# DEBUG - ShapeFactory(m9_4_2.py:83) - ('Triangle', 2, 3, 4)
# DEBUG - ShapeFactory(m9_4_2.py:83) - ('Square', 5)
# DEBUG - ShapeFactory(m9_4_2.py:83) - ('Rectangle', 8, 9)
# DEBUG - ShapeFactory(m9_4_2.py:83) - ('Triangle',)
# the created list of shapes:[
#  Triangle(2.0, 3.0, 4.0)
#  Square(5, 5, 5, 5)
#  Rectangle(8, 9, 8, 9)
#  Triangle(1.0, 1.0, 1.0)
#  ]
