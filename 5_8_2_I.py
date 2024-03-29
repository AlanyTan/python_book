numbers = [x / 10 for x in range(11)]
filter_by_round = filter(round, numbers)
print(f"# {list(filter_by_round)=}")
# list(filter_by_round)=[0.6, 0.7, 0.8, 0.9, 1.0]

filter_by_value = filter(lambda x: pow(x, 2)>0.36, numbers)
print(f"# {list(filter_by_value)=}")
# list(filter_by_value)=[0.7, 0.8, 0.9, 1.0]
