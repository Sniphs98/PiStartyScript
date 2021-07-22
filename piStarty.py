import sys
import os

import installations
import systemOperations


def print_hi():
    systemOperations.update_and_upgrade()

    if yes_or_no('Vim ?'):
        installations.vim_install()


    if yes_or_no('Change hostname ?'):
        new_host_name = raw_input('New hostname: ')
        systemOperations.change_host_name(new_host_name)

    if yes_or_no('New sudo user ?'):
        username = raw_input('Username: ')
        systemOperations.create_new_user(username)

    if yes_or_no('Enable ssh ?'):
        systemOperations.enable_ssh()
    else:
        systemOperations.disable_ssh()

    if yes_or_no('Auto update ?'):
        installations.auto_update()

    if yes_or_no('Reboot ?'):
        systemOperations.reboot()


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
