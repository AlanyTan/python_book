def safe_divide(numerator: float, denominator: float) -> float|int:
    result = None
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        print(f"#   got the result.")
        if not numerator % denominator:
            result = int(result[0])
            
    except ZeroDivisionError as err:
        print(f"#  Error {err.args}!")
    except ValueError as err:
        print(f"#  ValueError {err.args} on line {err.__traceback__.tb_lineno}")
    except Exception as err:
        print(f"#  Error {str(err)}")
    except:
        print(f"#  A rare unknown error has occurred, skipping divide") 
        
    return result

def main(list_of_numbers_to_try: list[int]) -> None:
    a = 4
    for b in list_of_numbers_to_try:
        print(f"#Trying {b}...")
        print(f"# {safe_divide(a, b)=}")
        
    print(f"#program continues..")
    
if __name__ == "__main__":
    denominators_to_try = [ 0, 1, '7.1.2', 5]
    main(denominators_to_try)

#Trying 0...
#  Error ('float division by zero',)!
# safe_divide(a, b)=None
#Trying 1...
#   got the result.
#  Error 'float' object is not subscriptable
# safe_divide(a, b)=4.0
#Trying 7.1.2...
#  ValueError ("could not convert string to float: '7.1.2'",) on line 5
# safe_divide(a, b)=None
#Trying 5...
#   got the result.
# safe_divide(a, b)=0.8
#program continues..
