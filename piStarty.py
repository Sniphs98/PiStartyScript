import sys
import os

import installations
import systemOperations


def print_hi():
    systemOperations.update_and_upgrade()

    if yes_or_no('test'):
        test()


    if yes_or_no('Vim ?'):
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

    reply = str(input(question + ' (y/n): ')).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False


def test():
    os.system('echo test')


if __name__ == '__main__':
    arguments = str(sys.argv).lower()

    print(arguments)

    # default
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
