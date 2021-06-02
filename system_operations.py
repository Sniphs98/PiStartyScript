import os


def create_new_user(username):
    os.system('sudo adduser ' + username)
    os.system('sudo usermod -aG sudo ' + username)
    os.system('sudo -l -U ' + username)


def enable_ssh():
    os.system('sudo apt install openssh-server')
    os.system('sudo systemctl status ssh')
    os.system('sudo ufw allow ssh')
    os.system('sudo ip a')


def update_and_upgrade():
    os.system('sudo apt update && sudo apt upgrade')

