import subprocess
import socket
import time
import os
import psutil
import requests
import os, sys
from os import system
from colorama import Fore, Back, Style

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
purple = Fore.MAGENTA + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
white = Fore.WHITE + Style.BRIGHT
no_colour = Fore.RESET + Back.RESET + Style.RESET_ALL


def line_print(n):
    for word in n + "\n":
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(0.05)


# tool version
version = "1.1"

# CHECK INTERNET

socket.setdefaulttimeout(30)


def check_intr(host="8.8.8.8", port=53, timeout=5):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        print(f'{red}No internet!')
        time.sleep(2)
        check_intr()


def spin():
    pid = os.getpid()
    delay = 0.25
    spinner = ['█■■■■', '■█■■■', '■■█■■', '■■■█■', '■■■■█']

    while any(pid in p.info for p in psutil.process_iter(['pid'])):
        for i in spinner:
            sys.stdout.write(f"\033[34m\r[*] Downloading..please wait.........\e[33m[\033[32m{i}\033[33m]\033[0m   ")
            sys.stdout.flush()
            time.sleep(delay)
            sys.stdout.write("\b" * 8)
        sys.stdout.write(" " * 8 + "\b" * 8)

    sys.stdout.write("\033[1;33m [Done]\033[0m")
    print("")


def banner():
    print(f'{red} ______                                  __  __           __   _            ')
    print(f'{cyan}/_  __/__  _________ ___  __  ___  __   / / / /___ ______/ /__(_)___  ____ _')
    print(f'{yellow} / / / _ \/ ___/ __ `__ \/ / / / |/_/  / /_/ / __ `/ ___/ //_/ / __ \/ __ `/')
    print(f'{blue} / / /  __/ /  / / / / / / /_/ />  <   / __  / /_/ / /__/ ,< / / / / / /_/ / ')
    print(f'{red}/_/  \___/_/  /_/ /_/ /_/\__,_/_/|_| _/_/ /_/\__,_/\___/_/|_/_/_/ /_/\__, /  ')
    print(f'{yellow}             __          (_)      __(_)      __                     /____/   ')
    print(f'{green}            / /   ____ _/ /_     / ___/___  / /___  ______                   ')
    print(f'{cyan}           / /   / __ `/ __ \    \__ \/ _ \/ __/ / / / __ \                  ')
    print(f'{red}          / /___/ /_/ / /_/ /   ___/ /  __/ /_/ /_/ / /_/ /                  ')
    print(f'{yellow}         /_____/\__,_/_.___/   /____/\___/\__/\__,_/ .___/                   ')
    print(f'{blue}                                                  /_/                        ')
    print("                       Tool Name: TermuxSetupHackingLab")
    print("                       Developer: @G_Man_Official")
    print(f"{cyan}                Telegram :: https://t.me/hacking_network8")
    print(f'{yellow}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')


def check_termux():
    # Install a package using pkg command
    package_name = "proot"
    result = subprocess.run(["pkg", "install", package_name, "-y"], capture_output=True)

    if result.returncode == 0:
        print("Package installation successful.")
    else:
        print("Package installation failed. Error message:")
        print("Trying To Change The Repo")
        os.system(f"echo 'deb https://termux.mentality.rip/termux-main stable main stable main' > $PREFIX/etc/apt/sources.list")
        os.system("apt update && apt upgrade -y")


def update():
    check_intr()
    git_ver = str(
        requests.get(
            "https://raw.githubusercontent.com/GManOfficial/Termux_HackingLab_Setup/blob/main/.version"
        ).text
    ).split()
    if version == git_ver[0]:
        system("clear")
        banner()
        print("Termux_ is up-to-date\n")
    elif version != git_ver and git_ver != "404: Not Found":
        changelog = requests.get(
            "https://raw.githubusercontent.com/GManOfficial/Termux_HackingLab_Setup/blob/main/.changelog.log"
        ).text
        update_commands = requests.get(
            "https://raw.githubusercontent.com/GManOfficial/Termux_HackingLab_Setup/blob/main/.update"
        ).text
        system("clear")
        banner()
        print(
            f"Termux_ has a new update!\nCurrent Version: {red}{version}\nAvailable Version: {green}{git_ver}\n"
        )
        update_ask = input("Do you want to update Termux_?[y/n] > " + green)
        if update_ask == "y":
            print(no_colour)
            system(update_commands)
            line_print(
                "\n"
                + green
                + "Termux_ updated successfully!! Please restart terminal!\n"
            )
            if changelog != "404: Not Found":
                print("Changelog:\n" + purple)
            exit()
        elif update_ask == "n":
            print(
                "\n"
                + "Updating cancelled. Using old version! \nVERSION : "
                + version
            )
            time.sleep(2)
        else:
            print("\nWrong input!\n")
            time.sleep(2)

if __name__ == "__main__":
  try:
    update()
    os.system("pip3 install -r requirements.txt")
    os.system("clear")
    banner()
    time.sleep(1)
    print(" ")
    print(" ")
    print(f"{green}                       Please Wait For A While We Check Everything... ")
    spin()
    os.system("apt update && apt upgrade -y")
    os.system("pip3 install -r requirements.txt")
    os.system("termux-setup-storage")
    check_termux()
    os.system("python3 pkg_installer.py")

  except KeyboardInterrupt:
    line_print("\n" + green + "Thanks for using This Tool!\n" + no_colour)


