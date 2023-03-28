from main import *
import os, io, subprocess
from contextlib import redirect_stdout

# specify the name of the new directory
new_directory = "ExpectedOutput"
# create the new directory if it doesn't exist
if not os.path.exists(new_directory):
    os.mkdir(new_directory)

#get current path
current_path = os.getcwd()
current_path += "/Compilers/testen"
directories = os.listdir(current_path)

#run through every test folder and through every test.c file and produce .dot file for it
for i in directories:
    oldpath = current_path
    current_path += f"/{i}"
    files = os.listdir(current_path)
    for j in files:
        temp_old2 = current_path
        current_path += f"/{j}"
        try:
            main(current_path)
        except SystemExit as e:
            pass
        current_path = temp_old2
    #reset current_path
    current_path = oldpath
