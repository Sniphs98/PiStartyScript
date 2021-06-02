import sys
import os


def print_hi():
    # print('# Username:', len(sys.argv))

    update_and_upgrade()

    if yes_or_no('New sudo user ?'):
        username = input("Username: ")
        create_new_user(username)

    if yes_or_no('Auto update ?'):
        auto_update()

    if yes_or_no('Enable ssh ?'):
        enable_ssh()


# os.system('echo ' + username)
# print(username)

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False


def update_and_upgrade():
    os.system('sudo apt update && sudo apt upgrade')


def auto_update():
    os.system('sudo apt-get install unattended-upgrades')
    os.system('sudo dpky-reconfigure --priority=low unattended-upgrades')


def create_new_user(username):
    os.system('sudo adduser ' + username)
    os.system('sudo usermod -aG sudo ' + username)
    os.system('sudo -l -U ' + username)


def enable_ssh():
    os.system('sudo apt install openssh-server')
    os.system('sudo systemctl status ssh')
    os.system('sudo ufw allow ssh')
    os.system('sudo ip a')


if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
