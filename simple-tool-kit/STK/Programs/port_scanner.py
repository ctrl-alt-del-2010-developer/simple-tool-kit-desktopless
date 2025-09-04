import sys
import socket
import threading
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QListWidget, QLabel
)

class PortScannerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Port Scanner")
        self.setGeometry(300, 300, 400, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label = QLabel("Enter IP Address or Domain:")
        layout.addWidget(self.label)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("e.g. 192.168.1.1 or example.com")
        layout.addWidget(self.input_field)

        self.scan_button = QPushButton("Start Scan")
        self.scan_button.clicked.connect(self.start_scan)
        layout.addWidget(self.scan_button)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        self.setLayout(layout)

    def start_scan(self):
        user_input = self.input_field.text().strip()
        if not user_input:
            self.result_list.addItem("Please enter a valid IP or domain.")
            return

        self.result_list.clear()
        self.result_list.addItem(f"Resolving '{user_input}'...")

        # Start thread to prevent GUI from freezing
        scan_thread = threading.Thread(target=self.resolve_and_scan, args=(user_input,))
        scan_thread.start()

    def resolve_and_scan(self, user_input):
        try:
            ip = socket.gethostbyname(user_input)
            self.result_list.addItem(f"Resolved to IP: {ip}")
            self.scan_ports(ip)
        except socket.gaierror:
            self.result_list.addItem(f"Error: Could not resolve '{user_input}'.")

    def scan_ports(self, ip):
        open_ports = []
        for port in range(1, 1025):
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                    sock.settimeout(0.5)
                    result = sock.connect_ex((ip, port))
                    if result == 0:
                        open_ports.append(port)
                        self.result_list.addItem(f"Port {port} is open.")
            except socket.error:
                self.result_list.addItem(f"Error: Could not connect to {ip}.")
                return

        if not open_ports:
            self.result_list.addItem("No open ports found.")
        else:
            self.result_list.addItem("Scan complete.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PortScannerApp()
    window.show()
    sys.exit(app.exec_())
