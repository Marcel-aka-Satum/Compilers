from main import *
import os, io, subprocess
from contextlib import redirect_stdout

'''
a test script that automatically runs your compiler on the specified C files and, for each C file, produces two things:
the AST tree in Graphviz dot format,
the LLVM IR code,
'''

def main_test():
    # runAll()
    runCorrect()


#TODO: PRODUCE LLVM
#run through every test folder in /testen and through every test.c files and produce .dot file for it
def runAll():
    #get current path
    current_path = os.getcwd()
    current_path += "/testen"

    #get all folders from /testen directory
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

#run only tests that expect no errors in /testen/correctTests directory
def runCorrect():
    #get current path
    current_path = os.getcwd()
    current_path += "/testen/correctTests"

    oldpath = current_path
    files = os.listdir(oldpath)
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
    


#run tests
main_test()