numbers=range(-5,5)
result= map(lambda x: x**2,numbers)
str_result = ""
for item in result:
    str_result += f"{item} "

print(f"# ^2 of each number: {(str_result)}")
# ^2 of each number: 25 16 9 4 1 0 1 4 9 16
