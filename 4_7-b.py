numbers=range(10)
result= sorted(numbers, key=lambda x: 1/(x+1) + x%2)

print(f"# 2-digit prime numbers: {result}")
# 2-digit prime numbers: [8, 6, 4, 2, 0, 9, 7, 5, 3, 1]
