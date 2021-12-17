#!/usr/bin/env python3
from os import system, getuid
from sys import exit
from subprocess import run, PIPE


if getuid() != 0:
    print("""
        This Script Requires Root Privilege,
        Please Run It With \"sudo\" or Change To Root User With Command \"su\" or \"sudo su\"""")
    exit()
else:
    system("mkdir -p ~/.config/linstall && touch ~/.config/linstall/config.toml")
    ins = run(['ls', '/bin/linstall'], stdout=PIPE).stdout.decode('UTF-8')
    if(ins.find('linstall') == -1):
        system("cp ~/linstAll/linstall.py /bin/linstall && sudo chmod +x /usr/bin/linstall")
    
    print("linstall is installed")
