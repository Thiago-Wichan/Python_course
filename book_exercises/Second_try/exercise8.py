
def writeToFile(file_name, text):
    with open(file_name, "w") as file:
        file.write(text)


def appendToFile(file_name, text):
    with open(file_name, 'a') as file:
        file.write(text)


def readFromFile(file_name):
    with open(file_name, 'r') as file:
        return file.read()


writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
