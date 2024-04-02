def circle_area(x) -> float:
    PI = 3.14159
    circumference = 2 * PI * x 
    return circumference

def rectangle_area(length, width) -> int|float:
    return length * width

def print_rectangle_area(length,width) -> None:
    print(f"area of the rectangle is:{length * width}")
