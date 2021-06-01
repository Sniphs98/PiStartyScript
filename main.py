import sys
import os



def print_hi(name):
    # print('# Username:', len(sys.argv))

    newUser = yes_or_no('New sudo User ?')
    if newUser == True:
        username = input("Username: ")
        create_new_user(username)

    autoUpdate = yes_or_no('Auto Update ?')
    if autoUpdate == True:
        update_and_upgrade()


# os.system('echo ' + username)
# print(username)

def yes_or_no(question):
    while "the answer is invalid":
        reply = str(input(question+ ' (y/n): ')).lower().strip()
        if reply[0] == 'y':
            return True
        if reply[0] == 'n':
            return False

def update_and_upgrade():
    os.system('sudo apt update && sudo apt upgrade')

def create_new_user(username):
    os.system("sudo adduser " + username)

if __name__ == '__main__':
    print_hi('PyCharm')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
