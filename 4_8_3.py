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
    if user_input.isnumeric() and int(user_input) >= 65:
        seq_number = f"S{next(senior):02d}"
    elif user_input[:3] == 'Set':
        if user_input[5:].isnumeric():
            new_number = int(user_input[5:])
            if user_input[3] == 'S':
                seq_number = f"S{senior.send(new_number):02d}"
                print("set", seq_number)
            elif user_input[3] == 'R':
                seq_number = f"R{regular.send(new_number):03d}"

        else:
            seq_number = "Reset without valid number"
                
    else:
        seq_number = f"R{next(regular):03d}"
    print(f"#Main: sequence nubmer is: {seq_number}")

# Enter age, 'exit' to quit:SetR 20
#Main: sequence nubmer is: R020
# Enter age, 'exit' to quit:67
#Main: sequence nubmer is: S00
# Enter age, 'exit' to quit:99
#Main: sequence nubmer is: S01
# Enter age, 'exit' to quit:40
#Main: sequence nubmer is: R021
# Enter age, 'exit' to quit:
