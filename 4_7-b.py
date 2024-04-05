numbers=range(10,100)
result= filter(lambda x: x%2 * x%3 * x%5 * x%7, numbers)

print(f"# 2-digit prime numbers: {sorted(result)}")
