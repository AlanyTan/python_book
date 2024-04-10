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
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        print(f"#   got the result.")
    except:
        print("#Error cannot divide!")
        
    return result

def main() -> None:
    """main func demo seding 0 as denominator to save_divide."""
    a = 4
    b = 0
    print(f"# {safe_divide(a, b)=}")
    print(f"# program continues..")
    
if __name__ == "__main__":
    main()

#Error cannot divide!
# safe_divide(a, b)=None
# program continues..
