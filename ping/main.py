import os

# variable with IP or host
ip_or_host = input("Enter IP or host to be verified: ")

# passing IP or host for verification
os.system(f"ping -n 6 {ip_or_host}")
