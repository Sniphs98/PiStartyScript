import sys
import os

import installations
import systemOperations


def print_hi():
    # systemOperations.update_and_upgrade()

    if yes_or_no('test question'):
        print('sugeces')

    if yes_or_no('Vim ?'):
        print('test')
        installations.vim_install()

    if yes_or_no('Change hostname ?'):
        new_host_name = input('New hostname: ')
        systemOperations.change_host_name(new_host_name)

    if yes_or_no('New sudo user ?'):
        username = input('Username: ')
        systemOperations.create_new_user(username)

    if yes_or_no('Enable ssh ?'):
        systemOperations.enable_ssh()

    if yes_or_no('Auto update ?'):
        installations.auto_update()


def yes_or_no(question):
    while "the answer is invalid":
        reply = str(raw_input(question + ' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


if __name__ == '__main__':
    arguments = str(sys.argv).lower()

    print(arguments)

    # default
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# /mnt/c/Users/lukas/PycharmProjects/PiStartyScript
