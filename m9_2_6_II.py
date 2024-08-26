"""demo callable functions"""

from m9_2_5 import Shape, Polygon, Quadrilateral, Rectangle


def main() -> None:
    """demo what is callable()"""
    rect_1 = Rectangle(1, 2)
    print(f"# {callable(rect_1)=}")
    print(f"# {callable(rect_1.__init__)=}")
    print(f"# {callable(rect_1.area)=}")
    print(f"# {callable(rect_1.sides)=}")

    print(f"# {callable(Rectangle)=}")
    print(f"# {callable(Rectangle.__init__)=}")
    print(f"# {callable(Rectangle.area)=}")
    print(f"# {callable(Rectangle.sides)=}")

    print(f"# {callable(Shape)=}")
    print(f"# {callable(Polygon.area)=}")
    print(f"# {callable(Polygon.sides)=}")
    print(f"# {callable(Quadrilateral.no_of_sides)=}")


if __name__ == "__main__":
    main()

# callable(rect_1)=False
# callable(rect_1.__init__)=True
# callable(rect_1.area)=True
# callable(rect_1.sides)=False
# callable(Rectangle)=True
# callable(Rectangle.__init__)=True
# callable(Rectangle.area)=True
# callable(Rectangle.sides)=False
# callable(Shape)=True
# callable(Polygon.area)=True
# callable(Polygon.sides)=False
# callable(Quadrilateral.no_of_sides)=False
