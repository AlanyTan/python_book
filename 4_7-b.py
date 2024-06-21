string_1 = "Hello Earth"
result= sorted(string_1, lambda x: 1-(x.lower in "aeiou"))

print(f"# Vowels first: {result}")
# Vowels first: ['e', 'o', 'E', 'a', 'H', 'l', 'l', ' ', 'r', 't', 'h']
