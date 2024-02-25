def rectangular_prism_volume(length, width, height) -> int|float:
    def area(x, y):
        return x * y
    
    return area(length, width) * height
