#!/usr/bin/env python3
from os import system, getuid
from sys import exit, argv
from subprocess import run, PIPE
import toml


cpright = "\033[31m _     _           _      _    _ _ \n| |   (_)_ __  ___| |_   / \  | | |\n| |   | | '_ \/ __| __| / _ \ | | |\n| |___| | | | \__ \ |_ / ___ \| | |\n|_____|_|_| |_|___/\__/_/   \_\_|_| V1.0\033[m\n\n\033[36mA Tool For Installing Any Programs Easily\n   Coding By M.J. Bagheri Nejad(MJBN)\n\t  WebSite: MJBN.IR\033[m"
warning="\n\tBefore updating your system , please remove all\n\t\tKali-linux repositories to avoid any kind of problem.\033[m"
class main:
    def __init__(self):
        print(cpright)
        self.path = int(input("Choose One of The Option Below:\n1 - Install Recommended Programs\n2 - Install What You Want\n3 - Install LAMP Stack (MariaDB, PHP)\n4 - Installing Kali Programs\n5 - Exit\n==> "))
        
        # Exit if the path equals 5
        if (self.path == 5): exit();

        # Recommended Programs
        self.program_name = ["uget", "vlc", "gimp", "firefox", "libreoffice"]

        #PKG Managers
        pkg = run(['ls', '/bin/apt', '/bin/pacman', '/bin/dnf'], stdout=PIPE).stdout.decode("UTF-8")
        if pkg.find('apt') != -1:
            system("apt-get update")
            system("apt-get install wget")
            architecture = run(['uname', '-m'], stdout=PIPE).stdout.decode("UTF-8")
            if architecture.find('x86_64') != -1:
                self.deb64()
            elif architecture.find('i686') != -1:
                self.deb32()
            else:
                print("There is no support for ", architecture, ", at the moment.")
                exit()
        elif pkg.find('pacman') != -1:
            system("pacman -Sy")
            system("pacman -S wget")
            self.arch()
        elif pkg.find('dnf') != -1:
            print("\033[36mComing Soon...\033[m")
            exit()
        else:
            print("\033[36mI don't have any plan for any other Package Management (Distro) now, But maybe in the future, I do something, Who knows\033[m ")
            exit()
            
    def deb64(self):
        if (self.path == 1):
            for i in self.program_name:
                system("apt-get install {}".format(i))
            main()
        elif (self.path == 2):
            program_name = []
            for i in range(101):
                b = str(input("Enter Your Program Name(Enter \'exit\' to start installing): "))
                if b != "exit":
                    program_name.append(b)
                else:
                    break
            for i in range(101):
                system("apt-get install {}".format(program_name[i]))
            main()
        elif (self.path == 3):
            system("apt-get install mariadb-server apache2 php libapache2-mod-php php-json php-mbstring php-zip php-gd php-xml php-curl php-mysql")
            system("systemctl enable mariadb")
            system("systemctl start mariadb")
            system("wget https://files.phpmyadmin.net/phpMyAdmin/5.0.1/phpMyAdmin-5.0.1-all-languages.zip")
            system("unzip phpMyAdmin-5.0.1-all-languages.zip -d /opt")
            system("mv -v /opt/phpMyAdmin-5.0.1-all-languages /opt/phpMyAdmin")
            system("chown -Rfv www-data:www-data /opt/phpMyAdmin")
            system("mkdir -p /etc/apache2/sites-available/ && cp ./conf/arch/phpmyadmin.conf /etc/apache2/sites-available/")
            system("echo 'Listen 8080' >> /etc/apache2/ports.conf")
            system("mysql_secure_installation")
            system("clear")
            print("Now You Should Follow The steps in \"CreateADatabase.txt\" File")
            print("")
            print("")
            system("mysql -u root -p")
            system("systemctl enable apache2")
            system("systemctl start apache2")
            main()
        elif (self.path == 4):
            print(cpright)
            print(warning)
            d = int(input("""
            1 - Add Kali repositories & Update
            2 - View Categories
            => """))
            if d == 1:
                print(warning)
                e = int(input("""
            1 - Add kali linux repositories
            2 - Update
            3 - Remove all kali linux repositories
            4 - View the contents of sources.list file
            => """))
                if e == 1:
                    system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
                    system("echo '#Kali repositories | Added by LinstAll' >> /etc/apt/sources.list")
                    system("echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
                elif e == 2:
                    system("apt-get update -m")
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
                print(warning)
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
                    system("apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 1:
                    system("apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 2:
                    system("apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
                elif e == 3:
                    system("apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                elif e == 4:
                    system("apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
                elif e == 5:
                    system("apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
                elif e == 6:
                    system("apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
                elif e == 7:
                    system("apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
                elif e == 8:
                    system("apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
                elif e == 9:
                    system("apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
                elif e == 10:
                    system("apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
                elif e == 11:
                    system("apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
                elif e == 12:
                    system("apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
                elif e == 13:
                    system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
                elif e == 14:
                    system("apt-get install squid3 && git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
        else:
            main()


    def deb32(self):
        if (self.path == 1):
            for i in self.program_name:
                if i == "vivaldi":
                    system("echo 'deb http://repo.vivaldi.com/stable/deb/ stable main' >> /etc/apt/sources.list.d/vivaldi.list")
                    system("apt-get update")
                system("apt-get install {}".format(i))
            main()
        elif (self.path == 2):
            program_name = []
            for i in range(101):
                b = str(input("Enter Your Program Name(Enter \'exit\' to start installing): "))
                if b != "exit":
                    program_name.append(b)
                else:
                    break
            for i in range(101):
                system("apt-get install {}".format(program_name[i]))
            main()
        elif (self.path == 3):
            system("apt-get install mariadb-server apache2 php libapache2-mod-php php-json php-mbstring php-zip php-gd php-xml php-curl php-mysql")
            system("systemctl enable mariadb")
            system("systemctl start mariadb")
            system("wget https://files.phpmyadmin.net/phpMyAdmin/5.0.1/phpMyAdmin-5.0.1-all-languages.zip")
            system("unzip phpMyAdmin-5.0.1-all-languages.zip -d /opt")
            system("mv -v /opt/phpMyAdmin-5.0.1-all-languages /opt/phpMyAdmin")
            system("chown -Rfv www-data:www-data /opt/phpMyAdmin")
            system("mkdir -p /etc/apache2/sites-available/ && cp ./conf/arch/phpmyadmin.conf /etc/apache2/sites-available/")
            system("echo 'Listen 8080' >> /etc/apache2/ports.conf")
            system("mysql_secure_installation")
            system("clear")
            print("Now You Should Follow The steps in \"CreateADatabase.txt\" File")
            print("")
            print("")
            system("mysql -u root -p")
            system("systemctl enable apache2")
            system("systemctl start apache2")
            main()
        elif (self.path == 4):
            print(warning)
            d = int(input("""
                    1 - Add Kali repositories & Update
                    2 - View Categories
                    => """))
            if d == 1:
                print(warning)
                e = int(input("""
                    1 - Add kali linux repositories
                    2 - Update
                    3 - Remove all kali linux repositories
                    4 - View the contents of sources.list file
                    => """))
                if e == 1:
                    system("apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6")
                    system("echo '#Kali repositories | Added by LinstAll' >> /etc/apt/sources.list")
                    system(
                        "echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list")
                elif e == 2:
                    system("apt-get update -m")
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
                print(warning)
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
                    system(
                        "apt-get -f install acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy apktool dex2jar python-distorm3 edb-debugger jad javasnoop jd ollydbg smali valgrind yara android-sdk apktool arduino dex2jar sakis3g smali && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 1:
                    system(
                        "apt-get install -y acccheck ace-voip amap automater braa casefile cdpsnarf cisco-torch cookie-cadger copy-router-config dmitry dnmap dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter ghost-phisher golismero goofile lbd maltego-teeth masscan metagoofil miranda nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslcaudit sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled twofi urlcrazy wireshark wol-e xplico ismtp intrace hping3 && wget http://www.morningstarsecurity.com/downloads/bing-ip2hosts-0.4.tar.gz && tar -xzvf bing-ip2hosts-0.4.tar.gz && cp bing-ip2hosts-0.4/bing-ip2hosts /usr/local/bin/")
                elif e == 2:
                    system(
                        "apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant hexorbase jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner powerfuzzer sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia")
                elif e == 3:
                    system(
                        "apt-get install -y aircrack-ng asleap bluelog blueranger bluesnarfer bully cowpatty crackle eapmd5pass fern-wifi-cracker ghost-phisher giskismet gqrx kalibrate-rtl killerbee kismet mdk3 mfcuk mfoc mfterm multimon-ng pixiewps reaver redfang spooftooph wifi-honey wifitap wifite")
                elif e == 4:
                    system(
                        "apt-get install -y apache-users arachni bbqsql blindelephant burpsuite cutycapt davtest deblaze dirb dirbuster fimap funkload grabber jboss-autopwn joomscan jsql maltego-teeth padbuster paros parsero plecost powerfuzzer proxystrike recon-ng skipfish sqlmap sqlninja sqlsus ua-tester uniscan vega w3af webscarab websploit wfuzz wpscan xsser zaproxy")
                elif e == 5:
                    system(
                        "apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey wireshark xspy yersinia zaproxy")
                elif e == 6:
                    system(
                        "apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely")
                elif e == 7:
                    system(
                        "apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal")
                elif e == 8:
                    system(
                        "apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester maltego-teeth set shellnoob sqlmap thc-ipv6 yersinia beef-xss")
                elif e == 9:
                    system(
                        "apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico")
                elif e == 10:
                    system(
                        "apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos")
                elif e == 11:
                    system(
                        "apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier hexorbase john johnny keimpx maltego-teeth maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy")
                elif e == 12:
                    system(
                        "apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA")
                elif e == 13:
                    system("apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali")
                elif e == 14:
                    system(
                        "apt-get install squid3 && git clone https://github.com/LionSec/wifresti.git && cp wifresti/wifresti.py /usr/bin/wifresti && chmod +x /usr/bin/wifresti && wifresti")
        else:
            self.deb32()

    def arch(self):
        if (self.path == 1):
            for i in self.program_name:
                system("pacman -S {}".format(i))
            main()
        elif (self.path == 2):
            program_name = []
            for i in range(101):
                b = str(input("Enter Your Program Name(Enter \'exit\' to start installing): "))
                if b != "exit":
                    program_name.append(b)
                else:
                    break
            for i in range(101):
                system("pacman -S {}".format(program_name[i]))
            main()
        elif (self.path == 3):
            system("pacman -S apache mariadb mariadb-clients libmariadbclient php php-apache phpmyadmin")
            system("cp ./conf/arch/httpd-mpm.conf ./conf/arch/httpd-default.conf ./conf/arch/httpd-vhosts.conf /etc/httpd/conf/extra/ && cp ./conf/arch/httpd.conf /etc/httpd/conf/")
            system("mkdir -p /srv/http/default /srv/http/localhost/public_html /srv/http/localhost/logs")
            system("mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql")
            system("systemctl start mysqld.service && systemctl enable mysqld.service")
            system("mysql_secure_installation")
            system("clear")
            print("Now You Should Follow The steps in \"CreateADatabase.txt\" File")
            system("mysql -u root -p")
            system("cp ./conf/arch/php.ini /etc/php/")
            system("mkdir /var/log/php && mkdir /var/log/php")
            system("cp ./conf/arch/phpmyadmin.conf /etc/httpd/conf/extra/")
            system("mkdir -p /etc/webapps/phpmyadmin/ && touch /etc/webapps/phpmyadmin/config.inc.php && echo '$cfg['blowfish_secret'] = 'askdjfyasdosadyasduahew97ftyaielrwuera980ghfireugsh8d7ofgydsf8i7gsasdfo7ydsfigh';' >> /etc/webapps/phpmyadmin/config.inc.php")
            system("mkdir -p /usr/share/webapps/phpMyAdmin/tmp/ && chown http /usr/share/webapps/phpMyAdmin/tmp/ && chmod 766 /usr/share/webapps/phpMyAdmin/tmp/")
            system("systemctl enable httpd.service && systemctl start httpd.service")
            print("Now you can access your:\nWebSite From http://localhost\nPHPMyAdmin Panel From http://localhost:3036")
            main()
        elif (self.path == 4):
            print("...")
        else:
            main()


if __name__ == "__main__":
    if getuid() != 0:
        print("""This Script Requires Root Privilege, Pleas Run It With \"sudo\" or Change To Root User With Command \"su\" or \"sudo su\"""")
        exit()
    else:
        main()
