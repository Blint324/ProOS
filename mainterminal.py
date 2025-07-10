import os

os.system("clear")

print("Welcome to ProOS!")

if os.path.isdir("/etc") == False:
    print("WARNING: You are not using Linux! Some commands are build with Linux bash in mind, and they might not work!")

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
            print("ProOS version u1.3")
        else:
            if cmd[3:6] == " -d":
                print("ProOS version u1.3\nCredits:\nBálint Vámosi: Lead developer.\nLinus Torvalds and the Linux team: Inspiration for this mockup.\nGergő Vámosi: Co-Owner of the project.")
    
            elif cmd[3:6] == " -h":
                print("Displays the current version of ProOS.\nUsage:\nver [FLAGS]")
    elif cmd[0:4] == "help":
        if len(cmd) == 4:
            print("Basic commands:\nrepeat\nexit\nver\ndisplay\ndir\nls\nexec\nwrite.")
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
                print("Lists the contents of the current working directory.\nFlags:\n-h: Shows this help text.\n-r: Operates recursively.\nUsage:\nls [<FLAGS>] [<DIRECTORY>]")
            elif cmd[5:9] == "exec":
                print("Executes whatever you put next to it in bash.\nFlags:\n-su: Runs command as superuser.\n-h: Displays this help text.")
            elif cmd[5:10] == "write":
                print("Writes to a file, either appends or overwrites.\nUsage:\nwrite [FILE]")
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
            print("Invalid usage!\nUsage:\ndisplay [FILE]")
        else:
            if cmd[8:11] == "-su":
                os.system(f"sudo cat {cmd[12:99999999999999999999999999999999]}")
            else:
                f = open(f"{cmd[8:99999999999999999999999999999]}", "r")
                print(f.read())
                f.close()
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
        if len(cmd) == 2:
            print(str(os.listdir()).replace("[", "").replace("]", "").replace(",", "   ").replace("'", ""))
        else:
            if cmd[3:5] == "-r":
                if not cmd[6:8] == "-h":
                    os.system(f"ls -R {cmd[6:999999999999999999999999999999]}")
                else:
                    print("Flag error! Can't use -h and -r at the same time.")
            elif cmd[3:5] == "-h":
                print("Lists the files and directories in the current working directory.\nFlags:\n-h: Shows this help text.\n-r: Operates recursively.\nUsage:\nls [<FLAGS>] [<DIRECTORY>]")
            else:
                os.system(f"ls {cmd[3:999999999999999999999]}")
    elif cmd[0:4] == "exec":
        if cmd[5:8] == "-su":
            os.system(f"sudo {cmd[9:999999999999999999999999]}")
        elif cmd[5:7] == "-h":
            print("Executes whatever you put next to it in bash.\nFlags:\n-su: Runs command as superuser.\n-h: Displays this help text.")
        else:
            os.system(cmd[5:99999999999999999999])
    elif cmd[0:5] == "write":
        if len(cmd) == 5:
            print("Invalid usage! Usage: write [FILE]")
        else:
            writeMode = input("What mode to write in? (Default: overwrite) (W/A) ")
            writeMode = writeMode.lower()
            if writeMode == "":
                writeMode = "w"
            f = open(f"{cmd[6:999999999999999999]}", f"{writeMode}")
            writeCont = input("What to write?")
            f.write(writeCont)
            f.close()

    else:
        print(f"Command {cmd} not found!")
