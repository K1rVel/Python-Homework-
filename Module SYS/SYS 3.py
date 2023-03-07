import sys

name = sys.argv[2]
text = sys.argv[1]

with open(name, "w+") as f:
    f.write(text)