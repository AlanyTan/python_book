int_1 = 31243

format_sp = 'c'
print("#", format(int_1,format_sp), "=", f"{int_1:c}")
# 程 = 程

format_sp = '#0o'
print("#", format(int_1, format_sp), "=", f"{int_1:{format_sp}}")
# 0o75013 = 0o75013
