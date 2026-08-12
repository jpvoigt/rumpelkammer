import os

message = os.environ.get("INPUT_MESSAGE", "Hallo aus Python")
print(message)

with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as output:
    output.write("result=erfolgreich\n")
