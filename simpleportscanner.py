#!/bin/python

import sys
import socket
import pyfiglet
from datetime  import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1])
else:
        print("Invalid amount of arguments.")
        print("Syntax: python3 scanner.py <ip address>")

print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("Made by Russell")
print("-" * 50)

try:
        for port in range(1,65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target,port))
                if result == 0:
                        print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
        print("\nExiting program.")
        sys.exit()
except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
except socket.error:
        print("Couldn't connect to the server")
        sys.exit()
