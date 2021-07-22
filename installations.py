import os
import subprocess


def vim_install():
    os.system('sudo apt install vim -y')


def auto_update():
    os.system('sudo apt-get install unattended-upgrades -y')
    os.system('sudo dpky-reconfigure --priority=low unattended-upgrades')


#def install(packed_name):
    #package_name = "<package_name>"
    #subprocess.run(["sudo", "apt", "install", "-y", package_name], check=True)