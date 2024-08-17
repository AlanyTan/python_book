numbers = [x if x == 1 else 1 / x for x in range(1, 4)]
print(f"# {numbers=}, {(sum_of_numbers := sum(numbers))=:4.4f}")
# numbers=[1, 0.5, 0.3333333333333333], (sum_of_numbers:=sum(numbers))=1.8333

complex_numbers = ((1 + 2j), (2 + 3j), (3 + 4j))
print(f"# {complex_numbers=}, {sum(complex_numbers)=:4.4f}")
# complex_numbers=((1+2j), (2+3j), (3+4j)), sum(complex_numbers)=6.0000+9.0000j

more_numbers = {x if x == 1 else 1 / x for x in range(4, 6)}
print(f"# {more_numbers=}, {sum(more_numbers, sum_of_numbers)=:4.4f}")
# more_numbers={0.25, 0.2}, sum(more_numbers, sum_of_numbers)=2.2833

complex_dict = {x.real: x.imag for x in complex_numbers}
print(f"# {complex_dict=}, {sum(complex_dict, sum_of_numbers)=:4.4}")
# complex_dict={1.0: 2.0, 2.0: 3.0, 3.0: 4.0}, sum(complex_dict, sum_of_numbers)=7.833
