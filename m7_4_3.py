"""Demo zip compressing and extraction 

Usage: python -m m7_4_3   
"""

import os
import zipfile
import m7_2_3 

def prepare_files(base_name: str) -> None:
    """prepare files to be added to the zip by using imported funcs

    Args:
        base_name: file name without extension name
    """
    m7_2_3.main(base_name)
    
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
    print(f"# {files_to_zip=}, {dir_to_zip=}")
    
    zipfile_name = base_name + ".zip"

    zf = zipfile.ZipFile(zipfile_name, mode='w')
    for f in files_to_zip:
        zf.write(f)
    for dtz in dir_to_zip:
        for root, dirs, files in os.walk(dtz):
            for file in files:
                zf.write(os.path.join(root, file))
    zf.close()

    os.remove(f"{base_name}.data.txt")
    print("# after deleting the txt file", [f for f in os.listdir()
        if f.startswith(f"{os.path.basename(base_name)}.data")])

    zf = zipfile.ZipFile(zipfile_name, 'r')
    print("#", *zf.infolist(), sep='\n#')
    zf.extract(f"{os.path.basename(base_name)}.data.txt")
    zf.close()
    
    print("# after extract the txt file from zip", [f for f in os.listdir()
        if f.startswith(f"{os.path.basename(base_name)}.data")])


if __name__ == '__main__':
    base_name = __file__[:-3]
    main(base_name)

# files_to_zip=['m7_4_3.data.bin', 'm7_4_3.data.txt'], dir_to_zip=['m6_3_package']
# after deleting the txt file ['m7_4_3.data.bin']
#
#<ZipInfo filename='m7_4_3.data.bin' filemode='-rw-rw-rw-' file_size=55>
#<ZipInfo filename='m7_4_3.data.txt' filemode='-rw-rw-rw-' file_size=49>
#<ZipInfo filename='m6_3_package/m6_4_4.py' filemode='-rw-rw-rw-' file_size=731>
#<ZipInfo filename='m6_3_package/module_1.py' filemode='-rw-rw-rw-' file_size=305>
#<ZipInfo filename='m6_3_package/module_2.py' filemode='-rw-rw-rw-' file_size=284>
#<ZipInfo filename='m6_3_package/__init__.py' filemode='-rw-rw-rw-' file_size=888>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/circle.py' filemode='-rw-rw-rw-' file_size=1017>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/irregular.py' filemode='-rw-rw-rw-' file_size=536>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/rectangle.py' filemode='-rw-rw-rw-' file_size=922>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/__init__.py' filemode='-rw-rw-rw-' file_size=915>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/__main__.py' filemode='-rw-rw-rw-' file_size=422>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/circle.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1572>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/rectangle.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1118>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/__init__.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=1150>
#<ZipInfo filename='m6_3_package/m6_3_2_geometry/__pycache__/__main__.cpython-312.pyc' filemode='-rw-rw-rw-' file_size=954>
# after extract the txt file from zip ['m7_4_3.data.bin', 'm7_4_3.data.txt']
