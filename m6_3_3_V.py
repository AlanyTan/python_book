"""Main script to demo import package"""
"""save this as m6_3_3_V.py"""
import m6_3_package.m6_3_2_geometry as geometry
#  in m6_3_package __init__.py
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'rectangle']
print("#=root level dir()", [d for d in dir() if not d.startswith('__')])
#=root level dir() ['geometry']
print("#=root level dir(geometry)", [d for d in dir(geometry) if not d.startswith('__')])
#=root level dir(geometry) ['CONST_1', 'circle', 'rectangle']

radius = 3
print(f"# area of {radius=} is {geometry.circle.area(radius)}")
# area of radius=3 is 28.27433385

length=4
print(f"# perimeter of square {length=} is "
      f" {geometry.rectangle.perimeter(length)}")
# perimeter of square length=4 is 16

print(f"# {'circle' in dir(geometry)=}\n"
      f"# {'rectangle' in dir(geometry)=}\n"
      f"# {'irregular' in dir(geometry)=}")
# 'circle' in dir(geometry)=True
# 'rectangle' in dir(geometry)=True
# 'irregular' in dir(geometry)=False
