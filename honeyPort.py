#!/usr/bin/env python3.8

import socket
import subprocess

"""
Program: HoneyPort.py
Author:  Eric Keith
Date:    August 14, 2021
---

Purpose:
    This program is built to show the use of Python in Cybersecurity.

Functions:
    The Main Function
        The 'main' function is where the initial server is created.
        The server is created with the sockets command and will be
        listening on all networks for connections over a specified
        port.
        
    The Firewall Connect Function
        The 'firewall_connect' function is built to create an ssh
        connection to a Firewall over an IP. Each variable about
        the Firewall will start with the term 'fWall'. The ssh
        connection will be using an ssh pre-shared key instead of
        a password. This allows for the password to not be saved
        in this python script. 
        
        Once the ssh connection is made, a command will be run to
        add add a specified IP Address to the Firewall's Black or
        Block List.
        
        Once this has been completed, the Firewall will issue a
        reconnect connection command to the Blocked IP. This will
        knock the IP Address from the network and when the device
        attempts reconnection it will be blocked.
"""

port = 14155
ip = '0.0.0.0'    


def blocker(blockIP):
    
    with open("/etc/pf.conf", 'a') as f:
        f.write(f"block in on em0 from {blockIP} to any")
    cmd = "pfctl -f /etc/pf.conf"
    subprocess.run(['csh', '-c', cmd])
    
        

def main():
    
    # Setting up listener
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    s.listen(2)
    print(f"[*] Server Started: {ip}:{port}")
    
    # Setting Connection for Client PC
    while True:
        c, cAddr = s.accept()
        print(f"[*] Client Connection: {cAddr[0]}")
        
        # Send Bad IP to blocker function 
        blocker(cAddr[0])
        
        # firewall_connect(cAddr[0])
        c.close()
        print(f"[*] Client Close: {cAddr[0]}:{cAddr[1]}")


if __name__ == "__main__":
    main()
    
