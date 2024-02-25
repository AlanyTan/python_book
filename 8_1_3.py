def safe_divide(numerator: float, denominator: float) -> float|int:
    result = None
    divisible = False
    try:
        try:
            numerator = float(numerator)
            denominator = float(denominator)
            result = numerator / denominator
            if not numerator % denominator:
                divisible = True
                
        except ZeroDivisionError as err:
            print(f"#  Error {err.args}!")
        except ValueError  as err:
            print(f"#  ValueError {err.args} on line {
                  err.__traceback__.tb_lineno}")
            print(f"#  causing another error in exception: {error}")
        except Exception as err:
            print(f"#  Error {str(err)}")
        else:
            print(f"#   got the result.")
            if divisible: 
                result = int(result[0])
            
    except TypeError as err:
        print(f"# Converting to INT error: {err.args}")
    except Exception as err:
        print(f"#  Error {str(err)}, on line {err.__traceback__.tb_lineno}")
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
# Converting to INT error: ("'float' object is not subscriptable",)
# safe_divide(a, b)=4.0
#Trying 7.1.2...
#  ValueError ("could not convert string to float: '7.1.2'",) on line 7
#  Error name 'error' is not defined, on line 17
# safe_divide(a, b)=None
#Trying 5...
#   got the result.
# safe_divide(a, b)=0.8
#program continues..
