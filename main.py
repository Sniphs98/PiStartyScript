import sys
import os

import installations
import system_operations


def print_hi():
    # print('# Username:', len(sys.argv))

    system_operations.update_and_upgrade()

    if yes_or_no('Vim ?'):
        installations.vim_install()

    if yes_or_no('New sudo user ?'):
        username = input("Username: ")
        system_operations.create_new_user(username)

    if yes_or_no('Enable ssh ?'):
        system_operations.enable_ssh()

    if yes_or_no('Auto update ?'):
        installations.auto_update()


# os.system('echo ' + username)
# print(username)


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


# system operations


if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
