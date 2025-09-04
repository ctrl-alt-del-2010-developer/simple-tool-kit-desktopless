import socket
import requests
import whois
import ssl
import sys
import time
import os

RED = "\033[31m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def vip(yazi, bekleme=0.01, end="\n"):
    for harf in yazi:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
    sys.stdout.write(end)  # print() yerine end parametresini kullandırıyoruz

ascii="""
 ██▀███  ▓█████ ▓█████▄     ██░ ██  ▄▄▄       █     █░██ ▄█▀
▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌   ▓██░ ██▒▒████▄    ▓█░ █ ░█░██▄█▒ 
▓██ ░▄█ ▒▒███   ░██   █▌   ▒██▀▀██░▒██  ▀█▄  ▒█░ █ ░█▓███▄░ 
▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌   ░▓█ ░██ ░██▄▄▄▄██ ░█░ █ ░█▓██ █▄ 
░██▓ ▒██▒░▒████▒░▒████▓    ░▓█▒░██▓ ▓█   ▓██▒░░██▒██▓▒██▒ █▄
░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▓░▒ ▒ ▒ ▒▒ ▓▒
  ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒     ▒ ░▒░ ░  ▒   ▒▒ ░  ▒ ░ ░ ░ ░▒ ▒░
  ░░   ░    ░    ░ ░  ░     ░  ░░ ░  ░   ▒     ░   ░ ░ ░░ ░ 
   ░        ░  ░   ░        ░  ░  ░      ░  ░    ░   ░  ░   
                 ░                                          

"""

def get_domain(url):
    return url.replace("http://", "").replace("https://", "").split('/')[0]

def get_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        vip(f"IP Address: {ip}")
    except Exception as e:
        vip(f"Error: {e}")

def whois_info(domain):
    try:
        w = whois.whois(domain)
        vip("WHOIS Info:")
        vip(w)
    except Exception as e:
        vip(f"Error fetching WHOIS info: {e}")

def http_headers(url):
    try:
        r = requests.get(url)
        vip("HTTP Headers:")
        for k, v in r.headers.items():
            vip(f"{k}: {v}")
    except Exception as e:
        vip(f"Error fetching headers: {e}")

def port_scan(domain):
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 8080, 8443, 3306, 3389, 5432, 6379, 8000, 8888]
    vip("Port Scan Results:")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.8)
            conn = sock.connect_ex((domain, port))
            if conn == 0:
                vip(f"Port {port}: Open")
            sock.close()
        except Exception as e:
            vip(f"Port {port}: Error ({e})")

def reverse_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        rev = socket.gethostbyaddr(ip)
        vip(f"Reverse DNS: {rev[0]}")
    except Exception as e:
        vip(f"Error: {e}")

def show_robots_txt(url):
    try:
        robots_url = url.rstrip('/') + '/robots.txt'
        r = requests.get(robots_url)
        vip("robots.txt:")
        vip(r.text)
    except Exception as e:
        vip(f"Error fetching robots.txt: {e}")

def ssl_info(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                vip("SSL Certificate Info:")
                for k, v in cert.items():
                    vip(f"{k}: {v}")
    except Exception as e:
        vip(f"Error fetching SSL info: {e}")

def traceroute(domain):
    try:
        import platform
        import subprocess
        vip("Traceroute:")
        if platform.systehm().lower() == "windows":
            cmd = ["tracert", domain]
        else:
            cmd = ["traceroute", domain]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in proc.stdout:
            vip(line, end="")
    except Exception as e:
        vip(f"Error: {e}")

def dns_info(domain):
    try:
        import dns.resolver
        vip("A records:")
        for rdata in dns.resolver.resolve(domain, 'A'):
            vip(f"  {rdata}")
        vip("AAAA records:")
        for rdata in dns.resolver.resolve(domain, 'AAAA'):
            vip(f"  {rdata}")
        vip("MX records:")
        for rdata in dns.resolver.resolve(domain, 'MX'):
            vip(f"  {rdata}")
        vip("NS records:")
        for rdata in dns.resolver.resolve(domain, 'NS'):
            vip(f"  {rdata}")
        vip("TXT records:")
        for rdata in dns.resolver.resolve(domain, 'TXT'):
            vip(f"  {rdata}")
    except Exception as e:
        vip(f"Error fetching DNS info: {e}")

def http_body(url):
    try:
        r = requests.get(url)
        vip("HTTP Response Body (first 2000 characters):")
        vip(r.text[:2000])
    except Exception as e:
        vip(f"Error fetching HTTP body: {e}")

def subdomain_brute(domain):
    subdomains = ["www", "mail", "ftp", "test", "dev", "webmail", "ns1", "ns2", "blog", "m", "cpanel", "shop", "api", "staging", "app"]
    vip("Subdomain brute force (common ones):")
    for sub in subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            vip(f"Found: {subdomain}")
        except:
            pass

def hsts_check(url):
    try:
        r = requests.get(url)
        hsts = r.headers.get("Strict-Transport-Security")
        if hsts:
            vip("HSTS Policy:", hsts)
        else:
            vip("No HSTS Policy detected.")
    except Exception as e:
        vip(f"Error fetching HSTS policy: {e}")

def http_methods(domain):
    try:
        url = "http://" + domain
        r = requests.options(url)
        vip("Allowed HTTP Methods:", r.headers.get('allow', r.headers.get('Allow')))
    except Exception as e:
        vip(f"Error fetching HTTP methods: {e}")

def csp_check(url):
    try:
        r = requests.get(url)
        csp = r.headers.get("Content-Security-Policy")
        if csp:
            vip("CSP Header:", csp)
        else:
            vip("No CSP header.")
    except Exception as e:
        vip(f"Error fetching CSP header: {e}")

def main():
    os.system("clear")
    vip("-" * 50)
    vip("RED_HAWK - Super Interactive Recon and Information Gathering Tool")
    vip("-" * 50)
    os.system("clear")
    url = input("Enter target site (https://...): ").strip()
    domain = get_domain(url)
    while True:
        os.system("clear")
        print(f"{RED}{ascii}{RESET}")
        vip("--------------------------------------------")
        vip(f"{RED}[{YELLOW}01{RED}]{RESET} WHOIS Info")
        vip(f"{RED}[{YELLOW}02{RED}]{RESET} HTTP Headers")
        vip(f"{RED}[{YELLOW}03{RED}]{RESET} Port Scan")
        vip(f"{RED}[{YELLOW}04{RED}]{RESET} Reverse DNS")
        vip(f"{RED}[{YELLOW}05{RED}]{RESET} Show IP Address")
        vip(f"{RED}[{YELLOW}06{RED}]{RESET} Show robots.txt")
        vip(f"{RED}[{YELLOW}07{RED}]{RESET} SSL Certificate Info")
        vip(f"{RED}[{YELLOW}08{RED}]{RESET} Traceroute")
        vip(f"{RED}[{YELLOW}09{RED}]{RESET} DNS Records")
        vip(f"{RED}[{YELLOW}10{RED}]{RESET} HTTP Body (first 2000 characters)")
        vip(f"{RED}[{YELLOW}11{RED}]{RESET} Subdomain Brute Force")
        vip(f"{RED}[{YELLOW}12{RED}]{RESET} HSTS Policy Check")
        vip(f"{RED}[{YELLOW}13{RED}]{RESET} HTTP Methods Test")
        vip(f"{RED}[{YELLOW}14{RED}]{RESET} CSP Header Check")
        vip(f"{RED}[{YELLOW}00{RED}]{RESET} Exit")
        vip("---------------------------------------------")
        print("")
        choice = input("Enter action number: ").strip()
        print("")
        if choice == "1":
            whois_info(domain)
        elif choice == "2":
            http_headers(url)
        elif choice == "3":
            port_scan(domain)
        elif choice == "4":
            reverse_dns(domain)
        elif choice == "5":
            get_ip(domain)
        elif choice == "6":
            show_robots_txt(url)
        elif choice == "7":
            ssl_info(domain)
        elif choice == "8":
            traceroute(domain)
        elif choice == "9":
            dns_info(domain)
        elif choice == "10":
            http_body(url)
        elif choice == "11":
            subdomain_brute(domain)
        elif choice == "12":
            hsts_check(url)
        elif choice == "13":
            http_methods(domain)
        elif choice == "14":
            csp_check(url)
        elif choice == "0":
            vip("Exiting...")
            break
        else:
            vip("Invalid choice.")
        vip("-" * 50)
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        vip("\nExiting...")
        sys.exit(0)
