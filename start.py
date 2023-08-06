import sys, os, platform, winreg
from Observer import run
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget


def add_to_startup() -> None:
    script_path = os.path.abspath(__file__)

    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_READ,
    )

    try:
        existing_value, _ = winreg.QueryValueEx(key, "Observe")
        if existing_value == script_path:
            print("Script is already in the startup applications.")
            return
    except WindowsError:
        pass

    n_key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        0,
        winreg.KEY_SET_VALUE,
    )

    winreg.SetValueEx(n_key, "Observe", 0, winreg.REG_SZ, script_path)

    winreg.CloseKey(key)

    print("[+] Operation complete [+]")


def MakeStartApp() -> None:
    sys_platform = platform.system()

    if sys_platform == "Windows":
        add_to_startup()


# Create a subclass of QWidget
class HelloWorld(QWidget):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle("Organizer")

        # Create a QVBoxLayout to hold the button
        layout = QVBoxLayout(self)

        # Create a QPushButton widget
        button = QPushButton("Run", self)

        # Connect the button's clicked signal to a function
        button.clicked.connect(self.button_clicked)

        # Add the button to the layout
        layout.addWidget(button)

    # Function to handle button click
    def button_clicked(self):
        MakeStartApp()
        run()


# Create an instance of QApplication
app = QApplication(sys.argv)

# Create an instance of the custom QWidget subclass
window = HelloWorld()
window.setGeometry(100, 100, 300, 350)  # Set the position and size of the window

# Show the window
window.show()

# Start the event loop
sys.exit(app.exec_())
