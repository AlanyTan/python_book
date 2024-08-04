""" main file for demo running package as main module """
from . import logger

from .. import m6_3_2_geometry as geometry

def main():
    print (f"testing circle {geometry.circle.area(3)}")
    print (f"testing circle {geometry.circle.circumference(3)}")
    print (f"testing circle {geometry.rectangle.area(3)}")
    print (f"testing circle {geometry.rectangle.perimeter(3)}")

if __name__ == "__main__":
    main()
