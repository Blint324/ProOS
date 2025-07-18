import os
os.system("clear")

print("Welcome to the ProShell setup! This will be quick...")
print("Importing core libraries...")
from termcolor import colored
import time
import sys
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
distroConf = ""
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
    elif setupCmd[0:7] == "install":
        if len(setupCmd) == 7:
            print("Invalid usage! Usage: install [PACKAGE]")
        else:
            if distroConf == "":
                print(colored("Error! Distroconf not set.", "red"))
            else:
                if distroConf == "debian" or "ubuntu":
                    os.system("sudo apt update")
                    os.system(f"sudo apt install {setupCmd[8:9999999999999999999]}")
                elif distroConf == "fedora":
                    os.system(f"sudo dnf install {setupCmd[8:9999999999999999999]}")
                elif distroConf == "arch":
                    os.system(f"sudo pacman -S {setupCmd[8:999999999999999999999]}")
                elif distroConf == "suse":
                    os.system(f"sudo zypper install {setupCmd[8:999999999999999999]}")
                elif distroConf == "gentoo":
                    os.system("sudo emerge --sync")
                    os.system(f"sudo emerge {setupCmd[8:999999999999999999999999]}")
    elif setupCmd[0:10] == "distroconf":
        if len(setupCmd) == 10:
            print("Invalid usage! Usage: distroconf [VALID DISTRO]\nDistros:\ndebian, ubuntu, fedora, arch, suse, gentoo.")
        else:
            if setupCmd[11:17] == "debian":
                distroConf = "debian"
            elif setupCmd[11:17] == "ubuntu":
                distroConf = "ubuntu"
            elif setupCmd[11:17] == "fedora":
                distroConf = "fedora"
            elif setupCmd[11:15] == "arch":
                distroConf = "arch"
            elif setupCmd[11:15] == "suse":
                distroConf = "suse"
            elif setupCmd[11:17] == "gentoo":
                distroConf = "gentoo"
            else:
                print(f"Distro {setupCmd[11:99999999999999999]} not found!\nDistros:\ndebian, ubuntu, fedora, arch, suse, gentoo.")
    else:
        if setupCmd == "":
            print("Command not found!")
        else:
            wrongCmdSplit = setupCmd.split()
            print(f"Command {wrongCmdSplit[0]} not found!")
