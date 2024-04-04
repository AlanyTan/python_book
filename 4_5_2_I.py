def func_parent_scope(arg_p: str) -> str:
    """Demonstrate enclosing scope reading

    Args:
        arg_p: argument to parent function

    Returns:
        the string returned by func_child which should be the 
            value of local_var
    """
    enclosing_var = 'encv'
    def func_child_scope(arg_c: int) -> str:
        local_var = 'locv'
        print(f"#  -=func_child, arg_c exist: {'arg_c' in dir()}, {arg_c=}")
        print(f"#  -=func_child, arg_p exist: {'arg_p' in dir()}, {arg_p=}")
        print(f"#  -=func_child, local_var exist: {'local_var' in dir()}"
              f", {local_var=}")
        print(f"#  -=func_child, enclosing_var exist:"
              f" {'enclosing_var' in dir()}, {enclosing_var=}")
        return local_var
    
    print(f"# -func_parent, arg_p exist: {'arg_p' in dir()}, {arg_p=}")
    print(f"# -func_parent, enclosing_var exist: {'enclosing_var' in dir()},"
          f" {enclosing_var=}")
    print(f"# -func_parent, arg_c exist: {'arg_c' in dir()}")
    print(f"# -func_parent, local_var exist: {'local_var' in dir()},")
    return func_child_scope('from parent')

print(f"# func returned:", func_parent_scope("from main"))
# -func_parent, arg_p exist: True, arg_p='from main'
# -func_parent, enclosing_var exist: True, enclosing_var='encv'
# -func_parent, arg_c exist: False
# -func_parent, local_var exist: False,
#  -=func_child, arg_c exist: True, arg_c='from parent'
#  -=func_child, arg_p exist: True, arg_p='from main'
#  -=func_child, local_var exist: True, local_var='locv'
#  -=func_child, enclosing_var exist: True, enclosing_var='encv'
# func returned: locv

print(f"# outside, arg_p exist: {'arg_p' in dir()}")
# outside, arg_p exist: False

print(f"# outside, local_var exist: {'local_var' in dir()}")
# outside, local_var exist: False    

print(f"# outside, enclosing_var exist: {'enclosing_var' in dir()}")
# outside, enclosing_var exist: False
