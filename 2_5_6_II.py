string_1 = "\nabcde\"\t\"fghij\nklmno\' \'pqrst\n"
print("'''"+ string_1 + "'''")
'''
abcde"	"fghij
klmno' 'pqrst
'''

rstring_1 = r"\nabcde\"\t\"fghij\nklmno\' \'pqrst\n"
print("'''\nstring literal \"" + rstring_1 + "\" is actually: " +
      string_1 + "'''")
'''
string literal "\nabcde\"\t\"fghij\nklmno\' \'pqrst\n" is actually: 
abcde"	"fghij
klmno' 'pqrst
'''

dir_path = r"C:\Users\python\book"
book_filename = "\120\x79\x74\x68\x6f\x6e\u7a0b\u5e8f\u8bbe\u8ba1"
book_fileext = ".pdf"
print("# file full path:", dir_path + "\\" + book_filename + book_fileext)
# file full path: C:\Users\python\book\Python程序设计.pdf
