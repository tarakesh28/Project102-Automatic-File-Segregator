import os
import shutil

print()
print("Please Input the Source and Destination Directories to move files: ")
source = input("Source:      ")
dest = input("Destination: ")

#from_dir = r"C:\Users\tarak\Downloads"
#to_dir = r"C:\Users\tarak\Documents\Coding"
from_dir = str(source)
to_dir = str(dest)

list_of_files = os.listdir(from_dir)
#print("Files listed in source directory: ",list_of_files)
print()

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    if extension == '':
        continue
    if extension in ['.txt','.doc','.docx','.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name

        if os.path.exists(path2):
            print('Moving '+file_name+'.....')    
            shutil.move(path1,path3)

        else:
            os.mkdir(path2)    
            print('Moving '+file_name+'.....')    
            shutil.move(path1,path3)