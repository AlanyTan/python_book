"""Module for safe division and a main function to test them.

Usage:
    python m8_3_1.py
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

def safe_divide(numerator: float, denominator: float) -> float|int:
    """Attempts to divide two numbers, handling errors gracefully.

    This function takes two arguments, a numerator and a denominator, 
    and attempts to divide them.
    If the denominator is zero, the function raises a ZeroDivisionError.
    If the numerator or denominator is not a number, raises a TypeError.
    Otherwise, the function returns the result of the division.

    Args:
        numerator: The numerator of the division.
        denominator: The denominator of the division.

    Returns:
        The result of the division, or None if an error occurred.
    """
    result = None
    try:
        logger.debug(f"Trying {numerator=} / {denominator=}")
        try:
            if isinstance(denominator, str) and denominator.lower() == 'zero':
                logger.debug(f"{denominator=} equals 0, raise ZeroDivErr")
                raise ZeroDivisionError(f"Raised by {denominator=}, equals 0")

            if denominator == '0':
                logger.info(f"# intentionally trigger IndexError by calling"
                      f"{denominator[3]}")

            num = float(numerator)
            denom = float(denominator)
            result = num / denom

        except ZeroDivisionError as e:
            logger.error(f"  DivideByZeroError {e.args}"
                         f", line {e.__traceback__.tb_lineno}")
        except ValueError as e:
            logger.error(f"  ValueError {e.args}"
                          f", line {e.__traceback__.tb_lineno}")
            raise TypeError("Re-Raise ValueError as TypeError") from e
        except Exception as e:
            logger.error(f"  Unexpected Exception: {repr(e)}"
                         f", line {e.__traceback__.tb_lineno}")
            e.add_note("caught by inner except, re-raise.")
            raise
        else:
            logger.info(f"  calculated {numerator}/{denominator} = {result}.")
            if (not num % denom):
                logger.info(f"divisible, converting {result=} to int")
                logger.info(f"# intentionally trigger TypeError by calling "
                            f"{denominator[1]}")
                result = int(result)

    except TypeError as e:
        logger.error(f" TypeError:{e.args}, line {e.__traceback__.tb_lineno};"
              f" Originally triggered by {repr(e.__cause__)}")
    except IndexError as e:
        note_text = f"with Added Notes {e.__notes__}" if hasattr(e,
                                                            '__notes__') else ''
        logger.error(f"Error {repr(e)}, on line"
              f" {e.__traceback__.tb_lineno} {note_text}"
              f" Originally triggered by {repr(e.__cause__)}")
    except Exception as e:
        logger.error(f"# !!Unexpected Error {repr(e)}"
                     f", line {e.__traceback__.tb_lineno}")

    return result

def main(list_of_numbers_to_try: list[int]) -> None:
    """main func demo sending different denominators to safe_divide.
    
    Args:
        list_of_numbers_to_try: a list containing numbers to be used
        as denominator when trying to call safe_divide.
    """
    a = 4
    for b in list_of_numbers_to_try:
        print(f"# {safe_divide(a, b)=}")

    print("#program continues..")


if __name__ == "__main__":
    denominators_to_try = ['zero', 0, '8.3.1', 1, '0', 5]
    main(denominators_to_try)

#DEBUG - __main__(m8_3_1.py:30) - Trying numerator=4 / denominator='zero'
#DEBUG - __main__(m8_3_1.py:33) - denominator='zero' equals 0, raise ZeroDivErr
#ERROR - __main__(m8_3_1.py:45) -   DivideByZeroError ("Raised by denominator='zero', equals 0",), line 34
# safe_divide(a, b)=None
#DEBUG - __main__(m8_3_1.py:30) - Trying numerator=4 / denominator=0
#ERROR - __main__(m8_3_1.py:45) -   DivideByZeroError ('float division by zero',), line 42
# safe_divide(a, b)=None
#DEBUG - __main__(m8_3_1.py:30) - Trying numerator=4 / denominator='8.3.1'
#ERROR - __main__(m8_3_1.py:48) -   ValueError ("could not convert string to float: '8.3.1'",), line 41
#ERROR - __main__(m8_3_1.py:65) -  TypeError:('Re-Raise ValueError as TypeError',), line 50; Originally triggered by ValueError("could not convert string to float: '8.3.1'")
# safe_divide(a, b)=None
#DEBUG - __main__(m8_3_1.py:30) - Trying numerator=4 / denominator=1
#INFO - __main__(m8_3_1.py:57) -   calculated 4/1 = 4.0.
#INFO - __main__(m8_3_1.py:59) - divisible, converting result=4.0 to int
#ERROR - __main__(m8_3_1.py:65) -  TypeError:("'int' object is not subscriptable",), line 61; Originally triggered by None
# safe_divide(a, b)=4.0
#DEBUG - __main__(m8_3_1.py:30) - Trying numerator=4 / denominator='0'
#ERROR - __main__(m8_3_1.py:52) -   Unexpected Exception: IndexError('string index out of range'), line 38
#ERROR - __main__(m8_3_1.py:70) - Error IndexError('string index out of range'), on line 38 with Added Notes ['caught by inner except, re-raise.'] Originally triggered by None
# safe_divide(a, b)=None
#DEBUG - __main__(m8_3_1.py:30) - Trying numerator=4 / denominator=5
#INFO - __main__(m8_3_1.py:57) -   calculated 4/5 = 0.8.
# safe_divide(a, b)=0.8
#program continues..
