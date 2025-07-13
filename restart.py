import os

cwd = os.getcwd()
mnTerminal = __file__.replace("restart.py","mainterminal.py")
os.system(f"python3 {mnTerminal}")
