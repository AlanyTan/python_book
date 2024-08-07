"""Demo Adapter Pattern using Circle & Shaps

Classes:
    Circle: imported original Circle class
    CircleShape: a Circle adapter class inherited from Shape
    Shape and offsprings: imported family of Shape and subclasses 
"""

import logging
logging.basicConfig(level=logging.INFO, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

from m9_1_3_II import Circle
from m9_4_2 import Shape, Triangle, Rectangle, Square, ShapeFactory


class CircleShape(Shape):
    """Adapt Circle to return circumference if called its perimeter"""

    def __init__(self, radius: int | float):
        """construct adatpr that holds an original circle"""
        self.circle = Circle(radius)

    def perimeter(self) -> float:
        """rename circumference as primeter"""
        return self.circle.circumference()

    def area(self) -> float:
        """forward Circle.area as self.area"""
        return self.circle.area()

    def __repr__(self) -> str:
        """return test representation of self"""
        return f"{self.__class__.__name__}({self.circle.radius})"


def main():
    """showing Shape, Quadrilater are abstract; Rectangle can be instantiated"""
    shape_creator = ShapeFactory()
    ShapeFactory.register_shape_type('Triangle', Triangle, 3)
    ShapeFactory.register_shape_type('Rectangle', Rectangle, 2)
    ShapeFactory.register_shape_type('Square', Square, 1)
    ShapeFactory.register_shape_type('Circle', CircleShape, 1)
    shapes_to_create = [('Triangle', 3, 4, 5),
                        ('Square', 5),
                        ('Rectangle', 8, 9),
                        ('Triangle',),
                        ('Circle', 1)]
    shapes_created = []
    try:
        for stc in shapes_to_create:
            shapes_created.append(shape_creator.create_shape(*stc))

    except ValueError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")

    print(f"# the created list of shapes:[", *map(
        lambda x: (x, x.perimeter()), shapes_created), ']', sep='\n#  ')


if __name__ == "__main__":
    main()

# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Triangle', 3, 4, 5)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Square', 5)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Rectangle', 8, 9)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Triangle',)
# DEBUG - ShapeFactory(m9_4_2.py:85) - .create_shape('Circle', 1)
# the created list of shapes:[
#  (Triangle(3.0, 4.0, 5.0), 12.0)
#  (Square(5, 5, 5, 5), 20)
#  (Rectangle(8, 9, 8, 9), 34)
#  (Triangle(1.0, 1.0, 1.0), 3.0)
#  (CircleShape(1), 6.2831853)
#  ]
