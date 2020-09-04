from BookReg.lib.interface import *
from BookReg.lib.file import *
from time import sleep

file = 'EnglishLearner.txt'
headLine("MAIN MENU")
while True:
    answer = menu(['Create file', 'Register', 'Show up the learner', 'Delete the file', 'Exit'])
    if answer == 1:
        if not fileExist(file):
            createFile(file)
        else:
            print('\033[41mFile already exist.\033[m')
    elif answer == 2:
        # Function for register person
        name = str(input('Type the name: ')).strip()
        age = readInt('Type the age: ')
        register(file, name, age)
    elif answer == 3:
        if fileExist(file):
            readFile(file)
        else:
            print('\033[41mFile does not exist. Create a file.\033[m')
            print(dashes())
    elif answer == 4:
        while True:
            print('\033[41mATTENTION!!! If you delete this\033[m'.center(42))
            print('\033[41mfile this action can not undo.\033[m'.center(42))
            opt = menu(['Cancel', 'Delete Forever'])
            if opt == 1:
                break
            elif opt == 2:
                deleteFile(file)
                break
    elif answer == 5:
        headLine('Exiting the system... see you!')
        break
    else:
        headLine('\033[31mERROR! Type a valid option.\033[m')
    sleep(2)