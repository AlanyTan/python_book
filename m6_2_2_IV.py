#save this as m6_2_2_IV.py
from m6_2_2_II_circle import area as circle_area, circumference

print(f"# {'PI' in dir()=}, {'radius' in dir()=}")
# 'PI' in dir()=False, 'radius' in dir()=False

radius = 3
print(f"# {'radius' in dir()=}, {radius=}")
# 'radius' in dir()=True, radius=3

print(f"# {'circumference' in dir()=}, {circumference(radius)=}")
# 'circumference' in dir()=True, circumference(radius)=18.849555900000002

print(f"# {'area' in dir()=}, {'circle_area' in dir()=},"
      f" {circle_area(radius)=}")
# 'area' in dir()=False,'circle_area' in dir()=True, circle_area(radius)=28.27433385


from m6_2_2_II_circle import PI
print(f"# {'PI' in dir()=}, {PI=}")
# 'PI' in dir()=True, PI=3.14159265
