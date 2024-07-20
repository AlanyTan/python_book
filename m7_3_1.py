"""Module demonstrate read text file line by line with for loop.
When run as main, this module first call the m7_3_3.write_to_file()
to create a text file, then read every line of it using for loop.

Usage: 
    python -m m7_3_1

"""
from m7_2_3 import write_to_file

def main(file_name: str) -> None:
    """Demo using for loop to read every line of a text file
    
    Args:
        file_name: the name of the text file to read.
        
    Returns:
        None
    """
    file_r = open(file_name, 'r', encoding='utf-8')
    for line in file_r:
        print(f"# {line=}")

    file_r.close()

if __name__ == "__main__":
    base_name = __file__[:-3]
    file_name = base_name + ".data.txt"
    write_to_file(file_name, 't', 'utf-8')
    main(file_name)
# line='Python程序设计\n'
# line='2\n'
# line='False\n'
# line='A string literal.\n'
