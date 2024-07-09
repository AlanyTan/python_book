"""Test functions within this package

Usage:
    python -m m6_3_package.m6_3_2_geometry
"""

from . import rectangle
from . import circle
def main():
    print (f"testing circle {circle.area(3)}")
    print (f"testing circle {circle.circumference(3)}")
    print (f"testing circle {rectangle.area(3)}")
    print (f"testing circle {rectangle.perimeter(3)}")


    
if __name__ == "__main__":
    main()
