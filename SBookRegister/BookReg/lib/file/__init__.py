from BookReg.lib.interface import *
import os


# This function verify whether a file exist.
def fileExist(name):
    try:
        with open(name, 'rt') as a:
            a.close()
    except FileNotFoundError:
        return False
    else:
        return True


# This function is for create a file
def createFile(name):
    try:
        with open(name, 'wt+') as a:  # w = write, t = text, + create a file.
            a.close()
    except:
        print('ERROR while the file was being created.')
    else:
        print(f'\033[34mFile {name} was created.\033[m'.center(42))


# This function read the file lines and show the list of names and ages on screen
def readFile(name):
    try:
        a = open(name, 'rt')
    except:
        print('ERROR while trying to open the file.')
    else:
        headLine('Person registered')
        for line in a:
            dataLine = line.split(";")  # transform the line in a list and th ";" become de divisor of a list
            print(f'{dataLine[0]:<30}{dataLine[1]:>3}')
        print(dashes())
    finally:
        a.close()


# This function register the name and age in a line into the file.
def register(fileName, name='Unknown', age='0'):
    try:
        a = open(fileName, 'a')  # a = append it's used to add something in the file.
    except:
        print('ERROR while trying to open the file.')
    else:
        try:
            a.write(f'{name}; {age}\n')
        except:
            print('ERROR while trying to write in file.')
        else:
            print(f'\033[34m{name} was registered.\033[m')
            a.close()


# This function delete the file, the data into the file can't be recovered later.
def deleteFile(name):
    try:
        os.remove(name)
    except:
        print('ERROR while trying to delete the file')
    else:
        print(f'\033[34mFile {name} Deleted\033[m')
        print(dashes())
