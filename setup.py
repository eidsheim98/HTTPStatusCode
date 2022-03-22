import platform
import os
import pathlib

file_path = os.path.abspath(__file__) # full path of your script
dir_path = os.path.dirname(file_path) # full path of the directory of your script
script_path = os.path.join(dir_path,'hs.py')

if platform.system().lower() == "linux":
    os.system("alias hs='python3 {}'".format(script_path))
    os.system("touch ~/.bash_aliases")
    path = pathlib.Path.home()
    path = os.path.join(path, ".bash_aliases")
    try:
        with open(path, 'a') as file:
            file.write("\nalias hs='python3 {}'".format(script_path))
    except Exception as e:
        print("HTTPSTATUSCODE INSTALLATION ERROR:", e)

elif platform.system().lower() == "windows":
    with open("../hs.bat", 'w+') as file:
        file.write("@ECHO off\nset arg1=%1\npython " + script_path + " %arg1%")

print("Done! You may have to restart the terminal")
print("To use HTTPStatusCode, type: hs {statuscode}")