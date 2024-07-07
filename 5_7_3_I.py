numbers = [x / 10 for x in range(11)]
filter_by_round = filter(round, numbers)
print(f"# {list(filter_by_round)=}")
# list(filter_by_round)=[0.6, 0.7, 0.8, 0.9, 1.0]

filter_by_value = filter(lambda x: pow(x, 2)>0.36, numbers)
print(f"# {list(filter_by_value)=}")
# list(filter_by_value)=[0.7, 0.8, 0.9, 1.0]

dict_1 = {k+1: k for k in range(5)}
print(f"# {dict(filter(lambda x: x[1]%2, dict_1.items()))=}")
# dict(filter(lambda x: x[1]%2, dict_1.items()))={2: 1, 4: 3}
