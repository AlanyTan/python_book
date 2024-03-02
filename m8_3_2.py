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
        try:
            sendback = yield current
            if sendback is not None:
                    current = sendback - step
        except Exception as e:
            print(f"#  Generator received Exception <{e}> from caller.")

        else:
            current += step
        
regular = counter(100)
senior = counter(50)

def main() -> None: 
    while (user_input := input("# Enter age, 'exit' to quit:")) != 'exit':
        match user_input:
            case x if x.isnumeric() and int(x) > 65:
                seq_number = f"S{next(senior):02d}"
            case x if x.isnumeric() and int(x) < 65:
                seq_number = f"R{next(regular):03d}"
            case x if x.startswith("SetS"):
                new_number = int(x[5:])
                seq_number = f"S{senior.send(new_number):02d}"
            case x if x.startswith("SetR"):
                new_number = int(x[5:])
                seq_number = f"R{regular.send(new_number):03d}"
            case x if x.startswith("ErrS"):
                seq_number = f"S{senior.throw(Exception('caller sent error')):02d}"
            case x if x.startswith("ErrR"):
                seq_number = f"R{regular.throw(Exception('caller sent error')):03d}"
            case _:
                print(f"###Err un-cased input: {user_input}")
            
        print(f"#Main: sequence nubmer is: {seq_number}")
if __name__ == "__main__":
    main()
    
# Enter age, 'exit' to quit:50
#Main: sequence nubmer is: R000
# Enter age, 'exit' to quit:60
#Main: sequence nubmer is: R001
# Enter age, 'exit' to quit:70
#Main: sequence nubmer is: S00
# Enter age, 'exit' to quit:ErrR
#  Generator received Exception <caller sent error> from caller.
#Main: sequence nubmer is: R001
# Enter age, 'exit' to quit:ErrR
#  Generator received Exception <caller sent error> from caller.
#Main: sequence nubmer is: R001
# Enter age, 'exit' to quit:70
#Main: sequence nubmer is: S01
# Enter age, 'exit' to quit:40
#Main: sequence nubmer is: R002
# Enter age, 'exit' to quit:exit
