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
        yield current
        current += step
        
regular = counter(100)
senior = counter(50)
    
while (user_input := input("# Enter age, 'exit' to quit:")) != 'exit':
    if user_input.isnumeric() and int(user_input) >= 65:
        seq_number = f"S{next(senior):02d}"
    else:
        seq_number = f"R{next(regular):03d}"
    print(f"#Main: sequence nubmer is: {seq_number}")

# Enter age, 'exit' to quit:50
#Main: sequence nubmer is: R000
# Enter age, 'exit' to quit:60
#Main: sequence nubmer is: R001
# Enter age, 'exit' to quit:70
#Main: sequence nubmer is: S00
# Enter age, 'exit' to quit:80
#Main: sequence nubmer is: S01
# Enter age, 'exit' to quit:40
#Main: sequence nubmer is: R002
# Enter age, 'exit' to quit:exit
