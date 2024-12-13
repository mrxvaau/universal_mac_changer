### Universal MAC Address Changer Script

# This script detects the operating system and executes the appropriate logic to change the MAC address.

import os
import platform
import subprocess
import random

# Function to generate a valid MAC address
def generate_mac():
    hex_chars = "0123456789ABCDEF"
    mac = ["02"]  # Locally administered MAC address prefix
    for _ in range(5):
        mac.append("-".join(random.choice(hex_chars) + random.choice(hex_chars)))
    return "".join(mac)

# Function to execute system commands
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Windows MAC address changer
def change_mac_windows():
    mac = generate_mac()
    print(f"Generated MAC Address: {mac}")

    disable_command = "netsh interface set interface name=\"Wi-Fi\" admin=disabled"
    registry_command = (
        f"reg add \"HKLM\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001\" "
        f"/v \"NetworkAddress\" /t REG_SZ /d {mac} /f"
    )
    enable_command = "netsh interface set interface name=\"Wi-Fi\" admin=enabled"

    run_command(disable_command)
    run_command(registry_command)
    run_command(enable_command)
    print(f"Successfully changed the MAC address to: {mac}")

# Linux MAC address changer
def change_mac_linux():
    mac = generate_mac()
    print(f"Generated MAC Address: {mac}")

    # Replace eth0 with the correct interface name
    interface = subprocess.getoutput("ip -o link show | awk -F': ' '{print $2}' | head -n 1")

    disable_command = f"sudo ip link set dev {interface} down"
    set_mac_command = f"sudo ip link set dev {interface} address {mac}"
    enable_command = f"sudo ip link set dev {interface} up"

    run_command(disable_command)
    run_command(set_mac_command)
    run_command(enable_command)
    print(f"Successfully changed the MAC address to: {mac}")

# macOS MAC address changer
def change_mac_mac():
    mac = generate_mac()
    print(f"Generated MAC Address: {mac}")

    # Find active interface
    interface = subprocess.getoutput(
        "networksetup -listallhardwareports | awk '/Wi-Fi/{getline; print $2}'"
    )

    disable_command = f"sudo ifconfig {interface} down"
    set_mac_command = f"sudo ifconfig {interface} ether {mac}"
    enable_command = f"sudo ifconfig {interface} up"

    run_command(disable_command)
    run_command(set_mac_command)
    run_command(enable_command)
    print(f"Successfully changed the MAC address to: {mac}")

# Detect the operating system and call the appropriate function
def main():
    os_type = platform.system()

    if os_type == "Windows":
        change_mac_windows()
    elif os_type == "Linux":
        change_mac_linux()
    elif os_type == "Darwin":
        change_mac_mac()
    else:
        print(f"Unsupported operating system: {os_type}")

if __name__ == "__main__":
    main()
