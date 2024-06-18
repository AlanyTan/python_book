string_1 = "abcde\"\t\"fghij\nklmno\' \'pqrst\n"
rstring_1 = r"abcde\"\t\"fghij\nklmno\' \'pqrst\n"
print("'''string literal \n\"" + rstring_1 + "\"\n   is actually:\n" +
      string_1 + "'''")
'''string literal 
"abcde\"\t\"fghij\nklmno\' \'pqrst\n"
   is actually:
abcde"	"fghij
klmno' 'pqrst
'''

dir_path = r"C:\Users\python\book"
book_filename = "\120\x79\x74\x68\x6f\x6e\u7a0b\u5e8f\u8bbe\u8ba1"
book_fileext = ".pdf"
print("# file full path:", dir_path + "\\" + book_filename + book_fileext)
# file full path: C:\Users\python\book\Python程序设计.pdf
