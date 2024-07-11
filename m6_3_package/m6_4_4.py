"""Test functions within this package

Usage:
    python -m m6_3_package.m6_3_2_geometry
"""

if __package__:
    from .m6_3_2_geometry.rectangle import perimeter
    from .module_1 import func_in_mod_1
else:
    from m6_3_2_geometry.rectangle import perimeter
    from module_1 import func_in_mod_1
#  in m6_3_package __init__.py
#   in m6_3_2_package/m6_3_2_geometry/__init__.py ['CONST_1', 'circle', 'perimeter', 'rectangle']
#  in m_package module_1.py ['var_mod_1']

    
def main():
    print(f"# testing circle {perimeter(3)}")
    print(f"# testing func_in_mod_1 {func_in_mod_1()}")


if __name__ == "__main__":
    main()
# testing circle 12
# testing func_in_mod_1 inside module_1 func_in_mod_1
