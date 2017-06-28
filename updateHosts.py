import sys
import os
import requests

HOSTS_PATH = os.path.join(os.path.expandvars(
    "%SystemRoot%"), "System32", "drivers", "etc", "hosts")
# HOSTS_URL = "https://raw.githubusercontent.com/Lerist/Go-Hosts/master/hosts"
HOSTS_URL = "https://raw.githubusercontent.com/wangchunming/2017hosts/master/hosts-pc"
index = 0

if sys.platform.startswith('win'):
    pass
else:
    print("Only for windows")


def checkHostsPathAva():
    if not (os.access(HOSTS_PATH, os.F_OK)):
        print("hosts does't exsist")
        return False
    if not (os.access(HOSTS_PATH, os.R_OK) and os.access(HOSTS_PATH, os.W_OK)):
        print("don't have permission")
        return False
    else:
        return True


def getHosts():
    r = requests.get(HOSTS_URL)
    return r.text


def changeHosts():
    if checkHostsPathAva():
        f = open(HOSTS_PATH, "w")
        f.write(getHosts())
        f.close()


def checkHosts():
    if checkHostsPathAva():
        f = open(HOSTS_PATH, "r")
        for i in range(0, 5):
            print(f.readline())
        f.close()


while True:
    command = input(
        'please type your command \n  "1" for upgrade hosts \n "0" for quit \n ')

    if command == '1':
        changeHosts()
        checkHosts()
    elif command == '0':
        print("quit")
        break
    else:
        print("please input valid code")
