import os

os.system("clear")

print("Welcome to ProOS!")
print("Importing core libraries...")

import time
import datetime
import random
import linecache

print("Defining variables...")

cmd = ""
cwd = os.getcwd()

print("Defining variables done.")
print("Starting main loop...")

while True:
    cmd = input(f"{cwd}: ")
    cmd.lower()

    # Checking for commands
    
    if cmd[0:3] == "ver":
        if len(cmd) == 3:
            print("ProOS version u1.2")
        else:
            if cmd[3:6] == " -d":
                print("ProOS version u1.2\nCredits:\nBálint Vámosi: Lead developer.\nLinus Torvalds and the Linux team: Inspiration for this mockup.\nGergő Vámosi: Co-Owner of the project.")
    
            elif cmd[3:6] == " -h":
                print("Displays the current version of ProOS.\nUsage:\nver [FLAGS]")
    elif cmd[0:4] == "help":
        if len(cmd) == 4:
            print("Basic commands:\nrepeat\nexit\nver\ndisplay.")
        else:
            if cmd[5:8] == "ver":
                print("Prints the current version of ProOS.\nFlags:\n-d: Displays more detailed info about ProOS.\n-h: Displays help for the command.")
            elif cmd[5:9] == "exit":
                print("Exits the program.")
            elif cmd[5:11] == "repeat":
                print("Repeats whatever you put next to it.")
            elif cmd[5:12] == "display":
                print("Displays the contents of any text file.\nFlags:\n-su: Runs as superuser.")
            elif cmd[5:10] == "clear":
                print("Clears the contents of the screen.")
            elif cmd[5:8] == "dir":
                print("Changes the working directory.\nUsage:\ndir [DIRECTORY]")
            elif cmd[5:7] == "ls":
                print("Lists the contents of the current working directory.")
            else:
                print(f"No help document detected for {cmd[5:999999999999999999999999999999999999999]}.")
    elif cmd[0:4] == "exit":
        quit(0)
    elif cmd[0:6] == "repeat":
        if len(cmd) == 6:
            print("Invalid usage!\nUsage:\nrepeat [ANYTHING]")
        else:
            print(cmd[7:9999999999999999999999999999999999999999999999999])
    elif cmd[0:7] == "display":
        if len(cmd) == 7:
            os.system(f"cat {cmd[8:999999999999999999999999999999999999]}")
        else:
            if cmd[8:11] == "-su":
                os.system(f"sudo cat {cmd[8:99999999999999999999999999999999]}")
            else:
                print(f"Flag {cmd[8:9999999999999999999999999999999999999999999999999999]} not found!")
    elif cmd[0:5] == "clear":
        os.system("clear")
    elif cmd[0:3] == "dir":
        if len(cmd) == 3:
            print("Invalid usage!\nUsage:\ndir [DIRECTORY]")
        if cmd.find("-h") == -1:
            try:
                os.chdir(cmd[4:6942069420])
                cwd = os.getcwd()
            except FileNotFoundError:
                print(f"Error! Directory {cmd[4:9999999999999999999999999999]} not found!")
            except:
                print("Error! Unknown.")
        else:
            if cmd[4:6] == "-h":
                print("Changes the working directory.\nUsage:\ndir [DIRECTORY]")
            else:
                try:
                    os.chdir(cmd[4:6942069420])
                    cwd = os.getcwd()
                except FileNotFoundError:
                    print(f"Error! Directory {cmd[4:9999999999999999999999999999]} not found!")
                except:
                    print("Error! Unknown.")

    elif cmd[0:2] == "ls":
        print(str(os.listdir()).replace("[", "").replace("]", "").replace(",", "   ").replace("'", ""))
    else:
        print(f"Command {cmd} not found!")
