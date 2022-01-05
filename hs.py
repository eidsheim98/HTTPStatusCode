import sys
import json

code = sys.argv[1]

file = open("statuscodes.json", "r")
lines = file.read()
j = json.loads(lines)

try:
    status = j[code]
    print(f'Statuscode:{" ":4}', code)
    print(f'Message:{" ":7}', status["message"])
    print(f'Description:{" ":3}', status["desc"])

except Exception as e:
    print("Error: Statuscode", code, "does not exist")