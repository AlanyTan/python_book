"""Demo Factory Method Pattern using Shaps

Classes:
    Triangle: simplified Triangle inherited from Polygon
    Square: simplified Square inherited from Rectangle
    ShapFactory: the Factory class that can create various shapes
    Shape and offsprings: imported family of Shape and subclasses 
"""
from m8_2_2 import get_logger, logging_context as log_to
from m9_2_5 import Shape, Triangle, Rectangle


class Square(Rectangle):
    """Square, inherited from Rectangle to demo factory"""

    def __init__(self, l: int | float) -> None:
        """initialize a square object

        Args:
            l: length of sides
        """
        super().__init__(l, l)


class ShapeFactory:
    """the factory class to generate different shapes"""

    _registered_shapes = dict()

    logger = get_logger("ShapeFactory", "DEBUG")

    @classmethod
    def register_shape_type(cls, name: str, class_: object, arg_no: int
                            ) -> None:
        """register a shape for the Factory Method to create

        Args:
            name: the name of the shape
            class_: the class itself
            arg_no: the number of arguments this class requires
        """
        cls._registered_shapes[name] = (class_, arg_no)

    @classmethod
    def create_shape(cls, *args: str | int | float) -> Shape:
        """the Factory Method to construct and return shapes based on args"""
        cls.logger.debug("creating a shape with %r ", args)
        type_, *rest_args = args
        if type_ in cls._registered_shapes:
            shape, arg_no = cls._registered_shapes[type_]
            rest_args.extend([0] * (arg_no - len(rest_args)))
        else:
            cls.logger.error("'%s' is not a registered shape", type_)
            raise ValueError(f"'{type_}' is not a registered shape.")
        return shape(*rest_args[:arg_no])


def main():
    """Use the Factory Method to create shapes"""
    ShapeFactory.register_shape_type('Triangle', Triangle, 3)
    ShapeFactory.register_shape_type('Rectangle', Rectangle, 2)
    ShapeFactory.register_shape_type('Square', Square, 1)
    shapes_to_create = [('Triangle', 3, 4, 5, 6, 7),
                        ('Square', 5),
                        ('Rectangle', 8, 9),
                        ('Rectangle', 1),
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
    with log_to("main", stream=False) as logger:
        main()

#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Triangle', 3, 4, 5, 6, 7)
#    DEBUG - m9_2_5.py:94 Triangle.__init__() - constructing Triangle with 3, 4, 5
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Square', 5)
#    DEBUG - m9_2_5.py:128 Square.__init__() - constructing Rectangle with 5, 5
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Rectangle', 8, 9)
#    DEBUG - m9_2_5.py:128 Rectangle.__init__() - constructing Rectangle with 8, 9
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Rectangle', 1)
#    DEBUG - m9_2_5.py:128 Rectangle.__init__() - constructing Rectangle with 1, 0
#    DEBUG - m9_4_2.py:47 ShapeFactory.create_shape() - creating a shape with ('Circle', 1)
#    ERROR - m9_4_2.py:53 ShapeFactory.create_shape() - 'Circle' is not a registered shape
#    DEBUG - m9_2_5.py:58 Triangle.__repr__() - representing sides (3, 4, 5) as string
#    DEBUG - m9_2_5.py:58 Square.__repr__() - representing sides (5, 5, 5, 5) as string
#    DEBUG - m9_2_5.py:58 Rectangle.__repr__() - representing sides (8, 9, 8, 9) as string
#    DEBUG - m9_2_5.py:58 Rectangle.__repr__() - representing sides (1, 0, 1, 0) as string
# the created list of shapes:[
#  shp=Triangle(3, 4, 5), shp.perimeter()=12, shp.area()=6.0
#  shp=Square(5, 5, 5, 5), shp.perimeter()=20, shp.area()=25
#  shp=Rectangle(8, 9, 8, 9), shp.perimeter()=34, shp.area()=72
#  shp=Rectangle(1, 0, 1, 0), shp.perimeter()=2, shp.area()=0
# ]
