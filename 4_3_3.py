def volume(length, width, height) -> int|float:
    """Calculates the volume of a rectangular prism.

    Args:
        length (int or float): The length of the rectangular prism.
        width (int or float): The width of the rectangular prism.
        height (int or float): The height of the rectangular prism.

    Returns:
        int or float: The volume of the rectangular prism.
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

print(f"# {area(2, 3)=}")
# area(2, 3)=6

print (f"# {volume(2, 3, 4)=}")
# volume(2, 3, 4)=24
