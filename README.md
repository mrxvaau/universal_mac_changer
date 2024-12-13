# Universal MAC Address Changer

This project provides tools for generating and setting a new MAC address across different operating systems: Windows, Linux, and macOS. It includes:

1. A universal Python script (`universal_mac_changer.py`) that detects the operating system and performs the necessary steps to change the MAC address.
2. Individual scripts for each platform:
   - `mac_address_windows.bat`
   - `mac_address_linux.sh`
   - `mac_address_mac.sh`

## Prerequisites

### Windows
- Administrative privileges
- `netsh` command available (default in Windows)
- Access to the registry editor via command line

### Linux
- `ip` command installed (default in most Linux distributions)
- `sudo` permissions

### macOS
- `ifconfig` command available (default in macOS)
- Administrative permissions

### Python Script
- Python 3.x installed
- Necessary permissions for executing network commands

## How to Run

### Using the Universal Python Script

1. Ensure you have Python 3.x installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing `universal_mac_changer.py`.
4. Run the script:
   ```bash
   python universal_mac_changer.py
   ```
5. Follow the prompts. The script will detect your OS and execute the corresponding commands.

### Windows Script (`mac_address_windows.bat`)

1. Open the Command Prompt as Administrator.
2. Navigate to the directory containing `mac_address_windows.bat`.
3. Run the script:
   ```
   mac_address_windows.bat
   ```
4. The script will generate a new MAC address, disable the Wi-Fi interface, update the registry, and re-enable the interface.

### Linux Script (`mac_address_linux.sh`)

1. Open a terminal.
2. Navigate to the directory containing `mac_address_linux.sh`.
3. Make the script executable:
   ```bash
   chmod +x mac_address_linux.sh
   ```
4. Run the script with `sudo`:
   ```bash
   sudo ./mac_address_linux.sh
   ```
5. The script will detect the active network interface, generate a new MAC address, disable the interface, set the new MAC, and re-enable it.

### macOS Script (`mac_address_mac.sh`)

1. Open the Terminal.
2. Navigate to the directory containing `mac_address_mac.sh`.
3. Make the script executable:
   ```bash
   chmod +x mac_address_mac.sh
   ```
4. Run the script with `sudo`:
   ```bash
   sudo ./mac_address_mac.sh
   ```
5. The script will identify the active Wi-Fi interface, generate a new MAC address, disable the interface, set the new MAC, and re-enable it.

## Notes

- Ensure you have the necessary administrative permissions on your system to run these scripts.
- Some network adapters may not support MAC address changes.
- These scripts are for educational and testing purposes only. Use responsibly.

## Troubleshooting

- **Permission Denied**: Ensure you’re running the script with `Administrator` or `sudo` privileges.
- **Interface Not Found**: Verify the active network interface and modify the script if needed.
- **Command Not Found**: Ensure required utilities (`netsh`, `ip`, `ifconfig`) are installed and accessible.

## Disclaimer

The use of these scripts is at your own risk. Always ensure compliance with local laws and regulations when modifying your device’s MAC address.

