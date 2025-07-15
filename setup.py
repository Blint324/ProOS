print("Welcome to the ProShell setup! This will be quick...")
print("Importing core libraries...")
import os
from termcolor import colored
import time
print("Importing done!")

crashFlag = 0
custDir = input("Would you like to set a custom directory for ProShell? [y/N] ")
custDir.lower()

if custDir == "":
    custDir = "n"
if custDir == "n":
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
elif custDir == "y":
    custDirLoc = input("Where should the directory be? ")
    print("Creating core folders...")
    try:
        os.mkdir(custDirLoc)
        os.mkdir(f"{custDirLoc}/data")
        os.mkdir(f"{custDirLoc}/data/users")
        os.mkdir(f"{custDirLoc}/data/logs")
        os.mkdir(f"{custDirLoc}/data/config")
        f = open(f"{custDirLoc}/data/config/autolog.conf", "w")
        f.write("false")
        f.close()
        f = open(f"{custDirLoc}/data/config/bootexec.py", "w")
        f.write("# This file starts whenever you launch mainterminal.py, put any python script here you'd like.")
        f.close()
    except FileExistsError:
        print(colored("Error! Files already exist.", "red"))
    except PermissionError:
        print(colored("Error! Lack of permissions.", "red"))
        crashFlag = 1
        crashReason = "Lack of permissions."
    except:        
        print(colored("Error! Unknown.", "red"))
        crashFlag = 1
        crashReason = "Unknown."
else:
    print("Thats not a valid option!")
    quit(1)
if crashFlag == 0:
    print(colored("Setup done!", "green"))
else:
    print(colored(f"Error! Setup failed. Reason: {crashReason}", "red"))
    quit(1)

print("Welcome to ProShell, we hope you enjoy ;)")

time.sleep(1)
os.system("clear")
autoTime = 10
for i in range(10):
    print(f"Autostarting ProShell in {autoTime}, Press CTRL + C to cancel.")
    time.sleep(1)
    autoTime = autoTime - 1
    os.system("clear")
os.system("python3 mainterminal.py")
