import csv

def main(file_name: str) -> None:
    csv_file_obj = open(file_name, "w", newline='', encoding='utf-8')
    fieldnames = ['ID', 'Name', 'Age', 'Grade', 'Pass/Fail']
    csv_writer = csv.DictWriter(csv_file_obj, fieldnames, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    print(f"# open csv for {csv_file_obj.mode}, use {type(csv_writer)=}")
    csv_writer.writeheader()
    csv_writer.writerow({'ID':1, 'Name':'Alice', 'Age':18, 'Grade':80.5, 'Pass/Fail':str(True)})
    csv_writer.writerow({'ID':2, 'Name':'Bob', 'Age':19, 'Grade':70, 'Pass/Fail':str(True)})
    csv_writer.writerow({'ID':3, 'Name':'Carole', 'Age':17, 'Grade':75, 'Pass/Fail':str(True)})
    csv_writer.writerow({'ID':4, 'Name':'David', 'Age':18, 'Grade':85.5, 'Pass/Fail':str(True)})
    csv_file_obj.close()


    csv_file_obj = open(file_name, "r", newline='', encoding='utf-8')
    csv_reader = csv.DictReader(csv_file_obj, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
    print(f"# open csv for {csv_file_obj.mode}, use {type(csv_reader)=}")
    for row in csv_reader:
        print("#", row)
        
    csv_file_obj.close()

if __name__ == '__main__':
    base_name = __file__[:-3]
    file_name = (base_name + ".data.csv")
    main(file_name)

# open csv for w, use type(csv_writer)=<class 'csv.DictWriter'>
# open csv for r, use type(csv_reader)=<class 'csv.DictReader'>
# {'ID': 1.0, 'Name': 'Alice', 'Age': 18.0, 'Grade': 80.5, 'Pass/Fail': 'True'}
# {'ID': 2.0, 'Name': 'Bob', 'Age': 19.0, 'Grade': 70.0, 'Pass/Fail': 'True'}
# {'ID': 3.0, 'Name': 'Carole', 'Age': 17.0, 'Grade': 75.0, 'Pass/Fail': 'True'}
# {'ID': 4.0, 'Name': 'David', 'Age': 18.0, 'Grade': 85.5, 'Pass/Fail': 'True'}
