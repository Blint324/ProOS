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
            print("ProOS version u1.1")
        else:
            if cmd[3:6] == " -d":
                print("ProOS version u1.0\nCredits:\nBálint Vámosi: Lead developer.\nLinus Torvalds and the Linux team: Inspiration for this mockup.\nGergő Vámosi: Co-Owner of the project.")
    
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
    else:
        print(f"Command {cmd} not found!")
