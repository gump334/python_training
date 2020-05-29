#!/usr/bin/env python3

# create a python script that will clean old files from your
import os

# User input for dir path and file name
print("list the file path of dir that file exist in to be deleted")
dir = input()
print("enter the file name to be delete")
file_name = input()
home = os.chdir(dir)
file_list = os.listdir()

# check to see if content is a file or directory. if file is located then it will delete it. if dir then it will confirm that it is
if os.path.isfile(file_name):
    print("file exists, removing file!")
    os.remove(file_name)
elif os.path.isdir(file_name):
    print("this is a directory")
else:
    print("file does not exist")

