def func_parent_scope(arg_p: str) -> str:
    enclosing_var = 'encv'
    enc_var_alias = enclosing_var
    def func_child_scope(arg_c: int) -> int:
        nonlocal enclosing_var
        enclosing_var = "value from child"
        local_var = 'locv'
        return arg_c

    print(f"# -func_parent, {enclosing_var is enc_var_alias=}, {enclosing_var=}")
    func_child_scope(0)
    print(f"# -func_parent, {enclosing_var is enc_var_alias=}, {enclosing_var=}")
    return arg_p[:3]

print(f"# func returned:", func_parent_scope("anything"))
# -func_parent, enclosing_var is enc_var_alias=True, enclosing_var='encv'
# -func_parent, enclosing_var is enc_var_alias=False, enclosing_var='value from child'
# func returned: any
