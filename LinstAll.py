#!/usr/bin/env python3
import os, sys


la_d="\n\t\033[31m|$$|     $$          |$$$$$$|  |$$|       |$$|     |$$||$$|\n\t|$$|    |$$||$$|     |$$|    |$$$$$$|  |$$|  |$$|  |$$||$$|\n\t|$$|    |$$||$$$$$$|    |$$|   |$$|   |$$$$$$$$$$| |$$||$$|\n\t|$$$$$$||$$||$$  $$||$$$$$$|   |$$|  |$$|      |$$||$$||$$| V1.0\033[m\n\n\t\t\033[36mA Tool For Installing Any Programs Easily\n\t\tCoding By M.J. Bagheri Nejad (MJBN)\n\t\t\tWebSite: MJBN.IR\033[m"
la_kali="\n\t\033[31m|$$|     $$          |$$$$$$|  |$$|       |$$|     |$$||$$|\n\t|$$|    |$$||$$|     |$$|    |$$$$$$|  |$$|  |$$|  |$$||$$|\n\t|$$|    |$$||$$$$$$|    |$$|   |$$|   |$$$$$$$$$$| |$$||$$|\n\t|$$$$$$||$$||$$  $$||$$$$$$|   |$$|  |$$|      |$$||$$||$$| V1.0\033[m\n\n\t\t\033[36mA Tool For Installing Any Programs Easily\n\t\tCoding By M.J. Bagheri Nejad (MJBN)\n\t\t\tWebSite: MJBN.IR\033[m\n\tBefore updating your system , please remove all\n\t\tKali-linux repositories to avoid any kind of problem.\033[m"
class main:
    def __init__(self):
        print(la_d)
        a = input("""
            Please Choose Your Package Management (Distro):
            1 - APT (Debian, Ubuntu, Kubuntu, Lubuntu,...)
            2 - Pacman (Arch, Manjaro,...)
            3 - Dnf (Fedora,...)
            4 - ...
            5 - Exit
            => """)
        if a == "1":
            deb()
        elif a == "2":
            arch()
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
    
class deb(main):
    def __init__(self):
        os.system("apt-get update")
        os.system("apt-get install wget")
        print("")
        print("")
        print(la_d)
        b = input("""
            Please choose your architecture:
            1 - amd64 (x64)
            2 - i386 (x86/x32)
            3 - Go Back (../)
            4 - Exit
            => """)
        if b == "1":
            deb.deb64()
        elif b == "2":
            deb.deb32()
        elif b == "3":
            main()
        elif b == "4":
            sys.exit()
        else:
            main()
    def deb64(self):
        print(la_d)
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
            program_name = ["uget", "vlc", "qbittorrent", "gimp", "tor", "vivaldi", "libreoffice"]
            for i in program_name:
                if i == "vivaldi":
                    os.system("echo 'deb http://repo.vivaldi.com/stable/deb/ stable main' >> /etc/apt/sources.list.d/vivaldi.list")
                    os.system("apt-get update")
                os.system("apt-get install {}".format(i))
            deb.deb64()
        elif c == "2":
            program_name = ["filezilla", "git", "uget", "vlc", "qbittorrent", "google-chrome", "gimp", "tor",
                            "telegram-desktop", "aegisub", "libreoffice", "chromium", "godot3", "Steam", "Wine", "Atom", "vivaldi"]
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
                        os.system("apt-get update")
                        os.system("apt-get install steam")
                        os.system("apt-get install libgl1:i386 mesa-vulkan-drivers:i386 mesa-vulkan-drivers")
                        continue
                    if i == "google-chrome":
                        os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
                        os.system("apt-get install ./google-chrome-stable_current_amd64.deb")
                        continue
                    if i == "vivaldi":
                        os.system("echo 'deb http://repo.vivaldi.com/stable/deb/ stable main' >> /etc/apt/sources.list.d/vivaldi.list")
                        os.system("apt-get update")
                    os.system("apt-get install {}".format(i))
                else:
                    continue
            deb.deb64()
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
            deb.deb64()
        elif c == "4":
            os.system("apt-get install mariadb-server apache2 php libapache2-mod-php php-json php-mbstring php-zip php-gd php-xml php-curl php-mysql")
            os.system("systemctl enable mariadb")
            os.system("systemctl start mariadb")
            os.system("wget https://files.phpmyadmin.net/phpMyAdmin/5.0.1/phpMyAdmin-5.0.1-all-languages.zip")
            os.system("unzip phpMyAdmin-5.0.1-all-languages.zip -d /opt")
            os.system("mv -v /opt/phpMyAdmin-5.0.1-all-languages /opt/phpMyAdmin")
            os.system("chown -Rfv www-data:www-data /opt/phpMyAdmin")
            os.system("mkdir -p /etc/apache2/sites-available/ && cp ./conf/arch/phpmyadmin.conf /etc/apache2/sites-available/")
            os.system("echo 'Listen 8080' >> /etc/apache2/ports.conf")
            os.system("mysql_secure_installation")
            os.system("clear")
            print("Now You Should Follow The steps in \"CreateADatabase.txt\" File")
            print("")
            print("")
            os.system("mysql -u root -p")
            os.system("systemctl enable apache2")
            os.system("systemctl start apache2")
            deb.deb64()
        elif c == "5":
            print(la_kali)
            d = int(input("""
            1 - Add Kali repositories & Update
            2 - View Categories
            => """))
            if d == 1:
                print(la_kali)
                e = int(input("""
            1 - Add kali linux repositories
            2 - Update
            3 - Remove all kali linux repositories
            4 - View the contents of sources.list file
            => """))
                if e == 1:
                    os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
                    os.system("echo '#Kali repositories | Added by LinstAll' >> /etc/apt/sources.list")
                    os.system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
                elif e == 2:
                    os.system("apt-get update -m")
                elif e == 3:
                    infile = "/etc/apt/sources.list"
                    outfile = "/etc/apt/sources.list"

                    delete_list = ["#Kali repositories | Added by LinstAll",
                                "deb http://http.kali.org/kali kali-rolling main contrib non-free"]
                    fin = open(infile)
                    os.remove("/etc/apt/sources.list")
                    fout = open(outfile, "w+")
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, "")
                        fout.write(line)
                    fin.close()
                    fout.close()
                    print("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
                elif e == 4:
                    file = open('/etc/apt/sources.list', 'r')
                    print(file.read())
            elif d == 2:
                print(la_kali)
                e = int(input("""
            \033[1;36m**************************** All Categories *****************************\033[1;m
            0 - All
            1 - Information Gathering			8 - Exploitation Tools
            2 - Vulnerability Analysis			9 - Forensics Tools
            3 - Wireless Attacks			    10 - Stress Testing
            4 - Web Applications				11 - Password Attacks
            5 - Sniffing & Spoofing				12 - Reverse Engineering
            6 - Maintaining Access				13 - Hardware Hacking
            7 - Reporting Tools 				14 - Extra
            => """))
                if e == 0:
                    os.system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 1:
                    os.system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 2:
                    os.system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
                elif e == 3:
                    os.system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                elif e == 4:
                    os.system("apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
                elif e == 5:
                    os.system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
                elif e == 6:
                    os.system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
                elif e == 7:
                    os.system("apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
                elif e == 8:
                    os.system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
                elif e == 9:
                    os.system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
                elif e == 10:
                    os.system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
                elif e == 11:
                    os.system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
                elif e == 12:
                    os.system("apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
                elif e == 13:
                    os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
                elif e == 14:
                    os.system("apt-get install squid3 && git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
        elif c == "6":
            sys.exit()
        else:
            deb.deb64()


    def deb32(self):
        print(la_d)
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
            program_name = ["uget", "vlc", "qbittorrent", "gimp", "tor", "vivaldi", "libreoffice"]
            for i in program_name:
                if i == "vivaldi":
                    os.system("echo 'deb http://repo.vivaldi.com/stable/deb/ stable main' >> /etc/apt/sources.list.d/vivaldi.list")
                    os.system("apt-get update")
                os.system("apt-get install {}".format(i))
            deb.deb32()
        elif c == "2":
            program_name = ["filezilla", "git", "uget", "vlc", "qbittorrent", "google-chrome", "gimp", "tor",
                            "telegram-desktop", "aegisub", "libreoffice", "chromium", "godot3", "Steam", "Wine", "vivaldi"]
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
                    if i == "vivaldi":
                        os.system("echo 'deb http://repo.vivaldi.com/stable/deb/ stable main' >> /etc/apt/sources.list.d/vivaldi.list")
                        os.system("apt-get update")
                    os.system("apt-get install {}".format(i))
                else:
                    continue
            deb.deb32()
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
            deb.deb32()
        elif c == "4":
            os.system("apt-get install mariadb-server apache2 php libapache2-mod-php php-json php-mbstring php-zip php-gd php-xml php-curl php-mysql")
            os.system("systemctl enable mariadb")
            os.system("systemctl start mariadb")
            os.system("wget https://files.phpmyadmin.net/phpMyAdmin/5.0.1/phpMyAdmin-5.0.1-all-languages.zip")
            os.system("unzip phpMyAdmin-5.0.1-all-languages.zip -d /opt")
            os.system("mv -v /opt/phpMyAdmin-5.0.1-all-languages /opt/phpMyAdmin")
            os.system("chown -Rfv www-data:www-data /opt/phpMyAdmin")
            os.system("mkdir -p /etc/apache2/sites-available/ && cp ./conf/arch/phpmyadmin.conf /etc/apache2/sites-available/")
            os.system("echo 'Listen 8080' >> /etc/apache2/ports.conf")
            os.system("mysql_secure_installation")
            os.system("clear")
            print("Now You Should Follow The steps in \"CreateADatabase.txt\" File")
            print("")
            print("")
            os.system("mysql -u root -p")
            os.system("systemctl enable apache2")
            os.system("systemctl start apache2")
            deb.deb32()
        elif c == "5":
            print(la_kali)
            d = int(input("""
                    1 - Add Kali repositories & Update
                    2 - View Categories
                    => """))
            if d == 1:
                print(la_kali)
                e = int(input("""
                    1 - Add kali linux repositories
                    2 - Update
                    3 - Remove all kali linux repositories
                    4 - View the contents of sources.list file
                    => """))
                if e == 1:
                    os.system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
                    os.system("echo '#Kali repositories | Added by LinstAll' >> /etc/apt/sources.list")
                    os.system(
                        "echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
                elif e == 2:
                    os.system("apt-get update -m")
                elif e == 3:
                    infile = "/etc/apt/sources.list"
                    outfile = "/etc/apt/sources.list"

                    delete_list = ["#Kali repositories | Added by LinstAll",
                                "deb http://http.kali.org/kali kali-rolling main contrib non-free"]
                    fin = open(infile)
                    os.remove("/etc/apt/sources.list")
                    fout = open(outfile, "w+")
                    for line in fin:
                        for word in delete_list:
                            line = line.replace(word, "")
                        fout.write(line)
                    fin.close()
                    fout.close()
                    print("\033[1;31m\nAll kali linux repositories have been deleted !\n\033[1;m")
                elif e == 4:
                    file = open('/etc/apt/sources.list', 'r')
                    print(file.read())
            elif d == 2:
                print(la_kali)
                e = int(input("""
                    \033[1;36m**************************** All Categories *****************************\033[1;m
                    0 - All
                    1 - Information Gathering			8 - Exploitation Tools
                    2 - Vulnerability Analysis			9 - Forensics Tools
                    3 - Wireless Attacks			    10 - Stress Testing
                    4 - Web Applications				11 - Password Attacks
                    5 - Sniffing & Spoofing				12 - Reverse Engineering
                    6 - Maintaining Access				13 - Hardware Hacking
                    7 - Reporting Tools 				14 - Extra
                    => """))
                if e == 0:
                    os.system(
                        "apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 1:
                    os.system(
                        "apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 2:
                    os.system(
                        "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
                elif e == 3:
                    os.system(
                        "apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                elif e == 4:
                    os.system(
                        "apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
                elif e == 5:
                    os.system(
                        "apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
                elif e == 6:
                    os.system(
                        "apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
                elif e == 7:
                    os.system(
                        "apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
                elif e == 8:
                    os.system(
                        "apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
                elif e == 9:
                    os.system(
                        "apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
                elif e == 10:
                    os.system(
                        "apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
                elif e == 11:
                    os.system(
                        "apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
                elif e == 12:
                    os.system(
                        "apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
                elif e == 13:
                    os.system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
                elif e == 14:
                    os.system(
                        "apt-get install squid3 && git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
        elif c == "6":
            sys.exit()
        else:
            deb.deb32()
            
            
            
            
class arch(main):
    def __init__(self):
        os.system("pacman -Sy")
        os.system("pacman -S wget")
        print("")
        print("")
        print(la_d)
        c = input("""
                Choose One of The Option Below:
                1 - Install Recommended Programs
                2 - Custom Install
                3 - Install What You Want
                4 - Install LAMP Stack (MariaDB, PHP)
                5 - ...
                6 - Go Back
                7 - Exit
                ==> """)
        if(c=="1"):
            program_name = ["uget", "celluloid", "qbittorrent", "gimp", "vivaldi", "libreoffice"]
            for i in program_name:
                os.system("pacman -S {}".format(i))
            arch()
        elif(c=="2"):
            program_name = ["filezilla", "git", "uget", "vlc", "qbittorrent", "gimp", "tor",
                                "telegram-desktop", "aegisub", "libreoffice", "chromium", "godot3", "wine", "atom", "vivaldi", 'celluloid', "Steam"]
            for i in program_name:
                b = str(input("Do you wanna install {}?(Y/n) ".format(i)))
                if b == "Y":
                    if i == "Steam":
                        os.system('printf "[multilib]\nInclude = /etc/pacman.d/mirrorlist" >> /etc/pacman.conf')
                        os.system("pacman -Sy")
                        os.system("pacman -S steam")
                        print("")
                        print("")
                        print("Please Reboot Your System")
                        print("")
                        print("")
                        continue
                    os.system("pacman -S {}".format(i))
                else:
                    continue
                arch()
        elif(c=="3"):
            program_name = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                                "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
                                "", "", "", "", ""]
            for i in range(101):
                    b = str(input("Enter Your Program Name(Enter \'Done\' to start installing): "))
                    if b != "Done":
                        program_name[i] = b
                    else:
                        break
            for i in range(101):
                os.system("pacman -S {}".format(program_name[i]))
            arch()
        elif(c=="4"):
            os.system("pacman -S apache mariadb mariadb-clients libmariadbclient php php-apache phpmyadmin")
            os.system("cp ./conf/arch/httpd-mpm.conf ./conf/arch/httpd-default.conf ./conf/arch/httpd-vhosts.conf /etc/httpd/conf/extra/ && cp ./conf/arch/httpd.conf /etc/httpd/conf/")
            os.system("mkdir -p /srv/http/default /srv/http/localhost/public_html /srv/http/localhost/logs")
            os.System("mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql")
            os.System("systemctl start mysqld.service && systemctl enable mysqld.service")
            os.system("mysql_secure_installation")
            os.system("clear")
            print("Now You Should Follow The steps in \"CreateADatabase.txt\" File")
            print("")
            print("")
            os.system("mysql -u root -p")
            os.system("cp ./conf/arch/php.ini /etc/php/")
            os.System("mkdir /var/log/php && mkdir /var/log/php")
            os.System("cp ./conf/arch/phpmyadmin.conf /etc/httpd/conf/extra/")
            os.System("mkdir -p /etc/webapps/phpmyadmin/ && touch /etc/webapps/phpmyadmin/config.inc.php && echo '$cfg['blowfish_secret'] = 'askdjfyasdosadyasduahew97ftyaielrwuera980ghfireugsh8d7ofgydsf8i7gsasdfo7ydsfigh';' >> /etc/webapps/phpmyadmin/config.inc.php")
            os.System("mkdir -p /usr/share/webapps/phpMyAdmin/tmp/ && chown http /usr/share/webapps/phpMyAdmin/tmp/ && chmod 766 /usr/share/webapps/phpMyAdmin/tmp/")
            os.System("systemctl enable httpd.service && systemctl start httpd.service")
            print("")
            print("")
            print("")
            print("Now you can access your:\nWebSite From http://localhost\nPHPMyAdmin Panel From http://localhost:8080")
            arch()
        elif(c=="5"):
            print("...")
        elif(c=="6"):
            main()
        elif(c=="7"):
            sys.exit()
        else:
            arch()




if os.getuid() != 0:
    print("""
        This Script Requires Root Privilege,
        Pleas Run It With \"sudo\" or Change To Root User With Command \"su\" or \"sudo su\"""")
    sys.exit()
else:
    main()
