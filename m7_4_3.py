"""Demo zip compressing and extraction 

Usage: python -m m7_4_3   
"""

import os
import zipfile
import logging
logging.basicConfig(level=logging.DEBUG, format="#%(levelname)s - "
                    "%(name)s(%(filename)s:%(lineno)d) - %(message)s")
logger = logging.getLogger(__name__)

import m7_2_3 

def prepare_files(base_name: str) -> None:
    """prepare files to be added to the zip by using imported funcs

    Args:
        base_name: file name without extension name
    """
    m7_2_3.main(base_name)
    logger.debug(f"prepared files to be zipped")
    
def main(base_name: str) -> None:
    """main func demo add to and extract from zip file.
    
    Args:
        base_name: file name without extension name
    """
    prepare_files(base_name)
    files_to_zip = [f for f in os.listdir() if f.startswith(
        f"{os.path.basename(base_name)}.data")]
    dir_to_zip = [f for f in os.listdir() if f.endswith(
        "package")]
    
    zipfile_name = base_name + ".zip"
    zf = zipfile.ZipFile(zipfile_name, mode='w')
    for f in files_to_zip:
        zf.write(f)
    for dtz in dir_to_zip:
        for root, dirs, files in os.walk(dtz):
            for file in files:
                zf.write(os.path.join(root, file))
    zf.close()

    logger.debug(f"{zipfile_name} created with {files_to_zip=}, {dir_to_zip=}")

    os.remove(f"{base_name}.data.txt")
    print("# deleted the txt file {base_name}.data.txt, only data file left is"
          , [f for f in os.listdir()
             if f.startswith(f"{os.path.basename(base_name)}.data")])

    zf = zipfile.ZipFile(zipfile_name, 'r')
    for zfinfo in zf.infolist():
        logger.debug(zfinfo)
    zf.extract(f"{os.path.basename(base_name)}.data.txt")
    zf.close()
    
    print("# extracted the txt file from zip, list of data files:"
          , [f for f in os.listdir()
             if f.startswith(f"{os.path.basename(base_name)}.data")])


if __name__ == '__main__':
    base_name = __file__[:-3]
    main(base_name)

#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_4_3.data.txt, open_mode='t' 
#DEBUG - m7_2_2(m7_2_3.py:46) - open_mod!='b', processing data as text.
#DEBUG - m7_2_2(m7_2_3.py:53) - write to text file content=['Python程序设计', 2, False, 'A string literal.']
#DEBUG - m7_2_2(m7_2_3.py:33) - write_to_file() called with m7_4_3.data.bin, open_mode='b' 
#DEBUG - m7_2_2(m7_2_3.py:36) - open_mode=='b', processing data as binary.
#DEBUG - m7_2_2(m7_2_3.py:43) - write to binary file content=[bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'), b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral']
#DEBUG - __main__(m7_4_3.py:22) - prepared files to be zipped
#DEBUG - __main__(m7_4_3.py:46) - C:\Users\user\Documents\python_book\m7_4_3.zip created with files_to_zip=['m7_4_3.data.bin', 'm7_4_3.data.txt'], dir_to_zip=['m6_3_package']
# deleted the txt file {base_name}.data.txt, only data file left is ['m7_4_3.data.bin']
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m7_4_3.data.bin' filemode='-rw-rw-rw-' file_size=55>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m7_4_3.data.txt' filemode='-rw-rw-rw-' file_size=49>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_3_IV.py' filemode='-rw-rw-rw-' file_size=1610>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/module_1.py' filemode='-rw-rw-rw-' file_size=518>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/module_2.py' filemode='-rw-rw-rw-' file_size=489>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__init__.py' filemode='-rw-rw-rw-' file_size=933>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/circle.py' filemode='-rw-rw-rw-' file_size=1017>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/irregular.py' filemode='-rw-rw-rw-' file_size=536>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/rectangle.py' filemode='-rw-rw-rw-' file_size=922>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/__init__.py' filemode='-rw-rw-rw-' file_size=1038>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/circle.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1572>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/rectangle.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1118>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/__init__.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1489>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/__main__.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1093>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_4_3/__init__.py' filemode='-rw-rw-rw-' file_size=349>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_4_3/__main__.py' filemode='-rw-rw-rw-' file_size=432>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_4_3/__pycache__/__init__.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=678>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_4_3/__pycache__/__main__.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1047>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__pycache__/circle.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1100>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__pycache__/m6_3_3_IV.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1153>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__pycache__/m6_4_4.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1021>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__pycache__/module_1.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1041>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__pycache__/module_2.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1023>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__pycache__/rectangle.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=723>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__pycache__/__init__.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1278>
# extracted the txt file from zip, list of data files: ['m7_4_3.data.bin', 'm7_4_3.data.txt']
