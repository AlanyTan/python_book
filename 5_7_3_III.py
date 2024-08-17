names = ["Albert", "Betty", "Charlie", "Doris", "Edward", "Fiona"]
age = [31, 18, 29, 17, 26, 19]
gender = ["Male", "Female", "Make", "Female", "Male", "Female"]
math_score = [95, 96, 94, 83, 82, 86]
cs_score = [89, 90, 92, 91, 90, 93]
student_records = zip(names, age, gender, math_score, cs_score)
for student_record in student_records:
    print("# {:10}{:3}\t{:8}{:3}\t{}".format(*student_record))
# Albert     31	Male     95	89
# Betty      18	Female   96	90
# Charlie    29	Make     94	92
# Doris      17	Female   83	91
# Edward     26	Male     82	90
# Fiona      19	Female   86	93
