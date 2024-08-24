"""Demo try-except-else structure with 'only do this part if no errors.

Usage:
    python -m m8_1_3
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)


def safe_divide(numerator: int | float, denominator: int | float
                ) -> float | int | None:
    """division with data checking before the / operation.

    This version moves converting to int into the -else clause of try-except.

    Args:
        numerator: number to be divided.
        denominator: number to be divided by. 

    Returns:
        the quotient as int if divisible, or quotient as float if not.
        otherwise return None.
    """
    result = None
    logger.debug("trying to divide %r / %r...", numerator, denominator)
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
    except ZeroDivisionError as e:
        logger.error("  Cannot divide by 0: %s, line %s",
                     e.args, e.__traceback__.tb_lineno)
    except (ValueError, ArithmeticError) as e:
        logger.error("  Incompatible value: %s, line %s",
                     e.args, e.__traceback__.tb_lineno)
    except Exception as e:
        logger.error("  Unexpected Exception: %r, line %s",
                     e, e.__traceback__.tb_lineno)
    else:
        logger.info("  calculated %s/%s = %s", num, denom, result)
        if not num % denom:
            logger.info("   divisible, converting %s to int", result)
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
    denominators_to_try = [0, '8.1.3', 2, '1', 5]
    main(denominators_to_try)

#DEBUG - __main__(m8_1_3.py:28) - trying to divide 4 / 0...
#ERROR - __main__(m8_1_3.py:34) -   Cannot divide by 0: ('float division by zero',), line 32
# safe_divide(a, b)=None
#DEBUG - __main__(m8_1_3.py:28) - trying to divide 4 / '8.1.3'...
#ERROR - __main__(m8_1_3.py:37) -   Incompatible value: ("could not convert string to float: '8.1.2'",), line 31
# safe_divide(a, b)=None
#DEBUG - __main__(m8_1_3.py:28) - trying to divide 4 / 2...
#INFO - __main__(m8_1_3.py:43) -   calculated 4.0/2.0 = 2.0
#INFO - __main__(m8_1_3.py:45) -    divisible, converting 2.0 to int
# safe_divide(a, b)=2
#DEBUG - __main__(m8_1_3.py:28) - trying to divide 4 / '1'...
#INFO - __main__(m8_1_3.py:43) -   calculated 4.0/1.0 = 4.0
#INFO - __main__(m8_1_3.py:45) -    divisible, converting 4.0 to int
# safe_divide(a, b)=4
#DEBUG - __main__(m8_1_3.py:28) - trying to divide 4 / 5...
#INFO - __main__(m8_1_3.py:43) -   calculated 4.0/5.0 = 0.8
# safe_divide(a, b)=0.8
