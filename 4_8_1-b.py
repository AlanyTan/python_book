def counter(arg_1:int, arg_2:int = None, step:int = 1):
    if arg_2 is None:
        current = 0
        stop = arg_1
    else:
        current = arg_1
        stop = arg_2
        
    sign = 1 if current < stop else -1
    if step*sign < 0:
        current = stop - step 
    
    while current * sign < stop * sign:
        print(f"# - in generator {current=}")
        yield current
        current += step

counter_gen = counter(-5, -10, -1)
    
for i in counter_gen:
    print(f"#main received:{i}")

#seq_nos is a <class 'generator'>
# - in generator current=-5
#main received:-5
# - in generator current=-6
#main received:-6
# - in generator current=-7
#main received:-7
# - in generator current=-8
#main received:-8
# - in generator current=-9
#main received:-9
