"""Test functions within this package

Usage:
    python -m m6_3_package
"""
"""save this as m6_3_package/__main__.py"""

from . import circle, rectangle
def main():
    print (f"testing circle {circle.area(3)}")
    print (f"testing circle {circle.circumference(3)}")
    print (f"testing circle {rectangle.area(3)}")
    print (f"testing circle {rectangle.perimeter(3)}")


    
if __name__ == "__main__":
    main()
