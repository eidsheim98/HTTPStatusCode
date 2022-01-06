import os

cwd = os.getcwd()

print("Readying files...")
with open('cwd.txt', 'w+') as file:
    file.write(cwd)

print("Creating launch file...")
with open("../hs.bat", 'w+') as file:
    file.write("@ECHO off\nset arg1=%1\npython " + cwd + "/hs.py %arg1%")

print("Task finished successfully")