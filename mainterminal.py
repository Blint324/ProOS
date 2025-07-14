import os
from termcolor import colored

os.system("clear")
os.system("python3 data/config/bootexec.py")

print("Welcome to ProOS!")

if os.path.isdir("/etc") == False:
    print(colored("WARNING: You are not using Linux! Some commands are build with Linux bash in mind, and they might not work!", "yellow"))

print("Importing core libraries...")

import time
import datetime
import random
import linecache
import shutil
import sys
import math

print("Importing done.")
print("Defining variables...")

cmd = ""
cwd = os.getcwd()
trueCwd = __file__.replace("mainterminal.py","")
trueCwd = trueCwd[0:len(trueCwd) - 1]
user = ""
sys.set_int_max_str_digits(0)

print("Defining variables done.")
print("Creating log file...")

logTime = datetime.datetime.today()
f = open(f"{trueCwd}/data/logs/{logTime}.log", "w")
f.close()

print("Creating log file done.")

userFiles = 0
for file in os.listdir(f"{trueCwd}/data/users"):
    userFiles = userFiles + 1
f = open(f"{trueCwd}/data/config/autolog.conf", "r")
autoLog2 = f.read()
f.close()

print("Defining functions...")

def login():
    f = open(f"{trueCwd}/data/config/autolog.conf", "r")
    autoLog2 = f.read()
    f.close()

    if userFiles == 1:
        global userName
        userName = os.listdir(f"{trueCwd}/data/users")[0]
        userName = userName.replace(".user","")
    if autoLog2[0:5] == "false":
        if userFiles == 1:
            autoLog = input(colored("Hey! We noticed you only have one user registered, would you like to enable autologin? (This can be disabled any time by configuring the autolog.conf file in /data/config.) [y/N] ", "blue"))
            autoLog.lower()
            if autoLog == "":
                pass
            if autoLog == "n":
                pass
            elif autoLog == "y":
                f = open(f"{trueCwd}/data/config/autolog.conf", "w")
                f.write("true")
                f.close()
                f = open(f"{trueCwd}/data/config/autolog.conf", "r")
                autoLog2 = f.read()
                autoLog2 = str(autoLog2)
                f.close()
            else:
                print("Thats not an option!")
    else:
        pass
    while True:
        if autoLog2[0:4] == "true":
            break
        loginCmd = input(colored(f"{cwd}: ", "light_green"))
        loginCmd.lower()
        if loginCmd == "help":
            print("This is the login screen, if this is your first time booting up ProOS, follow these steps:\n1. mkuser [USERNAME]\n2. setpass [USERNAME],[PASSWORD]\n3. login [USERNAME].\nOtherwise, type login [USERNAME] and you will start logging in.")
        elif loginCmd[0:6] == "mkuser":
            if len(loginCmd) == 6:
                print("Invalid usage! Usage: mkuser [USERNAME]")
            else:
                mkuserSplit = loginCmd.split()
                if len(mkuserSplit) > 1:
                    f = open(f"{trueCwd}/data/users/{mkuserSplit[1]}.user", "w")
                    f.close()
                else:
                    print("Invalid usage! Usage: mkuser [USERNAME]")
        elif loginCmd[0:7] == "setpass":
            if len(loginCmd) == 7:
                print("Invalid usage! Usage: setpass [USERNAME],[PASSWORD]")
            else:
                setpassSplit = loginCmd.split()
                setpassSplit2 = setpassSplit[1].split(",")
                if len(setpassSplit2) > 1:
                    try:
                        f = open(f"{trueCwd}/data/users/{setpassSplit2[0]}.user", "w")
                        f.write(setpassSplit2[1])
                        f.close()
                    except FileNotFoundError:
                        print(colored(f"Error! User file {setpassSplit2[0]} not found.", "red"))
                else:
                    print("Invalid usage! Usage: setpass [USERNAME],[PASSWORD]")
        elif loginCmd[0:5] == "login":
            if len(loginCmd) == 5:
                print("Invalid usage! Usage: login [USERNAME]")
            else:
                global loginSplit
                loginSplit = loginCmd.split()
                if len(loginSplit) > 1:
                    try:
                        f = open(f"{trueCwd}/data/users/{loginSplit[1]}.user", "r")
                        loginPass = f.read()
                        loginInput = input("Password: ")
                        if loginInput == loginPass:
                            break
                        else:
                            print("Wrong password!")
                    except FileNotFoundError:
                        print(colored(f"Error! User file {loginSplit[1]} not found.", "red"))
                else:
                    print("Invalid usage! Usage: login [USERNAME]")
        elif loginCmd == "exit":
            quit(0)
        else:
            wrongLoginCmd = loginCmd.split()
            if len(wrongLoginCmd) > 1:
                print(f"Command {wrongLoginCmd[0]} not found!")
            else:
                print(f"Command {loginCmd} not found!")

login()

print("Starting main loop...")

while True:
    if autoLog2[0:5] == "false":
        cmd = input(colored(f"{cwd}${loginSplit[1]}: ", "light_blue"))
        f = open(f"{trueCwd}/data/logs/{logTime}.log", "a")
        f.write(f"{datetime.datetime.today()}:  User {loginSplit[1]} executed command {cmd}\n")
        f.close()
    else:
        cmd = input(colored(f"{cwd}${userName}: ", "light_blue"))
        f = open(f"{trueCwd}/data/logs/{logTime}.log", "a")
        f.write(f"{datetime.datetime.today()}:  User {userName} executed command {cmd}\n")
        f.close()
    cmd.lower()

    # Checking for commands

    if cmd[0:3] == "ver":
        if len(cmd) == 3:
            print("ProOS version Alpha 1.8")
        else:
            if cmd[3:6] == " -d":
                print("ProOS version Alpha 1.8\nCredits:\nBálint Vámosi: Lead developer.\nLinus Torvalds and the Linux team: Inspiration for this mockup.\nGergő Vámosi: Co-Owner of the project.")
            elif cmd[3:6] == " -h":
                print("Displays the current version of ProOS.\nUsage:\nver [FLAGS]")
    elif cmd[0:4] == "help":
        if len(cmd) == 4:
            print("Basic commands:\nrepeat\nexit\nver\ndisplay\ndir\nls\nexec\nwrite\nqm.add\nqm.sub\nqm.mult\nqm.div\nmv\ncp\ncrt")
        else:
            if cmd[5:7] == "-a":
                print("repeat exit ver display dir ls exec write qm.add qm.sub qm.mult qm.div restart crt cp pyexec mv qm.rand qm.fib qm.fac login contains")
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
            elif cmd[5:12] == "qm.rand":
                print("Prints a random integer in the range of two values.\nUsage:\nqm.rand [INT1],[INT2]\nside note: before everyone argues about what it stands for, qm is for QuickMath.")
            elif cmd[5:11] == "qm.fib":
                print("Generates a certain amount of fibonacci numbers.\nUsage:\nqm.fib [NUM]\nside note: before everyone argues about what it stands for, qm is for QuickMath.")
            elif cmd[5:11] == "qm.fac":
                print("Generates the factorial of a number.\nUsage:\nqm.fac [NUM]\nside note: before everyone argues about what it stands for, qm is for QuickMath.")
            elif cmd[5:10] == "login":
                print("Executes the login script.")
            elif cmd[5:13] == "contains":
                print("Searches for a substring in a string.\nUsage:\ncontains [<FLAGS>]\nFlags:\n-f: Searches in a file.")
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
                print(colored(f"Error! Directory {cmd[4:9999999999999999999999999999]} not found!", "red"))
            except:
                print(colored("Error! Unknown.", "red"))
        else:
            if cmd[4:6] == "-h":
                print("Changes the working directory.\nUsage:\ndir [DIRECTORY]")
            else:
                try:
                    os.chdir(cmd[4:6942069420])
                    cwd = os.getcwd()
                except FileNotFoundError:
                    print(colored(f"Error! Directory {cmd[4:9999999999999999999999999999]} not found!", "red"))
                except:
                    print(colored("Error! Unknown.", "red"))
    elif cmd[0:2] == "ls":
        if len(cmd) == 2:
            print(str(os.listdir()).replace("[", "").replace("]", "").replace(",", "   ").replace("'", ""))
        else:
            if cmd[5:7] == "-r":
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
            writeMode = input("What mode to write in? (W/a) ")
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
                print(colored("Error! Must only use commas and numbers for qm operations.", "red"))
            except:
                print(colored("Error! Unknown.", "red"))
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
                print(colored("Error! Must only use commas and numbers for qm operations.", "red"))
            except:
                print(colored("Error! Unknown.", "red"))
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
                print(colored("Error! Must only use commas and numbers for qm operations.", "red"))
            except:
                print(colored("Error! Unknown.", "red"))
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
                print(colored("Error! Must only use commas and numbers for qm operations.", "red"))
            except:
                print(colored("Error! Unknown.", "red"))
    elif cmd[0:7] == "restart":
        os.system(f"python3 {trueCwd}/restart.py")
        quit(0)
    elif cmd[0:2] == "rm":
        if len(cmd) == 2:
            print("Invalid usage! Usage: rm [<FLAGS>] [FILE]")
        else:
            if cmd[3:6] == "-su":
                try:
                    os.system(f"sudo rm {cmd[7:9999999999999999999999999]}")
                except FileNotFoundError:
                    print(colored(f"Error! File {cmd[7:99999999999999999999999999]} doesn't exit!", "red"))
                except:
                    print(colored("Error! Unknown.", "red"))
            elif cmd[3:5] == "-h":
                print("Removes a file.")
            else:
                try:
                    os.remove(cmd[3:9999999999999999999])
                except FileNotFoundError:
                    print(colored(f"Error! File {cmd[7:99999999999999999999999999999]} doesn't exist!", "red"))
                except:
                    print(colored("Error! Unknown.", "red"))
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
                    print(colored(f"Error! File {cpSplit2[0]} or {cpSplit2[1]} doesn't exist!", "red"))
                except:
                    print(colored("Error! Unknown.", "red"))
            else:
                print(colored("Error! Two files must be provided.", "red"))
    elif cmd[0:6] == "pyexec":
        if len(cmd) == 6:
            print("Invalid usage! Usage: pyexec [COMMAND]")
        else:
            try:
                exec(cmd[7:999999999999999999999999999999999999999999])
            except NameError:
                print(colored("ERROR: NameError", "red"))
            except ValueError:
                print(colored("ERROR: ValueError", "red"))
            except IndexError:
                print(colored("ERROR: IndexError", "red"))
            except FileNotFoundError:
                print(colored("ERROR: FileNotFoundError", "red"))
            except:
                print(colored("ERROR: Unknown", "red"))
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
                    print(colored(f"Error! File {mvSplit2[0]} or {mvSplit2[1]} not found.", "red"))
                except:
                    print(colored("Error! Unknown.", "red"))
            else:
                print("Ivalid usage! Usage: mv [FILE] [DIRECTORY]")
    elif cmd[0:7] == "qm.rand":
        if len(cmd) == 7:
            print("Invalid usage! Usage: qm.rand [INT1],[INT2]")
        else:
            randSplit = cmd.split()
            randSplit2 = randSplit[1].split(",")
            if len(randSplit2) > 1:
                try:
                    print(random.randint(int(randSplit2[0]), int(randSplit2[1])))
                except ValueError:
                    print(colored("Error! Must use two integers.", "red"))
            else:
                print(colored("Error! Must use two integers for qm.rand.", "red"))
    elif cmd[0:6] == "qm.fib":
        if len(cmd) == 6:
            print("Invalid usage! Usage: qm.fib [NUM]")
        else:
            try:
                qmFibSplit = cmd.split()
                qmFibNext = 1
                qmFib1 = 0
                qmFib2 = 1
                if len(qmFibSplit) > 1:
                    print("0", end=" ")
                    for i in range(int(qmFibSplit[1])):
                        print(qmFibNext, end=" ")
                        qmFib1, qmFib2 = qmFib2, qmFibNext
                        qmFibNext = qmFib1 + qmFib2
                else:
                    print("Invalid usage! Usage: qm.fib [NUM]")
            except ValueError:
                print(colored("Error! Must use an integer.", "red"))
            except:
                print(colored("Error! Unknown.", "red"))
    elif cmd[0:6] == "qm.fac":
        if len(cmd) == 6:
            print("Invalid usage! Usage: qm.fac [NUM]")
        else:
            try:
                qmFacSplit = cmd.split()
                qmFacInput = int(qmFacSplit[1])
                if len(qmFacSplit) > 1:
                    print(math.factorial(qmFacInput))
                else:
                    print("Invalid usage! Usage: qm.fac [NUM]")
            except ValueError:     
                print(colored("Error! Must use an integer.", "red"))    
            except:    
                print(colored("Error! Unknown.", "red"))
    elif cmd[0:8] == "contains":
        if len(cmd) == 8:
            print("Invalid usage! Usage: contains [<FLAGS>]")
        else:
            contSplit = cmd.split()
            if cmd[9:11] == "-f":
                try:
                    f = open(f"{contSplit[2]}", "r")
                    contFile = f.read()
                    contFileName = contSplit[2]
                    contSearch = input("Text to search for: ")
                    if contSearch in contFile:
                        print(f"{contSearch} located at character {contFile.find(contSearch)} in {contFileName}.")
                    else:
                        print(f"{contSearch} not found in {contFileName}.")
                except FileNotFoundError:
                    print(colored(f"Error! File {contFileName} doesn't exist.", "red"))
                except:
                    print(colored("Error! Unknown.", "red"))
            elif cmd[9:11] == "-h":
                print("Locates a substring inside a string or file.\nFlags:\n-f: Searches in file.\n-h: Shows this help prompt.\nUsage:\ncontains [<FLAGS>] [TEXT/FILE]")
            else:
                contSearch = input("Text to search for: ")
                if contSearch in cmd[9:99999999999999999999999999999999999999]:
                    print(f"{contSearch} located at character {cmd[9:999999999999999999999999999].find(contSearch)}.")
                else:
                    print(f"{contSearch} not found in {cmd[9:999999999999999999999999999999999999]}.")
    elif cmd[0:5] == "login":
        f = open(f"{trueCwd}/data/config/autolog.conf", "r")
        autoLog2 = f.read()
        f.close()
        login()
        print(colored("INFO: If nothing gets outputted, autolog.conf is set to true.", "blue"))
    else:
        if not cmd == "":
            cmdNotFound = cmd.split()
            print(f"Command {cmdNotFound[0]} not found!")
        else:
            print(f"Command {cmd} not found!")
