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
import shutil

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
            print("ProOS version u1.4")
        else:
            if cmd[3:6] == " -d":
                print("ProOS version u1.4\nCredits:\nBálint Vámosi: Lead developer.\nLinus Torvalds and the Linux team: Inspiration for this mockup.\nGergő Vámosi: Co-Owner of the project.")
            elif cmd[3:6] == " -h":
                print("Displays the current version of ProOS.\nUsage:\nver [FLAGS]")
    elif cmd[0:4] == "help":
        if len(cmd) == 4:
            print("Basic commands:\nrepeat\nexit\nver\ndisplay\ndir\nls\nexec\nwrite\nqm.add\nqm.sub\nqm.mult\nqm.div\nmv\ncp\ncrt")
        else:
            if cmd[5:7] == "-a":
                print("repeat exit ver display dir ls exec write qm.add qm.sub qm.mult qm.div restart crt cp pyexec")
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
            elif cmd[5:11] == "qm.add":
                print("Adds two values together.\nUsage:\nqm.add [VALUE],[VALUE]\nside note: before everyone argues about what it stands for, qm is for QuickMath.")
            elif cmd[5:11] == "qm.sub":
                print("Subtracts two values.\nUsage:\nqm.sub [VALUE],[VALUE]\nside note: before everyone argues about what it stands for, qm is for QuickMath.")
            elif cmd[5:11] == "qm.div":
                print("Divides two values.\nUsage:\nqm.add [VALUE],[VALUE]\nside note: before everyone argues about what it stands for, qm is for QuickMath.")
            elif cmd[5:12] == "qm.mult":
                print("Multiplies two values together.\nUsage:\nqm.add [VALUE],[VALUE]\nside note: before everyone argues about what it stands for, qm is for QuickMath.")
            elif cmd[5:9] == "help":
                print("Prints help of commands.\nFlags:\n-a: Shows all commands.\nUsage:\nhelp [<FLAGS>] [<COMMAND>]")
            elif cmd[5:12] == "restart":
                print("Restarts the program.")
            elif cmd[5:8] == "crt":
                print("Creates a file.\nUsage:\ncrt [FILENAME]")
            elif cmd[5:7] == "rm":
                print("Removes a file.\nFlags:\n-su: Runs as superuser.\n-h: Prints a help prompt.\nUsage:\nrm [<FLAGS>] [FILE]")
            elif cmd[5:7] == "cp":
                print("Copies a file.\nUsage:\ncp [FILE],[DESTINATION]")
            elif cmd[5:11] == "pyexec":
                print("Executes code in Python.\nUsage:\npyexec [COMMAND]")
            elif cmd[5:7] == "mv":
                print("Moves a file.\nUsage:\nmv [FILE] [FOLDER]")
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
            writeCont = input("What to write? ")
            f.write(writeCont)
            f.close()
    elif cmd[0:6] == "qm.add":
        if len(cmd) == 6:
            print("Invalid usage! Usage: qm.add [VALUE],[VALUE]")
        else:
            qmSplit = cmd.split()
            qmSplit2 = qmSplit[1].split(",")
            try:
                qm1 = float(qmSplit2[0])
                qm2 = float(qmSplit2[1])
                print(qm1 + qm2)
            except ValueError:
                print("Only use commas and numbers!")
            except:
                print("An unknown error occoured!")
    elif cmd[0:6] == "qm.sub":
        if len(cmd) == 6:
            print("Invalid usage! Usage: qm.sub [VALUE],[VALUE]")
        else:
            qmSplit = cmd.split()
            qmSplit2 = qmSplit[1].split(",")
            try:
                qm1 = float(qmSplit2[0])
                qm2 = float(qmSplit2[1])
                print(qm1 - qm2)
            except ValueError:
                print("Only use commas and numbers!")
            except:
                print("An unknown error occoured!")
    elif cmd[0:6] == "qm.div":
        if len(cmd) == 6:
            print("Invalid usage! Usage: qm.div [VALUE],[VALUE]")
        else:
            qmSplit = cmd.split()
            qmSplit2 = qmSplit[1].split(",")
            try:
                qm1 = float(qmSplit2[0])
                qm2 = float(qmSplit2[1])
                print(qm1 / qm2)
            except ValueError:
                print("Only use commas and numbers!")
            except:
                print("An unknown error occoured!")
    elif cmd[0:7] == "qm.mult":
        if len(cmd) == 6:
            print("Invalid usage! Usage: qm.mult [VALUE],[VALUE]")
        else:
            qmSplit = cmd.split()
            qmSplit2 = qmSplit[1].split(",")
            try:
                qm1 = float(qmSplit2[0])
                qm2 = float(qmSplit2[1])
                print(qm1 * qm2)
            except ValueError:
                print("Only use commas and numbers!")
            except:
                print("An unknown error occoured!")
    elif cmd[0:7] == "restart":
        os.system("bash restart.sh")
        quit(0)
    elif cmd[0:2] == "rm":
        if len(cmd) == 2:
            print("Invalid usage! Usage: rm [<FLAGS>] [FILE]")
        else:
            if cmd[3:6] == "-su":
                try:
                    os.system(f"sudo rm {cmd[7:9999999999999999999999999]}")
                except FileNotFoundError:
                    print(f"Error! File {cmd[7:99999999999999999999999999]} doesn't exit!")
                except:
                    print("Error! Unknown.")
            elif cmd[3:5] == "-h":
                print("Removes a file.")
            else:
                try:
                    os.remove(cmd[3:9999999999999999999])
                except FileNotFoundError:
                    print(f"Error! File {cmd[7:99999999999999999999999999999]} doesn't exist!")
                except:
                    print("Error! Unknown.")
    elif cmd[0:3] == "crt":
        if len(cmd) == 3:
            print("Invalid usage! Usage: crt [FILENAME]")
        else:
            f = open(f"{cmd[4:999999999999999999999]}", "w")
            f.close()
    elif cmd[0:2] == "cp":
        if len(cmd) == 2:
            print("Invalid usage! Usage: cp [FILE],[FILEPATH]")
        else:
            cpSplit = cmd.split()
            cpSplit2 = cpSplit[1].split(",")
            if len(cpSplit2) > 1:
                try:
                    shutil.copy(cpSplit2[0], cpSplit2[1])
                except FileNotFoundError:
                    print(f"Error! File {cpSplit2[0]} or {cpSplit2[1]} doesn't exist!")
                except:
                    print("Error! Unknown.")
            else:
                print("Put two files!")
    elif cmd[0:6] == "pyexec":
        if len(cmd) == 6:
            print("Invalid usage! Usage: pyexec [COMMAND]")
        else:
            try:
                exec(cmd[7:999999999999999999999999999999999999999999])
            except NameError:
                print("ERROR: NameError")
            except ValueError:
                print("ERROR: ValueError")
            except IndexError:
                print("ERROR: IndexError")
            except FileNotFoundError:
                print("ERROR: FileNotFoundError")
            except:
                print("ERROR: Unknown")
    elif cmd[0:2] == "mv":
        if len(cmd) == 2:
            print("Invalid usage! Usage: mv [FILE] [DIRECTORY]")
        else:
            mvSplit = cmd.split()
            mvSplit2 = mvSplit[1].split(",")
            if len(mvSplit2) > 1:
                try:
                    shutil.move(mvSplit2[0], mvSplit2[1])
                except FileNotFoundError:
                    print(f"Error! File {mvSplit2[0]} or {mvSplit2[1]} not found!")
                except:
                    print("Error! Unknown.")
            else:
                print("Ivalid usage! Usage: mv [FILE] [DIRECTORY]")
    else:
        print(f"Command {cmd} not found!")
