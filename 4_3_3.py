def volume(length: int | float, width: int | float,
           height: int | float) -> int | float:
    """Calculates the volume of a rectangular prism.

    Args:
        length: The length of the rectangular prism.
        width: The width of the rectangular prism.
        height: The height of the rectangular prism.

    Returns:
        The volume of the rectangular prism.
    """
    return area(length, width) * height


def area(length: int | float, width: int | float) -> int | float:
    """Calculates the area of a rectangle.

    Args:
        length: The length of the rectangle.
        width: The width of the rectangle.

    Returns:
        The area of the rectangle.
    """
    return length * width


print(f"# {area(2, 3)=}")
# area(2, 3)=6

print(f"# {volume(2, 3, 4)=}")
# volume(2, 3, 4)=24
