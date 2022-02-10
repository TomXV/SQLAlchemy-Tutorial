import database
from database import clearConsole
from time import sleep

def method_continue():
    print(
"""
----------------------------------------------------------------
Continue?
----------------------------------------------------------------
Yes: 1
No: 0
----------------------------------------------------------------
"""
)
    sel_num = input("Number?: ")
    clearConsole()
    if sel_num == "1":
        main()
    else:
        exit()

def main():
    print(
"""
----------------------------------------------------------------
CRUD MENU
----------------------------------------------------------------
Create: 1
Read: 2
Update: 3
Delete: 4
Exit: 5
----------------------------------------------------------------
"""
)


    sel_menu_num = input("Number?: ")
    clearConsole()

    if sel_menu_num == "1":
        database.create()
        method_continue()
    elif sel_menu_num == "2":
        database.read()
        method_continue()
    elif sel_menu_num == "3":
        database.update()
        method_continue()
    elif sel_menu_num == "4":
        database.delete()
        method_continue()
    elif sel_menu_num == "5":
        exit()
    else:
        main()


if __name__ == '__main__':
    main()