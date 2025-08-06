# quiz.py
# Read the contents of a file line by line

filename = "Topic07-files/sample.txt"

with open(filename, "r") as f:
    for line in f:
        print(line.strip())
        