def parallelepiped_volume(length: int | float, width: int | float,
                          height: int | float) -> int | float:
    def area(x: int | float, y: int | float) -> int | float:
        return x * y

    return area(length, width) * height
