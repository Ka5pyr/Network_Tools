#!/usr/bin/env python3.8

import psutil
import subprocess
import sys

nic = sys.argv[1]

if psutil.WINDOWS:
    cmd = f"Restart-NetAdapter -Name {nic}"
    subprocess.run(["powershell", "-Command", cmd], capture_output=True)
elif psutil.LINUX:
    cmd = f"systemctl restart network-manager restart"
    subprocess.run(["bash", "-c", cmd], capture_output=True)
elif psutil.FREEBSD:
    subprocess.run(['service', 'netif', 'restart', nic], capture_output=True)
elif psutil.MACOS or psutil.OSX:
    cmd = f"sudo ifconfig {nic}"
    subprocess.run(["zsh", "-c", cmd, down], capture_output=True)
    subprocess.run(["zsh", "-c", cmd, up], capture_output=True)
else:
    print("Could not detect OS")

print(f"[*] Interface {nic} Restarted")