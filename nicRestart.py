#!/usr/bin/env python3.8

import psutil
import subprocess
import sys

# nic = sys.argv[1]
nic = input("NIC: ")

if psutil.WINDOWS:
    cmd = f"Restart-NetAdapter -Name {nic}"
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)
elif psutil.LINUX:
    subprocess.run(["FUNCTIONALITY COMING SOON!"], capture_output=True)
elif psutil.FREEBSD:
    subprocess.run(['service', 'netif', 'restart', nic], capture_output=True)
elif psutil.MACOS or psutil.OSX:
    cmd = "echo 'coming soon'"
    subprocess.run(["zsh", "-c", cmd], capture_output=True)
else:
    print("Could not detect OS")

print(f"[*] Interface {nic} Restarted")