numbers = [x / 10 for x in range(11)]
round_of_numbers = map(round, numbers)
print(f"# {list(round_of_numbers)=}")
# list(round_of_numbers)=[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

pow_of_numbers = map(lambda x: round(pow(x, 2),3), numbers)
print(f"# {list(pow_of_numbers)=}")
# list(pow_of_numbers)=[0.0, 0.01, 0.04, 0.09, 0.16, 0.25, 0.36, 0.49, 0.64, 0.81, 1.0]
