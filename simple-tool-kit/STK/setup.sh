
RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
RESET='\e[0m'

clear 
clear
sudo apt install python2 python3 pip cmatrix aircrack-ng iwd torbrowser-launcher sqlmap wireshark htop
pip3 install -r requirements.txt --break-system-packages
clear
echo -e "${GREEN}Installation completed. Enter the command 'bash run.sh' in the Command Prompt to start the program.${RESET}"

sleep 5
