"""Introduce multi inheritance using Parallelogram family

Classes:
    Parallelogram: imported
    Rectangle: imported
    Rhombus: all 4 sides equal length (a.k.a diamond)
    square: all side equal, 90 dg angle
"""

from m9_2_1_I import Parallelogram, Rectangle, logger


class Rhombus(Parallelogram):
    """Rhombus class inherited from Parallelogram

    All 4 sides are the same length"""
    @property
    def side(self) -> int | float:
        """int|float: length of sides of the Rhombus"""
        return self._long_side

    @side.setter
    def side(self, l: int | float) -> None:
        logger.debug(f" -Rhombus side setter: called with {l=}")
        try:
            self.long_side = self._short_side = l
        except ValueError as e:
            raise ValueError(f"Rhombus side length need to be >=0, "
                             f"at line {e.__traceback__.tb_lineno}")

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
        logger.debug(f"-Rhombus.__init__()")
        super().__init__(l, l, a)


class Square(Rectangle, Rhombus):
    """Square, inherited from Rectangle AND Rhombus"""

    def __init__(self, l: int | float):
        """Construct a square object by calling Rhombus.__init__()"""
        logger.debug(f" -Square.__init__(), MRO:{self.__class__.mro()}")
        super(Rectangle, self).__init__(l, 90)


def main():
    try:
        rhombus_1 = Rhombus(1, 45)
        rhombus_1.side = 2
        print(f"# {rhombus_1.area()=}")

        sq_1 = Square(6)
        print(f"# {sq_1.side=}, {sq_1.area()=}")

    except ValueError as e:
        logger.error(f"{e} at line {e.__traceback__.tb_lineno}")
        print("# ERROR:", e)


if __name__ == "__main__":
    main()

# DEBUG - m9_2_1_I(m9_2_1_I.py:15) - defining class Parallelogram.
# DEBUG - m9_2_1_I(m9_2_1_I.py:146) - defining class Rectable based on Parallelogram
# DEBUG - m9_2_1_I(m9_2_1_II.py:46) - -Rhombus.__init__()
# DEBUG - m9_2_1_I(m9_2_1_I.py:116) - Parallelogram.__init__()
# DEBUG - m9_2_1_I(m9_2_1_I.py:38) - Parallelogram long_side setter: called with l=1.
# DEBUG - m9_2_1_I(m9_2_1_II.py:23) -  -Rhombus side setter: called with l=1
# DEBUG - m9_2_1_I(m9_2_1_I.py:38) - Parallelogram long_side setter: called with l=1.
# DEBUG - m9_2_1_I(m9_2_1_I.py:74) - Parallelogram acute_angle setter: called with aa=45.
# DEBUG - m9_2_1_I(m9_2_1_II.py:23) -  -Rhombus side setter: called with l=2
# DEBUG - m9_2_1_I(m9_2_1_I.py:38) - Parallelogram long_side setter: called with l=2.
# DEBUG - m9_2_1_I(m9_2_1_I.py:134) - - Parallelogram.height()
# rhombus_1.area()=2.8284271247461903
# DEBUG - m9_2_1_I(m9_2_1_II.py:53) -  -Square.__init__(), MRO:[<class '__main__.Square'>, <class 'm9_2_1_I.Rectangle'>, <class '__main__.Rhombus'>, <class 'm9_2_1_I.Parallelogram'>, <class 'object'>]
# DEBUG - m9_2_1_I(m9_2_1_II.py:46) - -Rhombus.__init__()
# DEBUG - m9_2_1_I(m9_2_1_I.py:116) - Parallelogram.__init__()
# DEBUG - m9_2_1_I(m9_2_1_I.py:38) - Parallelogram long_side setter: called with l=6.
# DEBUG - m9_2_1_I(m9_2_1_II.py:23) -  -Rhombus side setter: called with l=6
# DEBUG - m9_2_1_I(m9_2_1_I.py:38) - Parallelogram long_side setter: called with l=6.
# DEBUG - m9_2_1_I(m9_2_1_I.py:74) - Parallelogram acute_angle setter: called with aa=90.
# DEBUG - m9_2_1_I(m9_2_1_I.py:152) - -Rectangle.height()
# sq_1.side=6, sq_1.area()=36
