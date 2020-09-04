# Verify with number typed is a integer number
def readInt(number):
    while True:
        try:
            n = int(input(number))
        except (ValueError, TypeError):
            print('Please, type a valid number.')
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n


# This function set a line of dashes
def dashes(size=42):
    return '-' * size


# This function set up a text in center put two line between the text
def headLine(txt):
    print(dashes())
    print(txt.center(42))
    print(dashes())

# This function is for put number in each item of the menu.
def menu(lista):
    count = 1
    for item in lista:
        print(f'\033[33m{count}\033[m - \033[34m{item}\033[m')
        count += 1
    print(dashes())
    opt = readInt('\033[32mYour option:\033[m ')
    print(dashes())
    return opt
