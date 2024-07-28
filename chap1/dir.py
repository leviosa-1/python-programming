#python program to show the list of directory using os.listdir()
import os
cwd = os.getcwd()
print("Current working Directory ",cwd)

path = '/'
dir_list = os.listdir(path)
print("Files and directories in '",path, "' :")
print(dir_list)
