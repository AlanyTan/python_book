def rectangular_prism_volume(length, width, height) -> int|float:
    def area(x, y):
        return x * y
    
    return area(length, width) * height

print(f"# {rectangular_prism_volume(length=1, 3, 2)=}")
# rectangular_prism_volume(1, height=3, width=2)=6
