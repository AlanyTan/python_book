"""demo isinstance and issubclass functions"""

from m9_2_5 import Shape, Polygon, Quadrilateral, Rectangle

def main():
    rect_1 = Rectangle(1,2)
    print(f"# {isinstance(rect_1, Rectangle)=}")
    print(f"# {isinstance(rect_1, (list, Shape))=}")
    print(f"# {isinstance(rect_1, (list, tuple))=}")

    print(f"# {issubclass(Rectangle, Shape)=}")
    print(f"# {issubclass(tuple, (Polygon, Quadrilateral))=}")
    print(f"# {issubclass(Shape, (Polygon, Quadrilateral))=}")

if __name__ == "__main__":
    main()

# isinstance(rect_1, Rectangle)=True
# isinstance(rect_1, (list, Shape))=True
# isinstance(rect_1, (list, tuple))=False
# issubclass(Rectangle, Shape)=True
# issubclass(tuple, (Polygon, Quadrilateral))=False
# issubclass(Shape, (Polygon, Quadrilateral))=False
