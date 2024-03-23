def greatest_common_divisor(first_number,*tuple_of_rest):
    if tuple_of_rest:
        partial_result = greatest_common_divisor(*tuple_of_rest)
        numerator = first_number
        denominator = partial_result
        while reminder := numerator % denominator:
            numerator, denominator = denominator, reminder
            
        result = denominator
    else:
        result = first_number
    return result
    
print(f"# {greatest_common_divisor(32,96,168,240)=}")
# greatest_common_divisor(32,96,168,240)=8
