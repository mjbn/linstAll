#!/usr/bin/env python3
import os, sys

class main():
    def __init__(self):
        os.system("mkdir -p ~/.LinstAll && touch ~/.LinstAll/.la")
        os.system("(ls /usr/bin | grep linstall) > ~/.LinstAll/.la")
        file = open("~/.LinstAll/.la")
        lines = file.readlines()
        if(lines[0]!=""):
            os.system("~/.LinstAll/LinstAll.py")
        else:
            os.system("(ls ~ | grep LinstAll) > ~/.LinstAll/.la")
            file = open("~/.LinstAll/.la")
            lines = file.readlines()
            if(lines[0]!=""):
                os.system("cp ~/LinstAll ~/.LinstAll && sudo cp ./LinstAll/Installation.py /usr/bin/linstall && sudo chmod +x /usr/bin/linstall ~/.LinstAll/LinstAll.py && ~/.LinstAll/LinstAll.py")
            else:
                os.system("git clone https://github.com/MJBN/LinstAll.git ~/")
                os.system("cp ~/LinstAll ~/.LinstAll && sudo cp ./LinstAll/Installation.py /usr/bin/linstall && sudo chmod +x /usr/bin/linstall ~/.LinstAll/LinstAll.py && ~/.LinstAll/LinstAll.py")



if os.getuid() != 0:
    print("""
        This Script Requires Root Privilege,
        Please Run It With \"sudo\" or Change To Root User With Command \"su\" or \"sudo su\"""")
    sys.exit()
else:
    main()
