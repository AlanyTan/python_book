from collections.abc import Generator

def counter(arg_1:int, arg_2:int = None, step:int = 1) -> Generator[int]:
    """A counter generator with start, stop, step parameters.

    Args:
        arg_1: if used by itself, is before which the counter should stop
            if used with arg_2, is where the counter should start.
        arg_2: if provided, is before which the counter should stop.
        step: the step size between each yield.
    
    Yields:
        a the current counter number
    """
    if arg_2 is None:
        start = 0
        stop = arg_1
    else:
        start = arg_1
        stop = arg_2
        
    sign = 1 if start < stop else -1
    if step*sign < 0:
        current = stop - step 
    else:
        current = start
    
    while current * sign < stop * sign:
        print(f"# -in generator {current=}")
        yield current
        current += step

counter_gen = counter(-5, -10, -1)
    
for i in counter_gen:
    print(f"# main received:{i}")

# -in generator current=-5
# main received:-5
# -in generator current=-6
# main received:-6
# -in generator current=-7
# main received:-7
# -in generator current=-8
# main received:-8
# -in generator current=-9
# main received:-9
