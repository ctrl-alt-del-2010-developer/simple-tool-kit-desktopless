#!/bin/bash                                         
#Please only fork if you want to improve my project.

RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
RESET='\e[0m'

while true; do
    clear
    cat ascii.txt  #Show The Ascii
    echo -e "${RED}[${YELLOW}01${RED}]${RESET} Red Hawk      ${RED}[${YELLOW}07${RED}]${RESET} Ping Test"
    echo -e "${RED}[${YELLOW}02${RED}]${RESET} Tor IP        ${RED}[${YELLOW}08${RED}]${RESET} Tor Browser"
    echo -e "${RED}[${YELLOW}03${RED}]${RESET} Network Scan  ${RED}[${YELLOW}09${RED}]${RESET} Port Scanner"
    echo -e "${RED}[${YELLOW}04${RED}]${RESET} DDoS Tool     ${RED}[${YELLOW}10${RED}]${RESET} Sqlmap"   #Show The Menu
    echo -e "${RED}[${YELLOW}05${RED}]${RESET} Cmatrix       ${RED}[${YELLOW}11${RED}]${RESET} Wireshark(Lite)"
    echo -e "${RED}[${YELLOW}06${RED}]${RESET} İwctl Shell   ${RED}[${YELLOW}12${RED}]${RESET} Htop"
    echo ""
    echo -e "${RED}[${YELLOW}99${RED}]${RESET} About         ${RED}[${YELLOW}00${RED}]${RESET} Exit"          
    echo ""
    echo -e "${YELLOW}Tip:${RESET} Please Do Not Run Simple Tool Kit As Sudo Permissions." #Show The Tip
    echo ""
    read -p "> " opition

    case "$opition" in
        1)
            clear
            python3 ~/simple-tool-kit-desktopless/STK/Programs/red_hawk.py
            clear
            read -p "Press Enter Button For Continue..."
            ;;
        2)
            clear
            sudo systemctl start tor
            python3 ~/simple-tool-kit-desktopless/STK/Programs/ip_changer.py
            clear
            read -p "Press Enter Button For Continue..."
            ;;
        3)  
            clear
            wifi_ifaces=$(iw dev | awk '/Interface/ {print $2}')
            sudo airodump-ng $wifi_ifaces
            read -p "Press Enter Button For Continue..."
            ;;
        4)  
            clear
            python3 ~/simple-tool-kit-desktopless/STK/Programs/DDoS-tool.py
            clear
            read -p "Press Enter Button For Continue..."
            ;;
        5)  
            clear
            cmatrix
            clear
            read -p "Press Enter Button For Continue..."
            ;;
        6)  
            clear
            sudo systemctl start iwd 
            iwctl
            read -p "Press Enter Button For Continue..."
            ;;
        7)  
            clear
            ping 1.1.1.1 
            read -p "Press Enter Button For Continue..."
            ;;
        8)  
            clear
            torbrowser-launcher
            read -p "Press Enter Button For Continue..."
            ;;
        9)  
            clear
            python3 ~/simple-tool-kit/STK-desktopless/Programs/port_scanner.py
            read -p "Press Enter Button For Continue..."
            ;;
        10)  
            clear
            sqlmap --wizard
            read -p "Press Enter Button For Continue..."
            ;;
        11)  
            clear
            sudo horst $wifi_iface
            clear
            read -p "Press Enter Button For Continue..."
            ;;
        12)  
            clear
            htop
            read -p "Press Enter Button For Continue..."
            ;;
        99)  
            clear
            cat ~/simple-tool-kit-desktopless/STK/Programs/about.txt
            read -p "Press Enter Button For Continue..."
            ;;
         0)  
            echo -e "${RED}Exiting...${RESET}"
            exit 0
            ;;
        *)
            clear
            echo "Invalid Selection!"
            read -p "Press Enter Button For Contiune..."
            ;;
    esac
done
