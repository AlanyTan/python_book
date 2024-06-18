string_capital = "ABCD"
string_lower = "abcd"
string_underscore = "_ABCD_EFGH"
string_space = "abcd efgh"

print("#", string_capital == string_underscore[1:5])
# True

print("#", string_lower != string_space[:4])
# False

print("#", string_capital >= string_lower)
# False

print("#", string_lower < string_space)
# True

print("#", string_lower in string_underscore)
# False

print("#", string_capital not in string_space)
# True
