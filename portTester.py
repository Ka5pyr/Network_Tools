import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(1)

ip = "192.168.1.61"
print(f"Checking For Open Ports on {ip}")
for port in [22, 80, 443]:
    response = s.connect_ex(("192.168.1.61", port))
    if response == 0:   
        print(f"  [*] Port {port} Open!")
   # else:
   #     print(f"  [*] Port {port} Closed")
    s.close()
print("Scan Complete")
