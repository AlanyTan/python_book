def safe_divide(numerator: float, denominator: float) -> float|int:
    result = None
    divisible = False
    try:
        try:
            if isinstance(denominator, str):
                if denominator.lower() == 'zero':
                    raise ZeroDivisionError(f"{denominator} equals 0")

                char = denominator[3]
                
            numerator = float(numerator)
            denominator = float(denominator)
            result = numerator / denominator
            if not numerator % denominator:
                divisible = True
                
        except ZeroDivisionError as err:
            print(f"#   Error {err.args}!")
        except ValueError  as err:
            print(f"#   >WILL HIDE:ValueError {err.args} on line {
                  err.__traceback__.tb_lineno}")
            raise TypeError(f"Originally triggered by {err.args}@line#{
                err.__traceback__.tb_lineno}")
        except Exception as err:
            print(f"#   caught {err.args} on line {
                err.__traceback__.tb_lineno}")
            err.add_note(f"caught by inner except, re-raise.")
            raise
        else:
            print(f"#   got the result.")
            if divisible: 
                result = int(result[0])
            
    except TypeError as err:
        print(f"#  Converting to INT error: {err.args}")
    except Exception as err:
        print(f"#  Error {str(err)}, on line {err.__traceback__.tb_lineno
             } with notes {err.__notes__}")
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
    denominators_to_try = [ 'zero', '0', 0, 1, '8.3.1', 5]
    main(denominators_to_try)

#Trying zero...
#   Error ('zero equals 0',)!
# safe_divide(a, b)=None
#Trying 0...
#   caught ('string index out of range',) on line 10
#  Error string index out of range, on line 10 with notes ['caught by inner except, re-raise.']
# safe_divide(a, b)=None
#Trying 0...
#   Error ('float division by zero',)!
# safe_divide(a, b)=None
#Trying 1...
#   got the result.
#  Converting to INT error: ("'float' object is not subscriptable",)
# safe_divide(a, b)=4.0
#Trying 8.3.1...
#   >WILL HIDE:ValueError ("could not convert string to float: '8.3.1'",) on line 13
#  Converting to INT error: ('Originally triggered by ("could not convert string to float: \'8.3.1\'",)@line#13',)
# safe_divide(a, b)=None
#Trying 5...
#   got the result.
# safe_divide(a, b)=0.8
#program continues..
