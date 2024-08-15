string_1 = "Hello Earth"
result_1 = sorted(string_1, key=lambda x: 1 - (x.lower() in "aeiou"))
print(f"# Vowels first: {result_1}")
# Vowels first: ['e', 'o', 'E', 'a', 'H', 'l', 'l', ' ', 'r', 't', 'h']

list_of_complex = [(3 + 1j), (3 + 2j), (2 + 3j), (2 + 2j)]
result_2 = sorted(list_of_complex, key=lambda x: x.real**2 + x.imag**2)
print(f"# Complex number sorted: {result_2}")
# Complex number sorted: [(2+2j), (3+1j), (3+2j), (2+3j)]
