string_1 = "abcde\tfghij\nklmno"
print("'''","\n" + string_1,"\n'''")
''' 
abcde	fghij
klmno 
'''

string_r1 = r"abcde\tfghij\nklmno"
print("'''\nusing \"" + string_r1 + "\" can get " + "\n" + string_1, "\n'''")
'''
using "abcde\tfghij\nklmno" can get 
abcde	fghij
klmno 
'''

dir_path = r"C:\Users\python\book"
book_filename = "\120\x79\x74\x68\x6f\x6e\u7a0b\u5e8f\u8bbe\u8ba1"
book_fileext = ".pdf"
print("# file full path:", dir_path + "\\" + book_filename + book_fileext)
# file full path: C:\Users\python\book\Python程序设计.pdf
