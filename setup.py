print("Welcome to the ProShell setup! This will be quick...")
print("Importing core libraries...")
import os
from termcolor import colored
import time
print("Importing done!")

crashFlag = 0

print("Obtaining directory...")
directory = os.getcwd()
f = open("dir.txt", "w")
f.write(directory)
f.close()
print("Obtained directory successfully!")
print("Creating core folders...")
try:
    os.mkdir(f"{directory}/data")
    os.mkdir(f"{directory}/data/users")
    os.mkdir(f"{directory}/data/logs")
    os.mkdir(f"{directory}/data/config")
    f = open(f"{directory}/data/config/autolog.conf", "w")
    f.write("false")
    f.close()
    f = open(f"{directory}/data/config/bootexec.py", "w")
    f.write("# This file starts whenever you launch mainterminal.py, put any python script here you'd like.")
    f.close()
except FileExistsError:
    print(colored("Error! Files already exist.", "red"))
except:
    print(colored("Error! Unknown.", "red"))
    crashFlag = 1
if crashFlag == 0:
    print(colored("Setup done!", "green"))
else:
    print(colored(f"Error! Setup failed. Reason: {crashReason}", "red"))
    quit(1)
while True:
    setupCmd = input(colored(f"{directory}$setup: ", "light_green"))
    setupCmd.lower()
    if setupCmd == "help":
        print("This is the setup terminal. If you're new, please refer to the README.md file in the Github repo.")
    elif setupCmd[0:4] == "exec":
        if len(setupCmd) == 4:
            print("Invalid usage! Usage: exec [COMMAND]")
        else:
            os.system(setupCmd[5:9999999999999])
    elif setupCmd == "start":
        os.system("python3 mainterminal.py")
    elif setupCmd == "restart":
        os.system("python3 setup.py")
    elif setupCmd == "clear":
        os.system("clear")
    elif setupCmd == "exit":
        quit(0)
    else:
        if setupCmd == "":
            print("Command not found!")
        else:
            wrongCmdSplit = setupCmd.split()
            print(f"Command {wrongCmdSplit[0]} not found!")
