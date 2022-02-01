# Get Mac
# John S.
# UM Cyber Bootcamp Student May 2021

import subprocess
import sys

# Enter in IP address of target device
ip = input("Enter address of Device: ")

#  statement prevents program from crashing if target does not respond
try:
    subprocess.check_output(f"ping {ip}")
except:
    print("The target device is not responding")
    sys.exit()

# retrieve arp info of target from local arp cache
arpInfo = subprocess.check_output(f"arp -a {ip}")
# print(arpInfo)

# split string to create a tuple
splitData = arpInfo.split()
# print(splitTup)

# print position 10 in tuple and decode output to ascii
print(f" The MAC is: {splitData[10].decode('ascii')}")
