def func_local_scope(arg_l: str) -> str:
    """Demonstrate variable's local scope
    
    Args:
        arg_l: an argument used to demonstrate arguments are local scoped
        
    Returns:
        A string that was the value of the local variable.
    """

    local_var = 'locv'
    print(f"# -in func_local_scope, arg_l exist: {'arg_l' in dir()}, {arg_l=}")
    print(f"# -in func_local_scope, local_var exist: {'local_var' in dir()}"
          f", {local_var=}")
    return local_var


print(f"# in main, {func_local_scope('anything')=}")
# -in func_local_scope, arg_l exist: True, arg_l='anything'
# -in func_local_scope, local_var exist: True, local_var='locv'
# in main, func_local_scope('anything')='locv'

print(f"# in main, arg_l exist: {'arg_l' in dir()}"
      f", local_var exist: {'local_var' in dir()}")
# in main, arg_l exist: False, local_var exist: False
