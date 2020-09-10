import speedtest
from colorama import Fore, Back, Style, init
import time

# initialize colorama

init()

GREEN = Fore.GREEN
RED = Fore.RED
BLUE = Fore.BLUE
YELLOW = Fore.YELLOW
BLACK = Fore.BLACK
WHITE = Fore.WHITE
RESET = Style.RESET_ALL
MAGENTA = Fore.MAGENTA
CYAN = Fore.CYAN

##print(Fore.YELLOW, pyfiglet.figlet_format("FiberIL"), Style.RESET_ALL)
print(f"{GREEN}----------------------------------------------------------------------{RESET}")
print("")
print(f"{YELLOW}FiberIL Community SpeedTest Tool!{RESET}")
print("")
print(f"{RED}Schedule Tests Available :{GREEN} 2,4,6,8 Times a Day!{RESET}")
print(f"{RED}SpeedTest Report For Schedule Tests is : {GREEN}SpeedTest.txt{RESET}")
print("")
print(f"{YELLOW}                                                  Created By Dolev K.{RESET}")
print(f"{GREEN}----------------------------------------------------------------------{RESET}")


def looptest(x, x2):
    print(f"{YELLOW}Please Wait SpeedTest Is Running!")
    while True:
        def test():
            global s
            try:
                s = speedtest.Speedtest()
                s.get_best_server()
                s.download()
                s.upload()
            except:
                pass

        test()

        def results():
            with open("Speedtest.txt", "a") as f:
                try:
                    seconds = time.time()
                    local_time = time.ctime(seconds)
                    res = s.results.dict()
                    servername = res['server']
                    name = (servername.get("sponsor"))
                    upload = (int(res["upload"]))
                    upload2 = upload / 1000000
                    download = (int(res["download"]))
                    download2 = download / 1000000
                    ping = (int(res["ping"]))
                    print("")
                    print(
                        f"{GREEN}DownloadSpeed: {RED}{download2:.2f} Mbps \n{GREEN}UploadSpeed: {RED}{upload2:.2f} Mbps \n{GREEN}Ping:{RED} {ping} ms \n{GREEN}ServerName:{RED} {name}{RESET}")
                    head = f"Schedule Test Date: {local_time}"
                    r = f"DownloadSpeed: {download2:.2f} Mbps \nUploadSpeed: {upload2:.2f} Mbps \nPing: {ping} ms \nServerName: {name}"
                    f.write("\n")
                    f.write(head)
                    f.write("\n")
                    f.write(r)
                    f.write("\n")
                except:
                    pass
        results()
        print(x2)
        print(f"{YELLOW}SpeedTest Report is: Speedtest.txt")
        time.sleep(x)


def onetimetest():
    print(f"{YELLOW}Please Wait SpeedTest Is Running!")

    def test():
        global s
        try:
            s = speedtest.Speedtest()
            s.get_best_server()
            s.download()
            s.upload()
        except:
            pass

    test()

    def results():
        try:
            res = s.results.dict()
            servername = res['server']
            name = (servername.get("sponsor"))
            upload = (int(res["upload"]))
            upload2 = upload / 1000000
            download = (int(res["download"]))
            download2 = download / 1000000
            ping = (int(res["ping"]))
            print("")
            print(
                f"{GREEN}DownloadSpeed: {RED}{download2:.2f} Mbps \n{GREEN}UploadSpeed: {RED}{upload2:.2f} Mbps \n{GREEN}Ping: {RED}{ping} ms \n{GREEN}ServerName:{RED} {name}")
        except:
            pass
    results()


while True:
    print(f"{GREEN}")
    t = input(f"Do you want to Perform One Time Scan? [y/n]\n")
    if "y" in t:
        onetimetest()
    if "n" in t:
        tt = input(f"How many time a Day you want to Scan ? [2,4,6,8]\n")
        if "2" in tt:
            x = 43200
            x2 = f"{GREEN}12 Hours Till next Scan"
            looptest(x, x2)
        if "4" in tt:
            x = 21600
            x2 = f"{GREEN}6 Hours Till next Scan"
            looptest(x, x2)
        if "6" in tt:
            x = 14400
            x2 = f"{GREEN}4 Hours Till next Scan"
            looptest(x, x2)
        if "8" in tt:
            x = 10800
            x2 = f"{GREEN}3 Hours Till next Scan"
            looptest(x, x2)
        else:
            print(f"{RED}Wrong Input Try Again!")