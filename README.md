# PicoFly Autoflasher

![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/license-AGPLv3-blue)
![Requirements](https://img.shields.io/badge/dependencies-pip--requirements-blue)

A Python script to automatically detect and flash PicoFly firmware to RP2040 devices (such as PicoFly).  

---

## 🚀 Features

- Automatically detects RP2040 devices in BOOTSEL mode.
- Downloads the latest PicoFly firmware.
- Flashes firmware with minimal user interaction.
- Fast and user-friendly, ideal for quick setups.
- ✅ Precompiled `.exe` available for Windows — no need for Python or setup.

---

## 💻 Installation (Python Version)

1. Clone this repository:

   ```bash
   git clone https://github.com/jaherhum/picofly-autoflasher.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧩 Usage (Python Script)

1. Run the script:

   ```bash
   python main.py
   ```

2. Follow the on-screen instructions.

3. The script will automatically:
   - Detect your devices.
   - Download the latest firmware.
   - Flash it to the connected RP2040.

---

## 🔄 Alternative: Use the Precompiled `.exe`

If you don't have Python installed, you can simply download the standalone executable from the [Releases](https://github.com/jaherhum/picofly-autoflasher/releases) section.

### Steps:

1. Go to the [Releases page](https://github.com/jaherhum/picofly-autoflasher/releases).
2. Download the latest `PicoFlyAutoFlasher.exe` file.
3. Double-click the `.exe` and follow the on-screen instructions.

> ✅ No installation required.  
> 🖥️ Only works on **Windows**.

---

## 🐞 Issues

Please open an issue if you find any problems, bugs, or unexpected behavior.

---

## 📜 License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

You can:

- **Use** — use the software for any purpose, including commercial.
- **Study and modify** — access the source code and make changes.
- **Share** — redistribute the software under the same license.
- **Host and distribute** — even as a service, but must share source code.

Under the following terms:

- **Source Code Disclosure** — If you modify or use this software over a network (e.g., as a service), you must make the complete source code of your modified version available.
- **Copyleft** — Derivative works must also be licensed under AGPLv3.
- **Notice** — You must include a copy of the license and state any changes made.

📄 [Read the full license](https://www.gnu.org/licenses/agpl-3.0.html)


---

## ⚠️ Disclaimer

This project is not affiliated with the developers of PicoFly.  
Use at your own risk. Flashing unofficial firmware may void warranties or violate terms of service.

---

## 🙌 Credits

Made by **Jaherhum**.
