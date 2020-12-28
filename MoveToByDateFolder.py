import glob
import os
import datetime
import shutil

source_path = input()

if source_path == "":
    source_path = './'

print(source_path + "*")

source_files = sorted(glob.glob( source_path + "*" ), key=lambda f: os.stat(f).st_mtime)


dest_folders = {}

for file in source_files:
    print(file)
    if os.path.isdir(file):
        continue
    t = os.path.getmtime(file)
    d = datetime.datetime.fromtimestamp(t)
    dest_foldername = str(d)[0:10]

    if not dest_foldername in dest_folders:
        dest_folders[dest_foldername] = True
        if not os.path.exists(dest_foldername):
            os.mkdir(source_path + dest_foldername)
    print('----------source----------')
    print(source_path + os.path.basename(file))
    print('----------dest----------')
    print(source_path  + dest_foldername + "/" + os.path.basename(file))
    shutil.copy2( source_path + os.path.basename(file) , source_path  + dest_foldername + "/" + os.path.basename(file))

#print(dest_folders)