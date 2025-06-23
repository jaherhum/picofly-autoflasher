"""
This script will auto-flash the latest PicoFly firmware on your RP2040.
"""
import os
import urllib.request
import sys
import time
import shutil
import requests
import psutil

os.system('title PicoFly AutoFlasher')


def download():
    """Downloads the latest firmware from rehius' GitHub Repo."""

    response = requests.get('https://api.github.com/repos/rehius/usk/releases/latest', timeout=30)

    for file in response.json()['assets']:

        if file['name'] == 'firmware.uf2':
            if os.path.isfile(f"{os.getcwd()}\\{file['id']}.uf2"): #Checks if the latest firmware is already downloaded.
                return f"{file['id']}.uf2"

            urllib.request.urlretrieve(file['browser_download_url'], f'{file['id']}.uf2')
            return f"{file['id']}.uf2"

    raise FileNotFoundError("The firmware was not found in the latest release.")

print(r"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  ____  _           _____ _                                                   ║
║ |  _ \(_) ___ ___ |  ___| |_   _                                             ║
║ | |_) | |/ __/ _ \| |_  | | | | |                                            ║
║ |  __/| | (_| (_) |  _| | | |_| |                                            ║
║ |_|   |_|\___\___/|_|   |_|\__, |                                            ║
║     _         _        ____|___/         _                                   ║
║    / \  _   _| |_ ___ |  ___| | __ _ ___| |__   ___ _ __                     ║
║   / _ \| | | | __/ _ \| |_  | |/ _` / __| '_ \ / _ \ '__|                    ║
║  / ___ \ |_| | || (_) |  _| | | (_| \__ \ | | |  __/ |                       ║
║ /_/   \_\__,_|\__\___/|_|   |_|\__,_|___/_| |_|\___|_|                       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║    GitHub:  https://github.com/jaherhum/picofly-autoflasher                  ║
╚══════════════════════════════════════════════════════════════════════════════╝
""")

FIRM_NAME = download()

def get_drives():
    """Gets a list containing all drives connected when executed."""

    drives = []
    for partition in psutil.disk_partitions(all=False):
        if "removable" in partition.opts:
            drives.append(partition.device)
    return set(drives)

def flash():
    """Flash the firmware."""
    while True:
        input('Disconnect (if connected) your RP2040 and press Enter...')
        drives_before = get_drives()
        print("\nPress the BOOT button in your RP2040 and connect it while pressing...")

        while True:
            time.sleep(1)
            drives_after = get_drives()
            rpico = drives_after - drives_before
            if rpico:
                break

        drive = ''.join(rpico)  # Transform from set to str.
        shutil.copyfile(f"{os.getcwd()}\\{FIRM_NAME}", f'{drive}\\firmware.uf2')

        again = input("\nDone! Do you want to flash another RP2040? Y/N\n>> ")
        if again.upper() == "N":
            sys.exit()

flash()
