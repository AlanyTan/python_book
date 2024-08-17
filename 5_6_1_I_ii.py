key_1 = ("grade 1", "class 1")
value_1 = ["Albert Einstein", "Benjamin Franklin", "Charles Darwin"]
key_2 = ("grade 1", "class 2")
value_2 = ["Zhao Qian", "Sun Li", "Zhou We", "Zheng Wang"]
dict_example = {key_1: value_1, key_2: value_2}
print(f"# dictionary: {dict_example}")
# dictionary: {('grade 1', 'class 1'): ['Albert Einstein', 'Benjamin Franklin', 'Charles Darwin'], ('grade 1', 'class 2'): ['Zhao Qian', 'Sun Li', 'Zhou We', 'Zheng Wang']}

value_2[2:4] = []
print(f"# {dict_example[("grade 1", "class 1")].pop()=}")
# dict_example[("grade 1", "class 1")].pop()='Charles Darwin'
print(f"# dictionary: {dict_example}")
# dictionary: {('grade 1', 'class 1'): ['Albert Einstein', 'Benjamin Franklin'], ('grade 1', 'class 2'): ['Zhao Qian', 'Sun Li']}
