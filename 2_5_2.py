message = "Hello,"" World!"

message2 = message[:5] + " Python!"
print("# str concatenation:", message2)
# str concatenation: Hello Python!

message3 = message * 3      
print("# str multiplication:", message3)
# str multiplication: Hello, World!Hello, World!Hello, World!

formatted_message = "%.5s Python!" % message3
print("# str formating:", formatted_message)
# str formating: Hello Python!

str_variable_5 = "5.0"
str_variable_2 = "2"
int_variable_2 = 2

print("# str + str:", str_variable_5 + str_variable_2)
# str + str: 5.02

print("# str *"
      " int:", str_variable_5 * int_variable_2)
# str * int: 5.05.0
