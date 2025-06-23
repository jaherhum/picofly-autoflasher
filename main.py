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
            urllib.request.urlretrieve(file['browser_download_url'], 'firmware.uf2')
            break

def get_drives():
    """Gets a list containing all drives connected when executed."""

    drives = []
    for partition in psutil.disk_partitions(all=False):
        if "removable" in partition.opts:
            drives.append(partition.device)
    return set(drives)


def flash():
    """Flash the firmware."""

    input("Disconnect (if connected) your RP2040 and press any key.\n>> ")
    drives_before = get_drives()
    print("\nPress the BOOT button in your RP2040 and connect it while pressing...")

    while True:
        time.sleep(1)
        drives_after = get_drives()
        rpico = drives_after - drives_before
        if rpico:
            break
    drive = ''.join(rpico)  # Transform from set to str.

    shutil.copyfile(f"{os.getcwd()}\\firmware.uf2", f'{drive}\\firmware.uf2')

    input("\nDone! Press any key to exit...")
    sys.exit()

download()
flash()
