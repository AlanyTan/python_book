x = 7
if x % 2 == 0:
    print(f"# {x} is an even number.")
    print(f"# because {int(x / 2) == x / 2=}")
else:
    print(f"# {x} is an odd number.")
    print(f"# because {(int(x / 2) == x / 2)=}")
# 7 is an odd number.
# because (int(x / 2) == x / 2)=False

y = 8
if y % 2:
    print(f"# {y} is an odd number.")
    print(f"# because {int(y / 2) == y / 2=}")
else:
    print(f"# {y} is an even number.")
    print(f"# because {(int(y / 2) == y / 2)=}")
# 8 is an even number.
# because (int(y / 2) == y / 2)=True
