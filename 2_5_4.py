string_big = "ABCD"
string_small = "abcd"
string_underscore = "_ABCD_EFGH"
string_space = "abcd efgh"

print("#", string_big == string_underscore[1:5])
# True

print("#", string_small != string_space[:4])
# False

print("#", string_big >= string_small)
# False

print("#", string_small < string_space)
# True

print("#", string_small in string_space)
# True

print("#", string_big not in string_underscore)
# False
