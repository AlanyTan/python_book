numbers = range(-4,1)
print(f"# {list(numbers)=}")
# list(numbers)=[-4, -3, -2, -1, 0]

sorted_numbers = sorted(numbers, key=abs)
print(f"# {list(sorted_numbers)=}")
# list(sorted_numbers)=[0, -1, -2, -3, -4]

sorted_by_sq = sorted(numbers, key=lambda x: x**2 % 10)
print(f"# {list(sorted_by_sq)=}")
# list(sorted_by_sq)=[0, -1, -2, -4, -3]
