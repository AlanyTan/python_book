def safe_divide(numerator: float, denominator: float) -> float:
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
    a = 4
    b = 0
    print(f"# {safe_divide(a, b)=}")
    print(f"# program continues..")
    
if __name__ == "__main__":
    main()

#Error cannot divide!
# safe_divide(a, b)=None
# program continues..
