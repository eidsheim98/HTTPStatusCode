#! python3

import sys
import json

cwd = ""
with open("cwd.txt", 'r') as file:
    cwd = file.readlines()[0]

file = open(cwd + "/statuscodes.json", "r")
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