RED='\e[31m'
GREEN='\e[32m'
YELLOW='\e[33m'
RESET='\e[0m'

detect_pkg_manager() {
    OS=$(uname)
    if [ "$OS" = "Darwin" ]; then
        PKG_MANAGER="brew"
        INSTALL_CMD="brew install"
        PY2="python@2"
        PY3="python@3"
        PIP="pip3"
    elif [ -f /etc/os-release ]; then
        . /etc/os-release
        case "$ID" in
            ubuntu|debian|linuxmint|pop|elementary|zorin)
                PKG_MANAGER="apt"
                INSTALL_CMD="sudo apt install -y"
                PY2="python2"
                PY3="python3"
                PIP="python3-pip"
            ;;
            kali)
                PKG_MANAGER="apt"
                INSTALL_CMD="sudo apt install -y"
                PY2="python2"
                PY3="python3"
                PIP="python3-pip"
            ;;
            fedora)
                PKG_MANAGER="dnf"
                INSTALL_CMD="sudo dnf install -y"
                PY2="python2"
                PY3="python3"
                PIP="python3-pip"
            ;;
            rhel|almalinux|rocky|centos)
                PKG_MANAGER="yum"
                INSTALL_CMD="sudo yum install -y"
                PY2="python2"
                PY3="python3"
                PIP="python3-pip"
            ;;
            arch)
                PKG_MANAGER="pacman"
                INSTALL_CMD="sudo pacman -S --noconfirm"
                PY2="python2"
                PY3="python"
                PIP="python-pip"
            ;;
            manjaro)
                PKG_MANAGER="pacman"
                INSTALL_CMD="sudo pacman -S --noconfirm"
                PY2="python2"
                PY3="python"
                PIP="python-pip"
            ;;
            opensuse*|suse)
                PKG_MANAGER="zypper"
                INSTALL_CMD="sudo zypper install -y"
                PY2="python2"
                PY3="python3"
                PIP="python3-pip"
            ;;
            solus)
                PKG_MANAGER="eopkg"
                INSTALL_CMD="sudo eopkg install -y"
                PY2="python2"
                PY3="python3"
                PIP="python3-pip"
            ;;
            void)
                PKG_MANAGER="xbps"
                INSTALL_CMD="sudo xbps-install -Sy"
                PY2="python2"
                PY3="python3"
                PIP="python3-pip"
            ;;
            gentoo)
                PKG_MANAGER="emerge"
                INSTALL_CMD="sudo emerge"
                PY2="dev-lang/python:2.7"
                PY3="dev-lang/python"
                PIP="dev-python/pip"
            ;;
            clearlinux)
                PKG_MANAGER="swupd"
                INSTALL_CMD="sudo swupd bundle-add"
                PY2="python2-basic"
                PY3="python3-basic"
                PIP="python3-pip"
            ;;
            *)
                PKG_MANAGER="unknown"
            ;;
        esac
    else
        PKG_MANAGER="unknown"
    fi
}

clear
clear

detect_pkg_manager

if [ "$PKG_MANAGER" = "unknown" ]; then
    echo -e "${RED}Unsupported or unknown operating system!${RESET}"
    exit 1
fi

echo -e "${YELLOW}Detected package manager: $PKG_MANAGER${RESET}"

PACKAGES="$PY2 $PY3 $PIP cmatrix aircrack-ng iwd torbrowser-launcher sqlmap wireshark htop"

# Check if the package manager is installed
if ! command -v $PKG_MANAGER >/dev/null 2>&1; then
    echo -e "${RED}$PKG_MANAGER is not installed or not in your PATH. Please install it and retry.${RESET}"
    exit 2
fi

# Install packages
$INSTALL_CMD $PACKAGES

# Install Python requirements
if command -v pip3 >/dev/null 2>&1; then
    pip3 install -r requirements.txt --break-system-packages
elif command -v pip >/dev/null 2>&1; then
    pip install -r requirements.txt --break-system-packages
else
    echo -e "${RED}pip is not installed! Please install pip manually.${RESET}"
fi

clear
echo -e "${GREEN}Installation completed. Enter the command 'bash run.sh' in the Command Prompt to start the program.${RESET}"

sleep 5
