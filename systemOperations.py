import os
import socket
import subprocess
import platform


def change_host_name(hostname):
    old_hostname = socket.gethostname()
    # os.system('sudo hostnamectl set-hostname' + hostname)
    # os.system('sudo hostnamectl')
    print(old_hostname + ' -> ' + hostname)
    #TODO find old host name and change it to the new one


def create_new_user(username):
    os.system('sudo adduser ' + username)
    os.system('sudo usermod -aG sudo ' + username)
    os.system('sudo -l -U ' + username)


def enable_ssh():
    os.system('sudo apt install openssh-server')
    os.system('sudo systemctl status ssh')
    os.system('sudo ufw allow ssh')
    os.system('sudo ip a')

def disable_ssh():
    print(platform.release())
    platform.release()


def update_and_upgrade():
    os.system('sudo apt update && sudo apt upgrade')


