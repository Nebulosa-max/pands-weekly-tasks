# quiz2.py

FILENAME = "Topic07-files/count.txt"

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
    return number

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

# Test the functions
num = readNumber()
print("Current number in file:", num)

writeNumber(3)
print("Wrote number 3 to file.")

# quiz2.py

FILENAME = "Topic07-files/count.txt"

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
    return number

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        f.write(str(number))

# Main program
num = readNumber()
print(f"This program has been run {num} times.")

num += 1
writeNumber(num)