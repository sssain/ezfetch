import platform
import os
import wmi
import socket
import psutil
import time
from colorama import Fore, Back, Style, init
init()


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

def seconds_elapsed():
    return time.time() - psutil.boot_time()



print("\n")
print(Fore.RED + platform.node())
print("-----------")
print("OS: ", platform.system(), platform.release())
print("Processor: ", platform.processor())
print("Uptime:", seconds_elapsed())
print(f"IP Address: {ip_address}")
print("Python Version: ", platform.python_version())
print('CPU Usage: ', psutil.cpu_percent(4),"%")
print('Ram Usage: ', psutil.virtual_memory()[2],"%", "\n")



