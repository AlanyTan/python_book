"""Demo try-except structure by capture divided by 0.

Usage:
    python -m m8_1_1
"""

import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)9s\
 - %(filename)s:%(lineno)d  %(name)s.%(funcName)s() - %(message)s")
logger = logging.getLogger(__name__)


def safe_divide(numerator: float, denominator: float) -> float | None:
    """division with data checking before the / operation.

    Args:
        numerator: number to be divided.
        denominator: number to be divided by. 

    Returns:
        the quotient as float if both numerator and denominator are numbers
        and denominator is not 0. 
        otherwise return None.
    """
    result = None
    logger.debug("trying to divide %r / %r...", numerator, denominator)
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        logger.info("  calculated %s/%s = %s", num, denom, result)
    except:
        logger.error("#Error cannot divide %s / %s!", numerator, denominator)

    return result


def main() -> None:
    """main func demo seding 0 as denominator to safe_divide."""
    a = '4'
    b = 0
    print(f"# {safe_divide(a, a)=}")
    print(f"# {safe_divide(a, b)=}")
    print(f"# {safe_divide('a', a)=}")
    print("# program continues..")


if __name__ == "__main__":
    main()

#    DEBUG - m8_1_1.py:26 __main__.safe_divide() - trying to divide '4' / '4'...
#     INFO - m8_1_1.py:31 __main__.safe_divide() -   calculated 4.0/4.0 = 1.0
# safe_divide(a, a)=1.0
#    DEBUG - m8_1_1.py:26 __main__.safe_divide() - trying to divide '4' / 0...
#    ERROR - m8_1_1.py:33 __main__.safe_divide() - #Error cannot divide 4 / 0!
# safe_divide(a, b)=None
#    DEBUG - m8_1_1.py:26 __main__.safe_divide() - trying to divide 'a' / '4'...
#    ERROR - m8_1_1.py:33 __main__.safe_divide() - #Error cannot divide a / 4!
# safe_divide('a', a)=None
# program continues..
