import sys
import socket
import time
import os

ascii="""
 ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███  
▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒
▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░ 
             ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░     
                                                ░                                                       
"""
os.system("clear")
print(ascii)

def vip(yazi, bekleme=0.01, end="\n"):
    for harf in yazi:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    sys.stdout.write(end)  # print() yerine end parametresini kullandırıyoruz


def resolve_host(user_input):
    try:
        ip = socket.gethostbyname(user_input)
        vip(f"Resolved '{user_input}' to IP: {ip}")
        return ip
    except socket.gaierror:
        vip(f"Error: Could not resolve '{user_input}'.")
        return None

def scan_ports(ip):
    open_ports = []
    vip(f"Scanning ports on {ip} (1-1024)...")
    for port in range(1, 1025):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
                    vip(f"Port {port} is open.")
        except socket.error:
            vip(f"Error: Could not connect to {ip}.")
            return

    if not open_ports:
        vip("No open ports found.")
    else:
        vip("Scan complete.")

def main():
    if len(sys.argv) < 2:
        user_input = input("Enter IP Address or Domain: ").strip()
    else:
        user_input = sys.argv[1].strip()

    if not user_input:
        vip("Please enter a valid IP or domain.")
        return
    ip = resolve_host(user_input)
    if ip:
        scan_ports(ip)

if __name__ == "__main__":
    main()
