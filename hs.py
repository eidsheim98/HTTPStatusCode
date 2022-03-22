#! python3

import sys
import json
import os

file_path = os.path.abspath(__file__) # full path of your script
dir_path = os.path.dirname(file_path) # full path of the directory of your script
codes_path = os.path.join(dir_path,'statuscodes.json')

with open(codes_path + "/statuscodes.json", "r") as file:
    lines = file.read()
    j = json.loads(lines)

types = {1: "Informational Response", 2: "Successful Response", 3: "Redirection Message",
         4: "Client Error Message", 5: "Server Error Response"}

try:
    code = sys.argv[1]

    status = j[code]
    print(f'Statuscode:{" ":4}', code)
    print(f'Message:{" ":7}', status["message"])
    print(f'Type:{" ":10}', [types[x] for x in types if x == int(str(code)[:1])][0])
    print(f'Description:{" ":3}', status["desc"])

except IndexError:
    print("Error: No parameters provided. Try running \"hs {statuscode}\"")

except KeyError:
    print("Error: Statuscode", code, "does not exist")