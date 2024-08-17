print(f"# {min('aceg123')=}")
# min('aceg123')='1'

numbers = [x if x == 1 else 1 / x for x in range(1, 4)]
print(f"# {numbers=}, {max(numbers)=}")
# numbers=[1, 0.5, 0.3333333333333333], max(numbers)=1

empty_tuple = ()
print(f"# {empty_tuple=}, {min(empty_tuple, default='nothing')=}")
# empty_tuple=(), min(empty_tuple, default='nothing')='nothing'

print(f"# {max([numbers, 'abcdefg'], key=len)=}")
# max([numbers, 'abcdefg'], key=len)='abcdefg'

print(f"# {min({2}, {1}, {1, 2})=}")
# min({2}, {1}, {1,2})={2}
