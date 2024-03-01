import csv

def main(file_name: str) -> None:
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    csv_writer = csv.writer(csv_file_obj, dialect='excel')
    print(f"# open csv for {csv_file_obj.mode}, use {type(csv_writer)=}")
    csv_writer.writerow(['ID', 'Name', 'Age', 'Grade', 'Pass/Fail'])
    csv_writer.writerow([1, 'Alice', 18, 80.5, 'True'])
    csv_writer.writerow([2, 'Bob', 19, 70, 'True'])
    csv_writer.writerow([3, 'Carole', 17, 75, 'True'])
    csv_writer.writerow([4, 'David', 18, 85.5, 'True'])
    csv_file_obj.close()


    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    csv_reader = csv.reader(csv_file_obj, dialect='excel')
    print(f"# open csv for {csv_file_obj.mode}, use {type(csv_reader)=}")
    for row in csv_reader:
        print("#", row)
        
    csv_file_obj.close()

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

# open csv for w, use type(csv_writer)=<class '_csv.writer'>
# open csv for r, use type(csv_reader)=<class '_csv.reader'>
# ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
# ['1', 'Alice', '18', '80.5', 'True']
# ['2', 'Bob', '19', '70', 'True']
# ['3', 'Carole', '17', '75', 'True']
# ['4', 'David', '18', '85.5', 'True']
    