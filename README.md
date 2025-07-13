# ProOS

## Introduction

ProOS (Short for Programmer OS) is a mockup operating system made in various languages such as C, Bash, and Python. I'm making this purely for fun and not for actual purpose, and I will likely use it to practice my coding skills in different languages.
This will most likely support Windows in the future, however at the moment I'm just a single person writing this, so dont expect ports soon. Currently it only works for Linux.
Requirements:
- GNU Linux
- GCC and Python3
- A lot of programming knowlege.
- The termcolor module for Python

## Installation

ProOS is reccomended to be installed on GNU Linux, as it relies heavily on Linux bash and is undocumented and untested on Windows or MacOS.
FreeBSD is also undocumented, but may have a higher chance of fully working.
To install ProOS, first download the source code, the main branch is reccomended, as it has the latest stable release, however, if you want the latest commands, go with the experimental branches, but be aware, as that can be unstable and may have many bugs.
Once you have your source code of source, simply run setup.py and it will create everything for you, once that's done, it will autostart mainterminal.py.

## Quick Start

Once you're in mainterminal.py, you will have to log in, you can get help via using the help command at the login screen, but I will detail the login process here aswell:
1. Run `mkuser <USERNAME>` to create a user file.
2. Once that's done, run `setpass <USERNAME>` to set the password for that user
3. And finally, run `login <USERNAME>` to log in, where you will have to enter your previously set password.
When you're outside of the login screen, you will most likely be in the main loop. The main loop runs the commands of the program, which you can print by running `help -a`.
From there, it should be straight forward. If you need help, please open an issue for the program on the Github website and we will gladly help.
Thank you for choosing ProOS.
