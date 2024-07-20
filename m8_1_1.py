"""Demo try-except structure by capture divided by 0.

Usage:
    python -m m8_1_1
"""
def safe_divide(numerator: float, denominator: float) -> float:
    """division with data checking before the / operation.

    Args:
        numerator: number to be divided.
        denominator: number to be divided by. 
    
    Returns:
        the quotient as float if both numerator and denominator 
        are numbers and denominator is not 0. 
        otherwise return None.
    """
    result = None
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        print(f"#   calculated {numerator}/{denominator} = {result}.")
    except:
        print("#Error cannot divide!")

    return result

def main() -> None:
    """main func demo seding 0 as denominator to safe_divide."""
    a = '4'
    b = 0
    print(f"# {safe_divide(a, a)=}")
    print(f"# {safe_divide(a, b)=}")
    print("# program continues..")

if __name__ == "__main__":
    main()

#   calculated 4/4 = 1.0.
# safe_divide(a, a)=1.0
#Error cannot divide!
# safe_divide(a, b)=None
# program continues..
