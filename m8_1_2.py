"""Demo try-except with catching specific exceptions.

Usage: 
    python -m m8_1_2
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

def safe_divide(numerator: int|float, denominator: int|float) -> float|int:
    """division with data checking before the / operation.

    This version also tries to return integer if numerator is divisible 
    by denominator. The data type checking also reports type of error 
    including ievide by zero and numerator, denominator type error.

    Args:
        numerator: number to be divided.
        denominator: number to be divided by. 
    
    Returns:
        the quotient as int if divisible, or quotient as float if not,
        if both numerator and denominator are numbers and denominator is not 0,
        otherwise return None.
    """
    result = None
    try:
        logger.debug(f"trying to divide {numerator} / {denominator}...")
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        logger.info(f"  calculated {numerator}/{denominator} = {result}.")
        if (not numerator % denominator):
            result = int(result)

    except ZeroDivisionError as e:
        logger.error(f"  DivideByZeroError {e.args}"
                     f", line {e.__traceback__.tb_lineno}")
    except ValueError as e:
        logger.error(f"  ValueError {e.args}"
                     f", line {e.__traceback__.tb_lineno}")
    except Exception as e:
        logger.error(f"  Unexpected Exception: {repr(e)}"
                     f", line {e.__traceback__.tb_lineno}")
    except:
        logger.critical("#  A rare unknown error has occurred, skipping divide")
        exit(-1)

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

if __name__ == "__main__":
    denominators_to_try = [ 0, '1', '8.1.2', 2, 5]
    main(denominators_to_try)

#DEBUG - __main__(m8_1_2.py:30) - trying to divide 4 / 0...
#ERROR - __main__(m8_1_2.py:39) -   DivideByZeroError ('float division by zero',), line 33
# safe_divide(a, b)=None
#DEBUG - __main__(m8_1_2.py:30) - trying to divide 4 / 1...
#INFO - __main__(m8_1_2.py:34) -   calculated 4/1 = 4.0.
#ERROR - __main__(m8_1_2.py:45) -   Unexpected Exception: TypeError("unsupported operand type(s) for %: 'int' and 'str'"), line 35
# safe_divide(a, b)=4.0
#DEBUG - __main__(m8_1_2.py:30) - trying to divide 4 / 8.1.2...
#ERROR - __main__(m8_1_2.py:42) -   ValueError ("could not convert string to float: '8.1.2'",), line 32
# safe_divide(a, b)=None
#DEBUG - __main__(m8_1_2.py:30) - trying to divide 4 / 2...
#INFO - __main__(m8_1_2.py:34) -   calculated 4/2 = 2.0.
# safe_divide(a, b)=2
#DEBUG - __main__(m8_1_2.py:30) - trying to divide 4 / 5...
#INFO - __main__(m8_1_2.py:34) -   calculated 4/5 = 0.8.
# safe_divide(a, b)=0.8
