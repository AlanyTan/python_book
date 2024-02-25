number_to_be_added_to = 85
number_to_add = 31
while number_to_add != 0:
    bits_with_both_1 = number_to_be_added_to & number_to_add
    number_to_be_added_to = number_to_be_added_to ^ number_to_add
    number_to_add = bits_with_both_1 << 1
print("# addition result:", number_to_be_added_to)
# addition result: 116
