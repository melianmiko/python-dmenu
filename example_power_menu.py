import subprocess

import dmenu

menu = dmenu.DMenuContent()


@menu.item("Suspend")
def test_1():
    subprocess.run(["systemctl", "suspend"])


@menu.item("Reboot")
def test_1():
    subprocess.run(["systemctl", "reboot"])


@menu.item("Shutdown")
def test_1():
    subprocess.run(["systemctl", "shutdown"])


@menu.item("Log out")
def test_1():
    subprocess.run(["hyprctl", "dispatch", "exit"])


if __name__ == "__main__":
    menu.run()
