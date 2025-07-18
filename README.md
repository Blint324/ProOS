## Introduction

ProShell (Short for Programmer Shell) is a mockup operating system/shell made in Python. I'm making this purely for fun and not for actual purpose, and I will likely use it to practice my coding skills in different languages.
This will most likely support Windows in the future, however at the moment I'm just a single person writing this, so dont expect ports soon. Currently it only works for Linux.
Requirements:
- GNU Linux
- Python3
- A lot of programming knowlege
- The termcolor library for Python

## Downloading files

ProShell is recommended to be installed on GNU Linux, as it relies heavily on Linux bash and is undocumented and untested on Windows or MacOS.
FreeBSD is also undocumented, but may have a higher chance of fully working.
To install ProShell, first download the source code, the proshell-stable branch is recommended, as it has the latest stable release, however, if you want the latest commands, go with the experimental branches, but be aware, as that can be unstable and may have many bugs.

## Installation & Beginner's guide

Once you've downloaded the files, you will have to install the main shell itself. To do this, run setup.py.
This will set up all of the core files and directories for you, however you're not done yet.
Once the automatic section of the setup is done, you will be greeted with a terminal. This is used to configure the necessary files.
To fully install and configure the shell, you must first set the directory, which you can do by executing these following commands in the setup terminal:
`distroconf [DISTRO]` to set the distro you are using (this will be used later)
`install pip` if you haven't already
`exec pip install --break-system-packages [DEPENDENCIES]` currently, there are no dependencies you have to install here, but later on this can be a good troubleshooter if you get an error on startup.
`exec nvim mainterminal.py`
Or for people that prefer nano:
`exec nano mainterminal.py`
Then once you're in, edit the line below the comment that says "EDIT THE BELOW LINE!" to be `trueCwd = "[THE DIRECTORY YOU PUT PROSHELL IN]"`
Finally, run `start` to execute mainterminal.py.
Once you're in mainterminal.py, you will have to create and log into a user, to do that, run the following commands:
1. `mkuser <USERNAME>` to create a user file.
2. Once that's done, run `setpass <USERNAME>,<PASSWORD>` to set the password for that user
3. And finally, run `login <USERNAME>` to log in, where you will have to enter your previously set password.
When you're outside of the login screen, you will most likely be in the main loop. The main loop runs the commands of the program, which you can print by running `help -a`.
From there, it should be straight forward. If you need help, please open an issue for the program on the Github website and we will gladly help.

## Info

ProShell at the moment is only tested for Debian GNU Linux, and may be unstable on other distributions or OS's.
No, ProShell is _not_ an actual os, and is simply a mockup that I'm making with a few friends to practice my coding skills.
