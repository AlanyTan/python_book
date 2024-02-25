def func_parent_scope(arg_p: str) -> str:
    global_var = 'in func_parent'
    print(f"# -func_parent, {global_var_alias=}, {global_var=}")
    def func_child_scope(arg_c: int) -> int:
        global global_var
        print(f"# -=func_child, {global_var is global_var_alias=}, {global_var=}")
        global_var = "value from child"
        print(f"# -=func_child, {global_var_alias=}, {global_var=}")
        return arg_c

    func_child_scope(0)
    print(f"# -func_parent, {global_var_alias=}, {global_var=}")
    return arg_p[:3]

global_var = 'main flow'
global_var_alias = global_var
print(f"# func returned: {func_parent_scope("anything")}, {global_var=}" )
# -func_parent, global_var_alias='main flow', global_var='in func_parent'
# -=func_child, global_var is global_var_alias=True, global_var='main flow'
# -=func_child, global_var_alias='main flow', global_var='value from child'
# -func_parent, global_var_alias='main flow', global_var='in func_parent'
# func returned: any, global_var='value from child'
