"""Introduce multi inheritance using Parallelogram family

Classes:
    Parallelogram: imported
    Rectangle: imported
    Rhombus: all 4 sides equal length (a.k.a diamond)
    square: all side equal, 90 dg angle
"""

from m9_2_1_I import Parallelogram, Rectangle, get_logger, log_to
logger = get_logger(__name__, stream='DEBUG')


class Rhombus(Parallelogram):
    """Rhombus class inherited from Parallelogram

    All 4 sides are the same length"""
    @property
    def side(self) -> int | float:
        """int|float: length of sides of the Rhombus"""
        return self._long_side

    @side.setter
    def side(self, l: int | float) -> None:
        logger.debug(" -Rhombus side setter: called with l=%s", l)
        try:
            self.long_side = self._short_side = l
        except ValueError as e:
            e.add_note("Rhombus side length need to be >=0")
            raise

    @property
    def short_side(self) -> int | float:
        """make short_side a read-only property"""
        return super().short_side

    @short_side.setter
    def short_side(self, s):
        """redirect setting short_side to long_side setter"""
        self.side = s

    def __init__(self, l: int | float, a: int | float):
        """Initialize a Rhombus
        Args:
            l: length of the sides
            a: one of the angles
        """
        logger.debug("-Rhombus constructor will call super() constructor...")
        super().__init__(l, l, a)


class Square(Rectangle, Rhombus):
    """Square, inherited from Rectangle AND Rhombus"""

    def __init__(self, l: int | float):
        """Construct a square object by calling Rhombus.__init__()"""
        logger.debug("-Square constructor, MRO:{self.__class__.mro()}")
        super(Rectangle, self).__init__(l, 90)


def main() -> None:
    """demonstrate multi-inheritance"""
    try:
        rhombus_1 = Rhombus(1, 45)
        rhombus_1.side = 2
        print(f"# {rhombus_1.area()=}")

        sq_1 = Square(6)
        print(f"# {sq_1.side=}, {sq_1.area()=}")

    except ValueError as e:
        logger.error("%r at line %s", e, e.__traceback__.tb_lineno)
        print("# ERROR:", e)


if __name__ == "__main__":
    with log_to("main", stream=False):
        main()

#    DEBUG - m9_2_1_I.py:20 m9_2_1_I.Parallelogram() - defining class
#    DEBUG - m9_2_1_I.py:136 m9_2_1_I.Rectangle() - defining class based on Parallelogram
#    DEBUG - m9_2_1_II.py:48 __main__.__init__() - -Rhombus constructor will call super() constructor...
#    DEBUG - m9_2_1_I.py:106 m9_2_1_I.__init__() - Parallelogram constructor called
#    DEBUG - m9_2_1_I.py:40 m9_2_1_I.long_side() - Parallelogram setter: called with l=1
#    DEBUG - m9_2_1_II.py:25 __main__.side() -  -Rhombus side setter: called with l=1
#    DEBUG - m9_2_1_I.py:40 m9_2_1_I.long_side() - Parallelogram setter: called with l=1
#    DEBUG - m9_2_1_I.py:72 m9_2_1_I.acute_angle() - Parallelogram setter: called with aa=45
#    DEBUG - m9_2_1_II.py:25 __main__.side() -  -Rhombus side setter: called with l=2
#    DEBUG - m9_2_1_I.py:40 m9_2_1_I.long_side() - Parallelogram setter: called with l=2
#    DEBUG - m9_2_1_I.py:124 m9_2_1_I.height() - - Parallelogram.height() calculated using sin()
# rhombus_1.area()=2.82842712474619
#    DEBUG - m9_2_1_II.py:57 __main__.__init__() - -Square constructor, MRO:{self.__class__.mro()}
#    DEBUG - m9_2_1_II.py:48 __main__.__init__() - -Rhombus constructor will call super() constructor...
#    DEBUG - m9_2_1_I.py:106 m9_2_1_I.__init__() - Parallelogram constructor called
#    DEBUG - m9_2_1_I.py:40 m9_2_1_I.long_side() - Parallelogram setter: called with l=6
#    DEBUG - m9_2_1_II.py:25 __main__.side() -  -Rhombus side setter: called with l=6
#    DEBUG - m9_2_1_I.py:40 m9_2_1_I.long_side() - Parallelogram setter: called with l=6
#    DEBUG - m9_2_1_I.py:72 m9_2_1_I.acute_angle() - Parallelogram setter: called with aa=90
#    DEBUG - m9_2_1_I.py:144 m9_2_1_I.height() - Rectangle.height() return short_side directly
# sq_1.side=6, sq_1.area()=36
