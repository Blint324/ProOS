import os

directory = os.getcwd()

f = open("dir.txt", "w")
f.write(directory)
f.close()
print("Directory successfully obtained.")
