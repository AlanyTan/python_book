def parallelepiped_volume(length: int|float, width: int|float, 
                          height: int|float) -> int|float:
    """Calculate volume of a parallellepiped (a shape with six sides, 
        each side is a parallelogram, each side is the same shape as
        its opposite.)
    
    Args:
        length: Length of one edge of the bottom.
        width: The distance between the two edges of 
            which the length were taken from.
        height: The distance between the bottom and top.

    Returns:
        int|float: The number representing the volume of the parallelepiped.
    """
    def area(x, y) -> int|float:
        return x * y

    return area(x=length, y=width) * height

print(f"# {parallelepiped_volume(1, width=3, height=2)=}")
# parallelepiped_volume(1, width=3, height=2)=6
