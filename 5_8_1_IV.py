numbers = [x if x==1 else 1/x for x in range(1,4)]
print(f"# {numbers=}, {max(numbers)=:4.4f}")
# numbers=[1, 0.5, 0.3333333333333333], max(numbers)=1.0000

filtered_numbers = [x for x in numbers if x > 1]
print(f"# {filtered_numbers=}, {min(filtered_numbers, default='empty')=}")
# filtered_numbers=[], min(filtered_numbers, default='empty')='empty'

print(f"# {max([numbers, 'abcdefg'], key=len)=}")
# max([numbers, 'abcdefg'], key=len)='abcdefg'

print(f"# {min(numbers, range(4), key=sum)=}")
# min(numbers, range(4), key=sum)=[1, 0.5, 0.3333333333333333]
