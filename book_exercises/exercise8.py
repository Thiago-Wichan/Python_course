from pathlib import Path


def writeToFile(file_path, text):
    path_file = Path(__file__).parent / file_path
    with open(path_file, 'w') as file:
        return file.write(text)


def appendToFile(file_path, text):
    path_file = Path(__file__).parent / file_path
    with open(path_file, 'a') as file:
        return file.write(text)


def readFromFile(file_path):
    path_file = Path(__file__).parent / file_path
    with open(path_file, 'r') as file:
        return file.read()


writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
