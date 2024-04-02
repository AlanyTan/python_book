def volume(length, width, height) -> int|float:
    """Calculates the volume of a rectangular prism.

    Args:
        length (int|float): The length of the rectangular prism.
        width (int|float): The width of the rectangular prism.
        height (int|float): The height of the rectangular prism.

    Returns:
        int|float: The volume of the rectangular prism.
    """
    return area(x=length, y=width) * height

def area(x, y) -> int|float:
    """Calculates the area of a rectangle.

    Args:
        x (int|float): The length of the rectangle.
        y (int|float): The width of the rectangle.

    Returns:
        int|float: The area of the rectangle.
    """
    return x*y

print(f"# {area(x=2, y=3)=}")
# area(x=2, y=3)=6

print (f"# {volume(length=2, width=3, height=4)=}")
# volume(length=2, width=3, height=4)=24
