# module of os
import os

def curr_dir():
    print("current working directory befor : ")
    print(os.getcwd())
    print()

# print cwd befor
curr_dir()
# changing the current working directory
os.chdir('../')
# print cwd after
curr_dir()