def parallelepiped_volume(length, width, height) -> int|float:
    """Calculate volumn of a parallellepiped (a shape with six sides, 
        each side is a parallelogram, each side is the same shape as
        its opposite.)
    
    Args:
        length: int:float
            length of one edge of the bottom.
        width: int:float
            the distance between the two edges length was taken from.
        height: int:float
            the distance between the bottom and top.
    
    Return:
        A float or int representing the volume of the parallelepiped.
    """
    def area(x, y) -> float:
        return x * y

    return area(length, width) * height
