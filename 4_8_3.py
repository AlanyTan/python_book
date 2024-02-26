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
        sendback = yield current
        if sendback is not None:
            current = sendback - step
        current += step
        
regular = counter(100)
senior = counter(50)
    
while (user_input := input("# Enter age, 'exit' to quit:")) != 'exit':
    match user_input:
        case str(x) if x.isnumeric() and int(x) > 65:
            seq_number = f"S{next(senior):02d}"
        case str(x) if x.isnumeric() and int(x) < 65:
            seq_number = f"R{next(regular):03d}"
        case str(x) if x.startswith("SetS"):
            new_number = int(x[5:])
            seq_number = f"S{senior.send(new_number):02d}"
        case str(x) if x.startswith("SetR"):
            new_number = int(x[5:])
            seq_number = f"R{regular.send(new_number):03d}"
        case _:
            print(f"###Err un-cased input: {user_input}")
        
    print(f"#Main: sequence nubmer is: {seq_number}")

# Enter age, 'exit' to quit:50
#Main: sequence nubmer is: R000
# Enter age, 'exit' to quit:70
#Main: sequence nubmer is: S00
# Enter age, 'exit' to quit:SetR 32
#Main: sequence nubmer is: R032
# Enter age, 'exit' to quit:72
#Main: sequence nubmer is: S01
# Enter age, 'exit' to quit:40
#Main: sequence nubmer is: R033
# Enter age, 'exit' to quit:exit
