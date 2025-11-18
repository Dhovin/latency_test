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

Edit `ping_test.py` to include your device information and the target IPs you want to test.

*   `DEVICES`: A list of dictionaries, where each dictionary represents a device with its `host`, `username`, and `password`.
*   `TARGET_IPS`: A list of strings, where each string is an IP address to ping.
*   `PING_COUNT`: An integer representing the number of pings to send.

**3. Run the Script:**

Execute the script from your terminal:

```bash
python ping_test.py
```

The script will then connect to each device, run the ping tests, and print the average latency for each target IP.

# Development Conventions

*   **Configuration:** All configuration is done directly within the `ping_test.py` file.
*   **Error Handling:** The script includes basic error handling for SSH connection issues (e.g., authentication failures) and for cases where the ping output cannot be parsed.
*   **Modularity:** The core ping functionality is separated into the `get_ping_average` function, making it reusable and easy to understand.
