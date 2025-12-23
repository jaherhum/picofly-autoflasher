"""
This script will auto-flash the latest PicoFly firmware on your RP2040.
"""
import os
import urllib.request
import sys
import shutil
import platform
import requests
import psutil

os.system('title PicoFly AutoFlasher')


def download() -> str:
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

def get_drives() -> set:
    """Gets a list containing all drives connected when executed."""

    drives = []
    for partition in psutil.disk_partitions(all=False):
        if "removable" in partition.opts:
            drives.append(partition.device)
    return set(drives)

def check_os() -> str:
    '''Checks your current OS (LINUX/WINDOWS).'''
    system = platform.system()
    if system not in ['Linux', 'Windows']:
        print(f'Your OS ({system}) is not compatible with this script.\nPress any key to exit.')
        os.system('pause')
        sys.exit()
    return system



def flash():
    """Flash the firmware."""
    system = check_os()
    while True:

        if system == 'Linux':
            import subprocess
            import glob

            print('Connect your RP2040s pressing the BOOT button...')
            input("Then, press Enter...\n")

            rpico = glob.glob('/dev/disk/by-label/RPI-RP2*')
            for device in rpico:
                # Mounts with: udisksctl mount -b /dev/disk/by-label/RPI-RP2...
                result = subprocess.run(
                    ["udisksctl", "mount", "-b", device],
                    capture_output=True,
                    text=True,
                    check=True
                )

                # "Mounted /dev/sdb1 at /run/media/(user)/RPI-RP2.\n"
                output = result.stdout.strip()
                # Get mount path only
                mount_point = output.split(" at ")[1].rstrip(".")
                print("Mounted:", mount_point)
                # Copy firmware
                shutil.copyfile(
                    os.path.join(os.getcwd(), FIRM_NAME),
                    os.path.join(mount_point, "firmware.uf2")
                )



        elif system == 'Windows': # In case of adding support for MacOS (probably not)

            input('Disconnect (if connected) your RP2040s and press Enter...')
            drives_before = get_drives()
            input("Connect them pressing the BOOT button, and press Enter when finished...\n")


            drives_after = get_drives()
            rpicos = drives_after - drives_before

            for rpico in rpicos:
                drive = ''.join(rpico)  # Transform from set to str.
                shutil.copyfile(
                    os.path.join(os.getcwd(), FIRM_NAME),
                    os.path.join(drive, "firmware.uf2"))

        input("\nDone! Press Enter to exit. ")
        sys.exit()

flash()
