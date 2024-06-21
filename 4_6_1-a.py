def input_a_number() -> int|float|None:
    user_input = input("Please Enter a Number:")
    if user_input.isdigit():
        return int(user_input)
    elif user_input.replace('.','',1).isdigit():
        return float(user_input)
    else:
        return None

def multiply(a: int|float, n: int) -> int|float:
    return a * n

number_a = input_a_number()
n = 5
if not number_a is None:
    print(f"{multiply(number_a, n)=}")
          
