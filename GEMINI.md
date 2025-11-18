# Project Overview

This project contains a Python script, `ping_test.py`, designed to automate network latency tests. It connects to one or more remote devices via SSH, executes ping commands to specified target IP addresses, and calculates the average round-trip time.

The script is built to be easily configurable for different devices and target IPs.

**Technologies:**

*   Python
*   Paramiko library for SSH connectivity

# Building and Running

**1. Install Dependencies:**

The script requires the `paramiko` library. Install it using pip:

```bash
pip install paramiko
```

**2. Configure the Script:**

This script requires two configuration files/sections:

*   **`devices.txt`**: Create a file named `devices.txt` in the same directory as `ping_test.py`. Each line in this file should contain the IP address or hostname of a device you want to SSH into.

    Example `devices.txt`:
    ```
    192.168.1.1
    192.168.1.2
    my_router.local
    ```

*   **`ping_test.py`**: Edit `ping_test.py` to set the common SSH credentials and ping parameters.
    *   `DEVICE_USERNAME`: Your SSH username for all devices.
    *   `DEVICE_PASSWORD`: Your SSH password for all devices.
    *   `TARGET_IPS`: A list of strings, where each string is an IP address to ping (e.g., `["8.8.8.8", "1.1.1.1"]`).
    *   `PING_COUNT`: An integer representing the number of pings to send.

**3. Run the Script:**

Execute the script from your terminal:

```bash
python ping_test.py
```

The script will then connect to each device listed in `devices.txt`, run the ping tests to `TARGET_IPS`, and print the average latency for each target IP.

# Development Conventions

*   **Configuration:** All configuration is done directly within the `ping_test.py` file.
*   **Error Handling:** The script includes basic error handling for SSH connection issues (e.g., authentication failures) and for cases where the ping output cannot be parsed.
*   **Modularity:** The core ping functionality is separated into the `get_ping_average` function, making it reusable and easy to understand.
