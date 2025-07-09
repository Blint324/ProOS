import os

os.system("clear")

print("Welcome to ProOS!")
print("Importing core libraries...")

import time
import datetime
import random

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
            print("ProOS version u1.0")
        else:
            if cmd[3:6] == " -d":
                print("ProOS version u1.0\nCredits:\n Bálint Vámosi: Lead developer.\nLinus Torvalds and the Linux team:Inspiration for this mockup.")
    
            elif cmd[3:6] == " -h":
                print("Displays the current version of ProOS.\nUsage:\nver [FLAGS]")
    elif cmd[0:4] == "help":
        if len(cmd) == 4:
            print("Basic commands:\nrepeat\nexit\nver.")
        else:
            if cmd[5:8] == "ver":
                print("Prints the current version of ProOS.\nFlags:\n-d: Displays more detailed info about ProOS.\n-h: Displays help for the command.")
            elif cmd[5:9] == "exit":
                print("Exits the program.")
            elif cmd[5:11] == "repeat":
                print("Repeats whatever you put next to it.")
            else:
                print(f"No help document detected for {cmd[5:999999999999999999999999999999999999999]}.")
    elif cmd[0:4] == "exit":
        quit(0)
    elif cmd[0:6] == "repeat":
        if len(cmd) == 6:
            print("Invalid usage!\nUsage:\nrepeat [ANYTHING]")
        else:
            print(cmd[6:9999999999999999999999999999999999999999999999999])
