"""Module containing functions for safe division and a main function to test them.

Usage:
    python m8_3_1.py
"""
def safe_divide(numerator: float, denominator: float) -> float|int:
    """Attempts to divide two numbers, handling errors gracefully.

    This function takes two arguments, a numerator and a denominator, 
    and attempts to divide them.
    If the denominator is zero, the function raises a ZeroDivisionError.
    If the numerator or denominator is not a number, the function raises a TypeError.
    Otherwise, the function returns the result of the division.

    Args:
        numerator: The numerator of the division.
        denominator: The denominator of the division.

    Returns:
        The result of the division, or None if an error occurred.
    """
    result = None
    try:
        try:
            if isinstance(denominator, str) and denominator.lower() == 'zero':
                raise ZeroDivisionError(f"Raised by {denominator=}, it equals 0")

            if denominator == '0':
                print(f"# intentionally trigger IndexError by calling {denominator[3]}")

            num = float(numerator)
            denom = float(denominator)
            result = num / denom

        except ZeroDivisionError as err:
            print(f"#   -=Caught {err.__class__.__name__}:{err.args}!")
        except ValueError as err:
            print(f"#   -=Caught {err.__class__.__name__}:{err.args} on line"
                  f"{err.__traceback__.tb_lineno}, will raise TypeError")
            raise TypeError("Re-Raise ValueError as TypeError") from err
        except Exception as err:
            print(f"#   -=Caught {err.__class__.__name__}:{err.args} when"
                  f" {denominator=} on line {err.__traceback__.tb_lineno}")
            err.add_note("caught by inner except, re-raise.")
            raise
        else:
            print(f"#  got division {result=}")
            if (isinstance(numerator, int) and isinstance(denominator, int)
                and not numerator % denominator):
                result = int(result)
                print(f"# intentionally trigger TypeError by calling {denominator[1]}")

    except TypeError as err:
        print(f"#  -Caught {err.__class__.__name__}:{err.args};"
              f" Originally triggered by {repr(err.__cause__)}")
    except IndexError as err:
        note_text = f"with Added Notes {err.__notes__}" if hasattr(err, '__notes__') else ''
        print(f"#  Error {repr(err)}, on line"
              f" {err.__traceback__.tb_lineno} {note_text}"
              f" Originally triggered by {repr(err.__cause__)}")
    except Exception as err:
        print(f"# !!Unexpected Error {repr(err)}")

    return result

def main(list_of_numbers_to_try: list[int]) -> None:
    """main func demo sending different denominators to safe_divide.
    
    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call safe_divide.
    """
    a = 4
    for b in list_of_numbers_to_try:
        print(f"#Trying {b}...")
        print(f"# {safe_divide(a, b)=}")

    print("#program continues..")


if __name__ == "__main__":
    denominators_to_try = ['zero', 0, '8.3.1', 1, '0', 5]
    main(denominators_to_try)

#Trying zero...
#   -=Caught ZeroDivisionError:("Raised by denominator='zero', it equals 0",)!
# safe_divide(a, b)=None
#Trying 0...
#   -=Caught ZeroDivisionError:('float division by zero',)!
# safe_divide(a, b)=None
#Trying 8.3.1...
#   -=Caught ValueError:("could not convert string to float: '8.3.1'",) on line32, will raise TypeError
#  -Caught TypeError:('Reraise ValueError as TypeError',); Originally triggered by ValueError("could not convert string to float: '8.3.1'")
# safe_divide(a, b)=None
#Trying 1...
#  got division result=4.0
#  -Caught TypeError:("'int' object is not subscriptable",); Originally triggered by None
# safe_divide(a, b)=4
#Trying 0...
#   -=Caught IndexError:('string index out of range',) when denominator='0' on line 29
#  Error IndexError('string index out of range'), on line 29 with Added Notes ['caught by inner except, re-raise.'] Originally triggered by None
# safe_divide(a, b)=None
#Trying 5...
#  got division result=0.8
# safe_divide(a, b)=0.8
#program continues..
