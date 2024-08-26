"""demo hasattr functions"""

from m9_2_5 import Shape, Polygon, Quadrilateral, Rectangle


def main() -> None:
    """demo hasattr()"""
    rect_1 = Rectangle(1, 2)
    print(f"# {hasattr(rect_1, 'sides')=}")
    print(f"# {hasattr(rect_1, '__init__')=}")
    print(f"# {hasattr(rect_1, 'area')=}")
    print(f"# {hasattr(rect_1, 'Rectangle')=}")

    print(f"# {hasattr(Rectangle, 'sides')=}")
    print(f"# {hasattr(Rectangle, '__init__')=}")
    print(f"# {hasattr(Rectangle, 'area')=}")
    print(f"# {hasattr(Rectangle, 'Ploygon')=}")

    print(f"# {hasattr(Shape, 'area')=}")
    print(f"# {hasattr(Shape, 'no_of_sides')=}")
    print(f"# {hasattr(Polygon, 'sides')=}")
    print(f"# {hasattr(Quadrilateral, 'no_of_sides')=}")


if __name__ == "__main__":
    main()

# hasattr(rect_1, 'sides')=True
# hasattr(rect_1, '__init__')=True
# hasattr(rect_1, 'area')=True
# hasattr(rect_1, 'Rectangle')=False
# hasattr(Rectangle, 'sides')=True
# hasattr(Rectangle, '__init__')=True
# hasattr(Rectangle, 'area')=True
# hasattr(Rectangle, 'Ploygon')=False
# hasattr(Shape, 'area')=True
# hasattr(Shape, 'no_of_sides')=False
# hasattr(Polygon, 'sides')=True
# hasattr(Quadrilateral, 'no_of_sides')=True
