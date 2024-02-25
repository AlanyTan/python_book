def volume(length, width, height) -> int|float:
    return area(length, width) * height

def area(x, y) -> int|float:
    return x * y

print(f"# {area(2, 3)=}")
# area(2, 3)=6

print (f"# {volume(2,3,4)=}")
# volume(2,3,4)=24
