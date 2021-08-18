#!/usr/bin/env python3.8

import psutil
import socket


if __name__ == "__main__":

    nics = {}
    info = {"state": "", "ip": ""}
    nicAddrs = psutil.net_if_addrs()
    nicStats = psutil.net_if_stats()
    
    
    for nic, stat in nicStats.items():
        info = {'ip':'-', 'gateway':'-', 'ip6':'-', 'mac':'-', 'state':'-'}
        for addr in nicAddrs[nic]:
            if addr.family == socket.AF_INET:
                info['ip'] = addr.address
                info['gateway'] = '-' if addr.broadcast is None else addr.broadcast
            elif addr.family == socket.AF_INET6:
                info['ip6'] = addr.address
            elif addr.family == psutil.AF_LINK:
                info['mac'] = addr.address
        
        info['state'] = "up" if nicStats[nic].isup else "down"
        nics[nic] = info

    
    print(f"\n{'-' * 111}")
    print(f"| {'Interface':^13} | {'State':^7} | {'IPv4':^15} | {'IPv4 Gateway':^15} | {'IPv6 Address':^45} |")
    print(f"| {'-'*13}   {'-'*7}   {'-'*15}   {'-'*15}   {'-'*45} |")
    for nic, addr in nics.items():        
        print(f"| {nic:^13} | {nics[nic]['state']:^7} | {nics[nic]['ip']:^15} | {nics[nic]['gateway']:^15} | {nics[nic]['ip6']:^45} |")
    print(f"{'-' * 111}\n")