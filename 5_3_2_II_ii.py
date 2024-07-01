str_1 = "ABCD"
byte_arr_1 = bytearray(b'EFGH')
list_1 = [1, '2.0', (3.0+4j)]

print("# ", str_1)
#  ABCD
print("# ", *str_1)
#  A B C D

print("# ", byte_arr_1)
#  bytearray(b'EFGH')
str_template = ("# ASCII code of '{0:c}' is {0:d}\n"
                "# ASCII code of '{1:c}' is {1:d}\n"
                "# ASCII code of '{2:c}' is {2:d}\n"
                "# ASCII code of '{3:c}' is {3:d}")
print(str_template.format(*byte_arr_1))
# ASCII code of 'E' is 69
# ASCII code of 'F' is 70
# ASCII code of 'G' is 71
# ASCII code of 'H' is 72

print("# ", list_1)
#  [1, '2.0', (3+4j)]
list_3 = [*list_1, *str_1, *byte_arr_1]
print(f"# {list_3=}")
# list_3=[1, '2.0', (3+4j), 'A', 'B', 'C', 'D', 69, 70, 71, 72]
