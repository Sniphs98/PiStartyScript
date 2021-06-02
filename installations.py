import os


def vim_install():
    os.system('sudo apt install vim')


def auto_update():
    os.system('sudo apt-get install unattended-upgrades')
    os.system('sudo dpky-reconfigure --priority=low unattended-upgrades')


def vim_install():
    os.system('sudo apt install vim')
