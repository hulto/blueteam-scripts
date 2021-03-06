# Michael Burke
# Goes through every user's home directory and removes .ssh/authorized_keys

import os
import time
import sys

isRepeat = False

def repeat():
    time.sleep(5)
    do()
    repeat()

def do():
    for file in os.listdir("."):
        if os.path.isdir(file):
            os.system("rm -rf " + file + "/.ssh/authorized_keys")

def main():
    global isRepeat
    os.chdir("/home")
    if len(sys.argv) >= 2:
        for arg in sys.argv:
            if arg == "--repeat":
                isRepeat = True
    if isRepeat:
        do()
        repeat()
    else:
        do()

main()