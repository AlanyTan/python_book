alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"# length of literal: {len('abcde')=}")
# length of literal: len('abcde')=5

print(f"# length of Unicode string: {len('Python程序设计')=}")
# length of Unicode string: len('Python程序设计')=10

print(f"# length of variable: {len(alphabet)=}")
# length of variable: len(alphabet)=26

print(f"# length of expression: {len(alphabet[:3] * 2)=}")
# length of expression: len(alphabet[:3] * 2)=6

print(f"# positive and negative indexing equal: "
      f"{alphabet[len(alphabet) - 1:0:-1] == alphabet[-1:-len(alphabet):-1]}")
# positive and negative indexing equal: True
