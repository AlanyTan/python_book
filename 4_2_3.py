def parallelepiped_volume(length, width, height) -> int|float:
    """Calculate volume of a parallellepiped (a shape with six sides, 
        each side is a parallelogram, each side is the same shape as
        its opposite.)
    
    Args:
        length (int|float): Length of one edge of the bottom.
        width (int|float): The distance between the two edges of 
            which the length were taken from.
        height (int|float): The distance between the bottom and top.

    Returns:
        int|float: The number representing the volume of the parallelepiped.
    """
    def area(x, y) -> int|float:
        return x * y

    return area(length, width) * height
