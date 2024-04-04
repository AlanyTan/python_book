def func_parent_scope(arg_p: str) -> str:
    """Demonstrate global scope.

    Args:
        arg_p: arguments from main to parent function. 

    Returns:
        the incoming argument arg_p repeated
    """
    global_var = 'in func_parent'
    print(f"# -func_parent, {global_var_alias=}, {global_var=}")
    def func_child_scope(arg_c: int) -> int:
        global global_var
        print(f"# -=func_child, {global_var is global_var_alias=}, {global_var=}")
        global_var = "value from child"
        print(f"# -=func_child, {global_var_alias=}, {global_var=}")
        return arg_c

    return_from_func_child = func_child_scope(2)
    print(f"# -func_parent, {global_var_alias=}, {global_var=}")
    return arg_p * return_from_func_child

global_var = 'in main'
global_var_alias = global_var
print(f"# func returned: {func_parent_scope('called from main.')}, {global_var=}" )
# -func_parent, global_var_alias='in main', global_var='in func_parent'
# -=func_child, global_var is global_var_alias=True, global_var='in main'
# -=func_child, global_var_alias='in main', global_var='value from child'
# -func_parent, global_var_alias='in main', global_var='in func_parent'
# func returned: called from main.called from main., global_var='value from child'
