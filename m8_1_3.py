"""Demo try-except-else structure with 'only do this part if no errors.

Usage:
    python -m m8_1_3
"""
def safe_divide(numerator: int|float, denominator: int|float) -> float|int:
    """division with data checking before the / operation.

    This version moves converting to int into the -else clause of try-except.

    Args:
        numerator: number to be divided.
        denominator: number to be divided by. 
    
    Returns:
        both numerator and denominator are numbers and denominator is not 0,
        the quotient as int if divisible, or quotient as float if not.
        otherwise return None.
    """
    result = None
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        print(f"#  got the result.")
            
    except ZeroDivisionError as err:
        print(f"#  Error {err.args}!")
    except ValueError as err:
        print(f"#  ValueError {err.args} on line {err.__traceback__.tb_lineno}")
    except Exception as err:
        print(f"#  Error {str(err)}")
    except:
        print(f"#  A rare unknown error has occurred, skipping divide") 
    else:
        if (isinstance(numerator, int) and isinstance(denominator, int)
            and not numerator % denominator):
            result = int(result)
        
    return result

def main(list_of_numbers_to_try: list[int]) -> None:
    """main func demo sending different denominators to save_divide.
    
    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call save_divide.
    """
    a = 4
    for b in list_of_numbers_to_try:
        print(f"#Trying {b}...")
        print(f"# {safe_divide(a, b)=}")
        
    
if __name__ == "__main__":
    denominators_to_try = [ 0, 1, '7.1.2', 5]
    main(denominators_to_try)

#Trying 0...
#  Error ('float division by zero',)!
# safe_divide(a, b)=None
#Trying 1...
#  got the result.
# safe_divide(a, b)=4
#Trying 7.1.2...
#  ValueError ("could not convert string to float: '7.1.2'",) on line 6
# safe_divide(a, b)=None
#Trying 5...
#  got the result.
# safe_divide(a, b)=0.8

