print("Welcome to the ProOS setup! This will be quick...")
print("Importing core libraries...")
import os
from termcolor import colored
import time
print("Importing done!")

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
print("Setup done!")
print("Welcome to ProOS, we hope you enjoy ;)")

time.sleep(1)
os.system("clear")
autoTime = 10
for i in range(10):
    print(f"Autostarting ProOS in {autoTime}, Press CTRL + C to cancel.")
    time.sleep(1)
    autoTime = autoTime - 1
    os.system("clear")
os.system("python3 mainterminal.py")
