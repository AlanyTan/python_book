"""Module containing a counter generator supports .throw.

The generator yields the next number in the sequence each time it is called.
If the caller throws an exception, the generator will repeat the previous yield.

The main function takes user input and uses the counter generators to generate sequence numbers.
The user can enter an age, and the function will generate a sequence number from either regular or senior generator based on the age.
The user can also enter commands to set the current count or to trigger an error in the generator.

Usage:
    python m8_3_2.py
"""
def counter(arg_1:int, arg_2:int = None, step:int = 1):
    """A counter generator with start, stop, step parameters.

    Args:
        arg_1: if used by itself, is before which the counter should stop
            if used with arg_2, is where the counter should start.
        arg_2: if provided, is before which the counter should stop.
        step: the step size between each yield.
    
    Yields:
        a the current counter number.
    
    Sends:
        set next count to this number.

    Throws:
        triggers error inside the counter generator, cause it to 
        repeat previous yield.
    """
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

regular = counter(1000)
senior = counter(100)

def main() -> None:
    """Main function for the counter generator example.

    This function takes user input and uses the counter generators to 
    generate sequence numbers.
    The user can enter an age, and the function will generate a sequence 
    number from either regular or senior generator based on the age.
    The user can also enter commands to set the current count or to 
    trigger an error in the generator.

    Args:
        None

    Returns:
        None
    """
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
                seq_number = f"S{senior.throw(Exception('I lost previous number')):02d}"
            case x if x.startswith("ErrR"):
                seq_number = f"R{regular.throw(Exception('I lost previous number')):03d}"
            case _:
                print(f"###Err un-cased input: {user_input}")

        print(f"#Main: sequence nubmer is: {seq_number}")
if __name__ == "__main__":
    main()

# Enter age, 'exit' to quit:50
#Main: sequence nubmer is: R000
# Enter age, 'exit' to quit:69
#Main: sequence nubmer is: S00
# Enter age, 'exit' to quit:79
#Main: sequence nubmer is: S01
# Enter age, 'exit' to quit:ErrR
#  Generator received Exception <I lost previous number> from caller.
#Main: sequence nubmer is: R000
# Enter age, 'exit' to quit:ErrR
#  Generator received Exception <I lost previous number> from caller.
#Main: sequence nubmer is: R000
# Enter age, 'exit' to quit:70
#Main: sequence nubmer is: S02
# Enter age, 'exit' to quit:ErrS
#  Generator received Exception <I lost previous number> from caller.
#Main: sequence nubmer is: S02
# Enter age, 'exit' to quit:80
#Main: sequence nubmer is: S03
# Enter age, 'exit' to quit:50
#Main: sequence nubmer is: R001
# Enter age, 'exit' to quit:exit
