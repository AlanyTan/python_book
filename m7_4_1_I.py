"""Demo manually process CSV file contents.

Will write then read back a list of list (can be tuple of tuple as well.)
Uses repr to realize quote only strings. 
While reading, cell with quotationmarks will be convert to str, cells without 
quotation marks will be treated as bool or number.

Usage:
    python -m m7_4_1_I

Note:
    This module cannot handle nested quotation marks, escape characters,
    and ill formed float number (i.e. unquoted 1.1.1 will cause an error).
"""
SAMPLE_DATA = [
    ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'],
    [1, 'Zhang, Alice', 18, 80.5, True],
    [2, 'Yusuf, Bob', 19, 70, True],
    [3, 'Xanders, Carole', 17, 55, False],
    [4, 'West, David', 18, 85.5, True]
]
QUOTE = "'"
DELIMINATOR = ','

def convert_to_csv(obj: any = None) -> str:
    """convert a 2-d iterable object to string of csv.

    This function uses repr() to represent each object within obj. 
    So strings will be quoted using single quotation marks (unless 
    the string contains quotation marks), numbers, bools and None 
    are not quoted.
    
    Args: 
        obj: a 2-d iterable, of which outer iterable is used as row
            while inner iterable is interpreted as cell.
    
    Returns:
        a string representation of obj in which newline is the seperation of rows
        and DELIMATOR is used as seperator of cells.
    """
    if obj is None:
        obj = SAMPLE_DATA
    cs_list = []
    for row in obj:
        cs_list.append(DELIMINATOR.join(map(repr,row)))

    return "\n".join(cs_list)+"\n"

def convert_from_csv(csv: str) -> list[list]:
    """convert a string representing csv to list of lists.
    
    This function parse string csv, split by \n to rows and then split by , to 
    cells, it will respect quotation marks QUOTE do not use \n and , within QUOTE 
    to split. It does not handle quotation marks within quotation marks though, it
    does not handle escape sequence either. 
    
    Args:
        csv: string representing the content of a csv file.
    
    Returns:
        a list of lists, outer list represent rows, inner list represent cells.
    """
    def str_to_obj(element: str) -> any:
        match element:
            case 'True'|'False':
                  return element == 'True'
            case n if n.isdigit():
                return int(n)
            case s if s.startswith(QUOTE):
                return element.strip(QUOTE)
            case f if f[0].isdigit():
                return float(f)

    not_in_quote = True
    list_of_list = []
    inner_list = []
    current_element = ''
    for char in csv:
        match char:
            case qt if qt == QUOTE:
                not_in_quote = not not_in_quote
                current_element += qt
            case dl if dl == DELIMINATOR and not_in_quote:
                inner_list.append(str_to_obj(current_element))
                current_element = ''
            case "\n" as nl if not_in_quote:
                inner_list.append(str_to_obj(current_element))
                current_element = ''
                list_of_list.append(inner_list)
                inner_list = []
            case _ as c:
                current_element += c
    
    return list_of_list


def main(file_name: str) -> None:
    """main func demo write/read csv file manually. 
    
    Args:
        file_name: name of the file to use as csv file.

    """
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    csv_file_obj.write(convert_to_csv())
    csv_file_obj.close()

    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    csv_content = convert_from_csv(csv_file_obj.read())
    for row in csv_content:
        print("#", row)
    csv_file_obj.close()

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# [1, 'Zhang, Alice', 18, 80.5, True]
# [2, 'Yusuf, Bob', 19, 70, True]
# [3, 'Xanders, Carole', 17, 55, False]
# [4, 'West, David', 18, 85.5, True]
