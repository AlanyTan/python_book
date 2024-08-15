"""Demo try-except-else structure with 'only do this part if no errors.

Usage:
    python -m m8_1_3
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


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
        logger.debug(f"trying to divide {numerator} / {denominator}...")
        num = float(numerator)
        denom = float(denominator)
        result = num / denom            
    except ZeroDivisionError as e:
        logger.error(f"  DivideByZeroError {e.args}"
                     f", line {e.__traceback__.tb_lineno}")
    except ValueError as e:
        logger.error(f"  ValueError {e.args}"
                     f", line {e.__traceback__.tb_lineno}")
    except Exception as e:
        logger.error(f"  Unexpected Exception: {repr(e)}"
                     f", line {e.__traceback__.tb_lineno}")
    else:
        logger.info(f"  calculated {numerator}/{denominator} = {result}.")
        if (not num % denom):
            logger.info(f"divisible, converting {result=} to int")
            result = int(result)

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
    denominators_to_try = [ 0, '1', '8.1.3', 2, 5]
    main(denominators_to_try)

#DEBUG - __main__(m8_1_3.py:29) - trying to divide 4 / 0...
#ERROR - __main__(m8_1_3.py:34) -   DivideByZeroError ('float division by zero',), line 32
# safe_divide(a, b)=None
#DEBUG - __main__(m8_1_3.py:29) - trying to divide 4 / 1...
#INFO - __main__(m8_1_3.py:43) -   calculated 4/1 = 4.0.
#INFO - __main__(m8_1_3.py:45) - divisible, converting result=4.0 to int
# safe_divide(a, b)=4
#DEBUG - __main__(m8_1_3.py:29) - trying to divide 4 / 8.1.3...
#ERROR - __main__(m8_1_3.py:37) -   ValueError ("could not convert string to float: '8.1.3'",), line 31
# safe_divide(a, b)=None
#DEBUG - __main__(m8_1_3.py:29) - trying to divide 4 / 2...
#INFO - __main__(m8_1_3.py:43) -   calculated 4/2 = 2.0.
#INFO - __main__(m8_1_3.py:45) - divisible, converting result=2.0 to int
# safe_divide(a, b)=2
#DEBUG - __main__(m8_1_3.py:29) - trying to divide 4 / 5...
#INFO - __main__(m8_1_3.py:43) -   calculated 4/5 = 0.8.
# safe_divide(a, b)=0.8
