prime_numbers = [x for x in range(10, 100)
                 if (x % 2 and x % 3 and x % 5 and x % 7)]
result = [float(x) if (x % 10 + x // 10 == 10) else x for x in prime_numbers]
print(f"# {result=}")
# result=[11, 13, 17, 19.0, 23, 29, 31, 37.0, 41, 43, 47, 53, 59, 61, 67, 71, 73.0, 79, 83, 89, 97]
