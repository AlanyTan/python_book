def circle_area(r: int|float) -> float:
    PI = 3.14159
    circumference = 2*PI*r
    return circumference

def rectangle_area(length: int|float, width: int|float) -> int|float:
    return length * width

def print_rectangle_area(length: int|float, width: int|float) -> None:
    print(f"area of the rectangle is:{length*width}")
