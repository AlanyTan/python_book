#save this as m6_2_3_III_v.py
import m6_2_3_II_package as geometry

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
