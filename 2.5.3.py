str1 = "abc"
str2 = "DEF"

str1 += str2
print("#", str1)
# abcDEF

str1 *= 3
print("#", str1)
# abcDEFabcDEFabcDEF

str1 = "str2 formated: %.2s"
str1 %= str2
print("#", str1)
# str2 formated: DE
