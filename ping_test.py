# -*- coding: utf-8 -*-
"""
This script automates network latency tests by connecting to one or more remote devices
via SSH, executing ping commands to specified target IP addresses, and calculating the
average round-trip time.
"""

import re
import paramiko

# To install the required library, run: pip install paramiko

# --- Configuration ---
# A list of dictionaries, where each dictionary represents a device to connect to.
# Replace with your device information.
DEVICES = [
    {
        "host": "your_device_ip_1",
        "username": "your_username",
        "password": "your_password",
    },
    # Add more devices as needed
    # {
    #     "host": "your_device_ip_2",
    #     "username": "your_username",
    #     "password": "your_password",
    # },
]

# A list of strings, where each string is an IP address to ping.
TARGET_IPS = ["8.8.8.8", "1.1.1.1"]
# An integer representing the number of pings to send.
PING_COUNT = 10

def get_ping_average(ssh_client, target_ip, count=10):
    """
    Executes the ping command on the remote device and calculates the average round-trip time.

    Args:
        ssh_client (paramiko.SSHClient): The SSH client connected to the remote device.
        target_ip (str): The IP address to ping.
        count (int): The number of pings to send.

    Returns:
        float: The average round-trip time in milliseconds, or None if it cannot be determined.
    """
    stdin, stdout, stderr = ssh_client.exec_command(f"ping {target_ip} repeat {count}")
    output = stdout.read().decode("utf-8")

    # Regular expression to find the average round-trip time in milliseconds
    # This regex is designed to be flexible with the output of Cisco's ping command
    match = re.search(r"Success rate is \d+ percent \(\d+/\d+\), round-trip min/avg/max = \d+/(\d+)/\d+ ms", output)
    if match:
        return int(match.group(1))
    else:
        # Fallback regex for different ping output formats
        times = re.findall(r"time=(\d+\.?\d*) ms", output)
        if times:
            numeric_times = [float(t) for t in times]
            return sum(numeric_times) / len(numeric_times)
        else:
            return None

def main():
    """
    Main function to connect to devices and run ping tests.
    
    It iterates through the configured devices, establishes an SSH connection,
    and then runs ping tests for each target IP. It prints the results to the console.
    """
    for device in DEVICES:
        try:
            with paramiko.SSHClient() as ssh:
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(
                    device["host"],
                    username=device["username"],
                    password=device["password"],
                    timeout=10,
                    allow_agent=False,
                    look_for_keys=False,
                )
                print(f"--- Successfully connected to {device['host']} ---")

                for ip in TARGET_IPS:
                    print(f"Pinging {ip}...")
                    average_ping = get_ping_average(ssh, ip, PING_COUNT)

                    if average_ping is not None:
                        print(f"  Average ping to {ip}: {average_ping:.2f} ms")
                    else:
                        print(f"  Could not determine average ping to {ip}.")
                
                print("-" * (len(device['host']) + 30))

        except paramiko.AuthenticationException:
            print(f"Authentication failed for {device['host']}.")
        except Exception as e:
            print(f"An error occurred with {device['host']}: {e}")

if __name__ == "__main__":
    main()
