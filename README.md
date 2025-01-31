# Remote Phone Caller

This project allows you to remotely control your Android phone to make calls using a Python script. It uses ADB (Android Debug Bridge) to send commands to the phone over Wi-Fi or USB.

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
   - [Installing ADB](#installing-adb)
   - [Enabling USB Debugging](#enabling-usb-debugging)
4. [Setting Up the Project](#setting-up-the-project)
   - [Using USB](#using-usb)
   - [Using Wi-Fi](#using-wi-fi)
5. [Running the Project](#running-the-project)
6. [Troubleshooting](#troubleshooting)
7. [Contributing](#contributing)
8. [License](#license)

---

## Features
- Make calls remotely from your PC or another device.
- Works over Wi-Fi or USB.
- Easy-to-use Flask server on the phone.

---

## Prerequisites
- **Python 3.x** installed on both the phone and PC.
- **ADB** installed on the PC and phone.
- **USB Debugging** enabled on the phone.
- Both devices (phone and PC) must be on the **same Wi-Fi network** for Wi-Fi setup.
- **Your phone's IP address must be configured in the scripts.**

---

## Installation

### Installing ADB
ADB (Android Debug Bridge) is a command-line tool that allows communication between your PC and Android device.

#### On Windows:
1. Download the [ADB installer](https://developer.android.com/studio/releases/platform-tools).
2. Extract the files and add the folder to your system’s PATH:
   - Right-click on **This PC** > **Properties** > **Advanced system settings** > **Environment Variables**.
   - Under **System variables**, find `Path`, click **Edit**, and add the path to the ADB folder.

#### On macOS/Linux:
```sh
brew install android-platform-tools
```

#### On Android (Termux):
```sh
pkg update
pkg install android-tools
```

---

### Enabling USB Debugging
To enable USB debugging on your Android device:
1. Go to **Settings > About Phone > Tap Build Number 7 times** to enable Developer Options.
2. Go to **Developer Options** and enable **USB Debugging**.
3. Connect your phone to your PC via USB.
4. On your phone, when prompted, select **Allow USB Debugging**.

---

## Setting Up the Project

### Fill the ip of the phone and the number you wanna call

```
phone_ip = '192.168.1.123'
number_to_call = '+1234567890'
```
### Using USB
1. Connect your phone to your PC via USB.
2. Ensure ADB recognizes your device:
```sh
adb devices
```
   - If your device is listed, you’re ready to proceed.
   - If not, check your USB connection and ensure USB debugging is enabled.

3. Clone this repository:
```sh
git clone https://github.com/your-username/remote-phone-caller.git
cd remote-phone-caller
```

4. Install the required Python libraries:
```sh
pip install flask requests
```

5. **Set your phone's IP address** in `phone_server.py` and `pc_controller.py`.

6. Run the Flask server on your phone:
```sh
python phone_server.py
```

7. Run the PC controller script:
```sh
python pc_controller.py
```

---

### Using Wi-Fi
1. Connect your phone to your PC via USB.
2. Enable ADB over Wi-Fi:
```sh
adb tcpip 5555
```
3. Disconnect the USB cable.
4. Find your phone’s IP address:
   - Go to **Settings > Wi-Fi** and tap on the connected network to see the IP address (e.g., `192.168.1.123`).
5. Connect to your phone over Wi-Fi:
```sh
adb connect 192.168.1.123:5555
```
6. Verify the connection:
```sh
adb devices
```
   - Your device should be listed with its IP address.

7. Clone this repository:
```sh
git clone https://github.com/your-username/remote-phone-caller.git
cd remote-phone-caller
```

8. Install the required Python libraries:
```sh
pip install flask requests
```

9. **Set your phone's IP address** in `phone_server.py` and `pc_controller.py`.

10. Run the Flask server on your phone:
```sh
python phone_server.py
```

11. Run the PC controller script:
```sh
python pc_controller.py
```

---

## Running the Project
1. Ensure the Flask server is running on your phone.
2. Run the PC controller script to send a phone number to the phone.
3. The phone will initiate the call.

### Important Notes:
- **You must set the correct IP address of your phone** in both `phone_server.py` and `pc_controller.py` before running the code.
- The command `python pc_controller.py --call +1234567890` does not work as expected and should not be used.
- Always verify the ADB connection before running the scripts.

---

## Troubleshooting

### ADB No Devices/Emulators Found
- Ensure USB debugging is enabled on your phone.
- Try a different USB cable or port.
- Restart ADB:
```sh
adb kill-server
adb start-server
```

### ADB Over Wi-Fi Not Working
- Ensure both devices are on the same Wi-Fi network.
- Reconnect using:
```sh
adb connect 192.168.1.123:5555
```
- Restart ADB:
```sh
adb kill-server
adb start-server
```

### Flask Server Not Running
- Ensure Python and Flask are installed on your phone.
- **Check that your phone's IP address is correctly set in the scripts.**
- Check the logs for errors.

---

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

