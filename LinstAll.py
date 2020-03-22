#!/usr/bin/env python3
import os
import sys


def deb64():
    print("""
        \033[31m|$$|     $$          |$$$$$$|  |$$|       |$$|     |$$||$$|
        |$$|    |$$||$$|     |$$|    |$$$$$$|  |$$|  |$$|  |$$||$$|
        |$$|    |$$||$$$$$$|    |$$|   |$$|   |$$$$$$$$$$| |$$||$$|
        |$$$$$$||$$||$$  $$||$$$$$$|   |$$|  |$$|      |$$||$$||$$| V1.0\033[m

                 \033[36mA Tool For Installing Any Programs Easily
                    Coding By M.J. Bagheri Nejad (MJBN)
                            WebSite: MJBN.IR\033[m

        """)
    c = input("""
        Choose One of The Option Below:
        1 - Install Recommended Programs
        2 - Custom Install
        3 - Install What You Want
        4 - Install LAMP Stack (MariaDB, PHP)
        5 - Installing Kali Programs
        6 - Exit
        ==> """)
    if c == "1":
        program_name = ["uget", "vlc", "qbittorrent", "gimp", "tor", "google-chrome"]
        for i in program_name:
            if i == "google-chrome":
                os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
                os.system("apt-get install ./google-chrome-stable_current_amd64.deb")
                continue
            os.system("apt-get install {}".format(i))
        deb64()
    elif c == "2":
        program_name = ["filezilla", "git", "uget", "vlc", "qbittorrent", "google-chrome", "gimp", "tor",
                        "telegram-desktop", "aegisub", "libreoffice", "chromium", "godot3", "Steam", "Wine", "Atom"]
        for i in program_name:
            b = str(input("Do you wanna install {}?(Y/n) ".format(i)))
            if b == "Y":
                if i == "Atom":
                    os.system("wget -qO - https://packagecloud.io/AtomEditor/atom/gpgkey | sudo apt-key add")
                    os.system("echo 'deb [arch=amd64] https://packagecloud.io/AtomEditor/atom/any/ any main' >> /etc/apt/sources.list.d/atom.list")
                    os.system("apt-get update")
                    os.system("apt-get install atom")
                    continue
                if i == "Wine":
                    os.system("dpkg --add-architecture i386 && apt-get update")
                    os.system("apt-get install wine wine32 wine64 libwine libwine:i386 fonts-wine")
                    continue
                if i == "Steam":
                    os.system("echo 'deb http://deb.debian.org/debian/ buster main contrib non-free' >> /etc/apt/sources.list")
                    os.system("dpkg --add-architecture i386")
                    os.system("apt update")
                    os.system("apt install steam")
                    os.system("apt install libgl1:i386 mesa-vulkan-drivers:i386 mesa-vulkan-drivers")
                    continue
                if i == "google-chrome":
                    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
                    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")
                    continue
                os.system("apt-get install {}".format(i))
            else:
                continue
        deb64()
    elif c == "3":
        program_name = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", ""]
        for i in range(101):
            b = str(input("Enter Your Program Name(Enter \'exit\' to start installing): "))
            if b != "exit":
                program_name[i] = b
            else:
                break
        for i in range(101):
            os.system("apt-get install {}".format(program_name[i]))
        deb64()
    elif c == "4":
        os.system("apt-get install mariadb-server")
        os.system("systemctl start mariadb")
        os.system("apt-get install apache2 php libapache2-mod-php")
        os.system("apt-get install php-json php-mbstring php-zip php-gd php-xml php-curl php-mysql")
        os.system("wget https://files.phpmyadmin.net/phpMyAdmin/5.0.1/phpMyAdmin-5.0.1-all-languages.zip")
        os.system("unzip phpMyAdmin-5.0.1-all-languages.zip -d /opt")
        os.system("mv -v /opt/phpMyAdmin-5.0.1-all-languages /opt/phpMyAdmin")
        os.system("chown -Rfv www-data:www-data /opt/phpMyAdmin")
        print("Now You Should Follow The steps in \"LAMP Configuration.txt\" File")
        os.system("mysql_secure_installation")
        os.system("mysql -u root -p")
        # GRANT ALL ON *.* TO 'shovon'@'localhost' IDENTIFIED BY '123';
        # FLUSH PRIVILEGES;
        # \q
        deb64()
    elif c == "5":
        print("""
        \033[36mComing Soon...\033[m""")
        d = input("""
        What do you wanna do now?
        1 - Go Back (../)
        2 - Exit
        => """)
        if d == "1":
            deb64()
        elif d == "2":
            sys.exit()
    elif c == "6":
        sys.exit()
    else:
        deb64()


def deb32():
    print("""
        \033[31m|$$|     $$          |$$$$$$|  |$$|       |$$|     |$$||$$|
        |$$|    |$$||$$|     |$$|    |$$$$$$|  |$$|  |$$|  |$$||$$|
        |$$|    |$$||$$$$$$|    |$$|   |$$|   |$$$$$$$$$$| |$$||$$|
        |$$$$$$||$$||$$  $$||$$$$$$|   |$$|  |$$|      |$$||$$||$$| V1.0\033[m

                \033[36mA Tool For Installing Any Programs Easily
                    Coding By M.J. Bagheri Nejad (MJBN)
                            WebSite: MJBN.IR\033[m

        """)
    c = input("""
        Choose One of The Option Below:
        1 - Install Recommended Programs
        2 - Custom Install
        3 - Install What You Want
        4 - Install LAMP Stack (MariaDB, PHP)
        5 - Installing Kali Programs
        6 - Exit
        ==> """)
    if c == "1":
        program_name = ["uget", "vlc", "qbittorrent", "gimp", "tor", "google-chrome", "libreoffice"]
        for i in program_name:
            if i == "google-chrome":
                os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_i386.deb")
                os.system("apt-get install ./google-chrome-stable_current_i386.deb")
                continue
            os.system("apt-get install {}".format(i))
        deb32()
    elif c == "2":
        program_name = ["filezilla", "git", "uget", "vlc", "qbittorrent", "google-chrome", "gimp", "tor",
                        "telegram-desktop", "aegisub", "libreoffice", "chromium", "godot3", "Steam", "Wine"]
        for i in program_name:
            b = str(input("Do you wanna install {}?(Y/n) ".format(i)))
            if b == "Y":
                if i == "Wine":
                    os.system("apt-get install wine wine32 libwine fonts-wine")
                    continue
                if i == "Steam":
                    os.system(
                        "echo 'deb http://deb.debian.org/debian/ buster main contrib non-free' >> /etc/apt/sources.list")
                    os.system("apt-get update")
                    os.system("apt-get install steam")
                    os.system("apt-get install libgl1 mesa-vulkan-drivers")
                    continue
                if i == "google-chrome":
                    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
                    os.system("apt-get install ./google-chrome-stable_current_amd64.deb")
                    continue
                os.system("apt-get install {}".format(i))
            else:
                continue
        deb32()
    elif c == "3":
        program_name = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                        "", "", "", "", ""]
        for i in range(101):
            b = str(input("Enter Your Program Name(Enter \'exit\' to start installing): "))
            if b != "exit":
                program_name[i] = b
            else:
                break
        for i in range(101):
            os.system("apt-get install {}".format(program_name[i]))
        deb32()
    elif c == "4":
        os.system("apt-get install mariadb-server")
        os.system("systemctl start mariadb")
        os.system("apt-get install apache2 php libapache2-mod-php")
        os.system("apt-get install php-json php-mbstring php-zip php-gd php-xml php-curl php-mysql")
        os.system("wget https://files.phpmyadmin.net/phpMyAdmin/5.0.1/phpMyAdmin-5.0.1-all-languages.zip")
        os.system("unzip phpMyAdmin-5.0.1-all-languages.zip -d /opt")
        os.system("mv -v /opt/phpMyAdmin-5.0.1-all-languages /opt/phpMyAdmin")
        os.system("chown -Rfv www-data:www-data /opt/phpMyAdmin")
        print("Now You Should Follow The steps in \"LAMP Configuration.txt\" File")
        os.system("mysql_secure_installation")
        os.system("mysql -u root -p")
        deb32()
    elif c == "5":
        print("""
        \033[36mComing Soon...\033[m""")
        d = input("""
        What do you wanna do now?
        1 - Go Back (../)
        2 - Exit
        => """)
        if d == "1":
            deb32()
        elif d == "2":
            sys.exit()
    elif c == "6":
        sys.exit()
    else:
        deb32()


def main():
    print("""
        \033[31m|$$|     $$          |$$$$$$|  |$$|       |$$|     |$$||$$|
        |$$|    |$$||$$|     |$$|    |$$$$$$|  |$$|  |$$|  |$$||$$|
        |$$|    |$$||$$$$$$|    |$$|   |$$|   |$$$$$$$$$$| |$$||$$|
        |$$$$$$||$$||$$  $$||$$$$$$|   |$$|  |$$|      |$$||$$||$$| V1.0\033[m

                 \033[36mA Tool For Installing Any Programs Easily
                    Coding By M.J. Bagheri Nejad (MJBN)
                            WebSite: MJBN.IR\033[m

        """)
    a = input("""
        Please Choose Your Package Management (Distro):
        1 - APT (Debian, Ubuntu, Kubuntu, Lubuntu,...)
        2 - Pacman (Arch, Manjaro,...)
        3 - Dnf (Fedora,...)
        4 - ...
        5 - Exit
        => """)
    if a == "1":
        print("""
        \033[31m|$$|     $$          |$$$$$$|  |$$|       |$$|     |$$||$$|
        |$$|    |$$||$$|     |$$|    |$$$$$$|  |$$|  |$$|  |$$||$$|
        |$$|    |$$||$$$$$$|    |$$|   |$$|   |$$$$$$$$$$| |$$||$$|
        |$$$$$$||$$||$$  $$||$$$$$$|   |$$|  |$$|      |$$||$$||$$| V1.0\033[m

                \033[36mA Tool For Installing Any Programs Easily
                    Coding By M.J. Bagheri Nejad (MJBN)
                            WebSite: MJBN.IR\033[m

                """)
        b = input("""
        Please choose your architecture:
        1 - amd64 (x64)
        2 - i386 (x86/x32)
        3 - Go Back (../)
        4 - Exit
        => """)
        if b == "1":
            deb64()
        elif b == "2":
            deb32()
        elif b == "3":
            main()
        elif b == "4":
            sys.exit()
        else:
            main()
    elif a == "2":
        print("\033[36mComing Soon...\033[m")
        sys.exit()
    elif a == "3":
        print("\033[36mComing Soon...\033[m")
        sys.exit()
    elif a == "4":
        print("""
        \033[36mI don't have any plan for any other Package Management (Distro) now,
        But maybe in the future, I do something, Who knows\033[m""")
        sys.exit()
    elif a == "5":
        sys.exit()
    else:
        main()


if os.getuid() != 0:
    print("""
        This Script Requires Root Privilege,
        Pleas Run It With \"sudo\" or Change To Root User With Command \"su\" or \"sudo su\"""")
    sys.exit()
else:
    os.system("apt-get update")
    os.system("apt-get install wget")
    main()
