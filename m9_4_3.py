"""Demo Adapter Pattern using Circle & Shaps

Classes:
    Circle: imported original Circle class
    CircleShape: a Circle adapter class inherited from Shape
    Shape and offsprings: imported family of Shape and subclasses 
"""

from m8_2_2 import logging_context as log_to
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
            shapes_created.append(ShapeFactory.create_shape(*stc))

    except ValueError as e:
        logger.error("%r at line %s", e, e.__traceback__.tb_lineno)

    print("# the created list of shapes:[",
          *map(lambda shp: f"#  {shp=}, {shp.perimeter()=}, {shp.area()=}",
               shapes_created),
          '# ]', sep='\n')


if __name__ == "__main__":
    with log_to("main", stream="DEBUG") as logger:
        main()

#    DEBUG - m9_1_3_II.py:21 m9_1_3_II.Circle() - class attribute PI=3.14159265
#    DEBUG - m9_1_3_II.py:58 m9_1_3_II.Polygon() - class root level
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Triangle', 3, 4, 5)
#    DEBUG - m9_2_5.py:94 Triangle.__init__() - constructing Triangle with 3, 4, 5
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Square', 5)
#    DEBUG - m9_2_5.py:128 Square.__init__() - constructing Rectangle with 5, 5
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Rectangle', 8, 9)
#    DEBUG - m9_2_5.py:128 Rectangle.__init__() - constructing Rectangle with 8, 9
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Triangle',)
#    DEBUG - m9_2_5.py:94 Triangle.__init__() - constructing Triangle with 0, 0, 0
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Circle', 1)
#    DEBUG - m9_1_3_II.py:44 m9_1_3_II.__init__() - construct a Circle object with r=1
#    DEBUG - m9_1_3_II.py:35 m9_1_3_II.radius() - Circle radius property setter called with r=1
#    DEBUG - m9_2_5.py:58 Triangle.__repr__() - representing sides (3, 4, 5) as string
#    DEBUG - m9_2_5.py:58 Square.__repr__() - representing sides (5, 5, 5, 5) as string
#    DEBUG - m9_2_5.py:58 Rectangle.__repr__() - representing sides (8, 9, 8, 9) as string
#    DEBUG - m9_2_5.py:58 Triangle.__repr__() - representing sides (0, 0, 0) as string
# the created list of shapes:[
#  shp=Triangle(3, 4, 5), shp.perimeter()=12, shp.area()=6.0
#  shp=Square(5, 5, 5, 5), shp.perimeter()=20, shp.area()=25
#  shp=Rectangle(8, 9, 8, 9), shp.perimeter()=34, shp.area()=72
#  shp=Triangle(0, 0, 0), shp.perimeter()=0, shp.area()=0.0
#  shp=CircleShape(1), shp.perimeter()=6.2831853, shp.area()=3.14159265
# ]
#     INFO - m8_2_2.py:67 main.logging_context() - shutting down the logging facility...
