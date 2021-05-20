import os
import sys
try:
    from pyvox.parser import VoxParser
except ImportError:
    print("Dependencies not installed.\nPlease run \"pip install -r requirements.txt\"")

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage : python converter.py file [dest]")
        sys.exit(-1)
    file = os.path.abspath(sys.argv[1])
    if not os.path.exists(file):
        print("No such file!")
        sys.exit(-1)
    if len(sys.argv) == 3:
        txt_name = os.path.abspath(sys.argv[2])
    else:
        txt_name = os.path.abspath(os.path.splitext(
            os.path.split(file)[1])[0] + ".txt")

    vox_file = VoxParser(file).parse()

    length, width, height = vox_file.models[0].size
    with open(txt_name, "w") as f:
        for x, y, z, vox_color in vox_file.models[0].voxels:
            f.write(f"{x},{y},{z}\n")
