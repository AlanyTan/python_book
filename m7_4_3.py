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


def main(name_base: str) -> None:
    """main func demo add to and extract from zip file.

    Args:
        base_name: file name without extension name
    """
    m7_2_3.main(name_base)
    logger.debug("created files to be zipped")

    base_name = os.path.basename(name_base)
    files_to_zip = [f for f in os.listdir()
                    if f.startswith(f"{base_name}.data")]
    dir_to_zip = [f for f in os.listdir() if f.endswith("package")]

    zipfile_name = name_base + ".zip"
    zf = zipfile.ZipFile(zipfile_name, mode='w')

    for f in files_to_zip:
        zf.write(f)

    on_the_fly_text = f"{files_to_zip} were written into {zipfile_name}"
    zf.writestr(f"{base_name}.otf.txt", on_the_fly_text)

    for dtz in dir_to_zip:
        for root, dirs, files in os.walk(dtz):
            for file in files:
                zf.write(os.path.join(root, file))

    zf.close()
    logger.debug("%s created with on_the_fly text, %r and %r",
                 os.path.basename(zipfile_name), files_to_zip, dir_to_zip)

    os.remove(f"{name_base}.data.txt")
    print("# deleted  {base_name}.data.txt, only data.bin file left is",
          [f for f in os.listdir() if f.startswith(f"{base_name}.data")])

    zf = zipfile.ZipFile(zipfile_name, 'r')

    for zfinfo in zf.infolist():
        logger.debug(zfinfo)

    print(f"# {zf.read(f"{base_name}.data.txt")=}")

    zf.extract(f"{base_name}.otf.txt")

    zf.close()
    print("# extracted the txt file from zip, list of data files:",
          [f for f in os.listdir() if f.startswith(f"{base_name}.")
           and f.endswith(".txt")])


if __name__ == '__main__':
    namebase = __file__[:-3]
    main(namebase)

#DEBUG - m7_2_3(m7_2_3.py:33) - entering write_to_file(...m7_4_3.data.txt, t, utf-8)...
#DEBUG - m7_2_3(m7_2_3.py:47) - processing data as text.
#DEBUG - m7_2_3(m7_2_3.py:54) - writelines() to text file: ['Python程序设计', 2, False, 'A string literal.']
#DEBUG - m7_2_3(m7_2_3.py:57) - file {'...m7_4_3.data.txt'} closed.
#DEBUG - m7_2_3(m7_2_3.py:33) - entering write_to_file(...m7_4_3.data.bin, b, None)...
#DEBUG - m7_2_3(m7_2_3.py:37) - processing data as binary.
#DEBUG - m7_2_3(m7_2_3.py:44) - writelines() to binary file: [bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1'), b'\x02\x00\x00\x00', b'\x00', b'a bytes litteral']
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: bytearray(b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1') is 18 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'\x02\x00\x00\x00' is 4 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'\x00' is 1 bytes
#DEBUG - m7_2_2(m7_2_2.py:39) - ..pack_for_write: b'a bytes litteral' is 16 bytes
#DEBUG - m7_2_3(m7_2_3.py:57) - file {'...m7_4_3.data.bin'} closed.
#DEBUG - __main__(m7_4_3.py:23) - created files to be zipped
#DEBUG - __main__(m7_4_3.py:45) - m7_4_3.zip created with on_the_fly text, ['m7_4_3.data.txt', 'm7_4_3.data.otf', 'm7_4_3.data.bin'] and ['m6_3_package']
# deleted  {base_name}.data.txt, only data.bin file left is ['m7_4_3.data.otf', 'm7_4_3.data.bin']
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m7_4_3.data.txt' filemode='-rw-r--r--' file_size=45>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m7_4_3.data.bin' filemode='-rw-r--r--' file_size=55>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m7_4_3.otf.txt' filemode='?rw-------' file_size=94>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/module_2.py' filemode='-rw-r--r--' file_size=483>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/module_1.py' filemode='-rw-r--r--' file_size=503>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_3_IV.py' filemode='-rw-r--r--' file_size=1598>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/__init__.py' filemode='-rw-r--r--' file_size=965>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_4_3/__main__.py' filemode='-rw-r--r--' file_size=417>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_4_3/__init__.py' filemode='-rw-r--r--' file_size=333>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/irregular.py' filemode='-rw-rw-r--' file_size=513>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/rectangle.py' filemode='-rw-rw-r--' file_size=893>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/circle.py' filemode='-rw-rw-r--' file_size=974>
#DEBUG - __main__(m7_4_3.py:55) - <ZipInfo filename='m6_3_package/m6_3_2_geometry/__init__.py' filemode='-rw-r--r--' file_size=1008>
# zf.read(f"{base_name}.data.txt")=b'Python\xe7\xa8\x8b\xe5\xba\x8f\xe8\xae\xbe\xe8\xae\xa1\n2\nFalse\nA string literal.\n'
# extracted the txt file from zip, list of data files: ['m7_4_3.otf.txt']
