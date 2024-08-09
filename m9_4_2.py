"""Demo Factory Method Pattern using Shaps

Classes:
    Triangle: simplified Triangle inherited from Polygon
    Square: simplified Square inherited from Rectangle
    ShapFactory: the Factory class that can create various shapes
    Shape and offsprings: imported family of Shape and subclasses 
"""
import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m9_2_5 import Shape, Polygon, Rectangle


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

    _registered_shapes = []

    @classmethod
    def create_shape(self, *args: tuple[str | int | float]) -> Shape:
        """the Factory Method to construct and return shapes based on args"""
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.debug(f".create_shape{args}")
        type_, *rest = args
        type_filtered = list(filter(
            lambda x: x[0] == type_, self._registered_shapes))
        if len(type_filtered) > 0:
            registered_shape = type_filtered[0]
            for i in range(registered_shape[2] - len(rest)):
                rest.append(1)
            return registered_shape[1](*rest[:registered_shape[2]])
        else:
            self.logger.error(f"'{type_}' is not a registered shape.")
            raise ValueError(f"'{type_}' is not a registered shape.")

    @classmethod
    def register_shape_type(cls, name: str, class_: object, arg_no: int) -> None:
        """register a shape for the Factory Method to create

        Args:
            name: the name of the shape
            class_: the class itself
            arg_no: the number of arguments this class requires
        """
        cls._registered_shapes.append((name, class_, arg_no))


def main():
    """showing Shape, Quadrilater are abstract; Rectangle can be instantiated"""
    ShapeFactory.register_shape_type('Triangle', Triangle, 3)
    ShapeFactory.register_shape_type('Rectangle', Rectangle, 2)
    ShapeFactory.register_shape_type('Square', Square, 1)
    shapes_to_create = [('Triangle', 3, 4, 5),
                        ('Square', 5),
                        ('Rectangle', 8, 9),
                        ('Triangle',),
                        ('Circle', 1)]
    shapes_created = []
    try:
        for stc in shapes_to_create:
            shapes_created.append(ShapeFactory.create_shape(*stc))

    except ValueError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")

    print(f"# the created list of shapes:[", *map(
        lambda x: (x, x.area()), shapes_created), ']', sep='\n#  ')


if __name__ == "__main__":
    main()

# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Triangle', 2, 3, 4)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Square', 5)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Rectangle', 8, 9)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Triangle',)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Circle',)
# ERROR - ShapeFactory(m9_4_2.py:95) - 'Circle' is not a registered shape.
# ERROR - __main__(m9_4_2.py:127) - 'Circle' is not a registered shape. at line 124
# the created list of shapes:[
#  (Triangle(3.0, 4.0, 5.0), 6.0)
#  (Square(5, 5, 5, 5), 25)
#  (Rectangle(8, 9, 8, 9), 72)
#  (Triangle(1.0, 1.0, 1.0), 0.4330127018922193)
#  ]
