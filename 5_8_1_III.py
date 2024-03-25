numbers = [x if x==1 else 1/x for x in range(1,4)]
print(f"# {numbers=}, {(sum_of_numbers:=sum(numbers))=:4.4f}")
# numbers=[1, 0.5, 0.3333333333333333], (sum_of_numbers:=sum(numbers))=1.8333333333333333

more_numbers = [x if x==1 else 1/x for x in range(4,6)]
print(f"# {more_numbers=}, {sum(more_numbers, sum_of_numbers)=:4.4f}")
# more_numbers=[0.25, 0.2], sum(more_numbers, sum_of_numbers)=2.283333333333333


complex_numbers = [complex(x, x+1) for x in range(2)]
print(f"# {complex_numbers=}, {sum(complex_numbers, sum_of_numbers)=:4.4}")
# complex_numbers=[1j, (1+2j)], sum(complex_numbers, sum_of_numbers)=(2.833333333333333+3j)
