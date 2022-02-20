import platform
import os
import socket
import psutil
import time
from colorama import Fore, Back, Style, init
init()
from cpuinfo  import get_cpu_info as cpu_info


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

def seconds_elapsed():
    return time.time() - psutil.boot_time()

print("\n")
print(Fore.BLUE + """  
                   .oodMMMMMMMMMMMMM
       ..oodMMM  MMMMMMMMMMMMMMMMMMM
 oodMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 MMMMMMMMMMMMMM  MMMMMMMMMMMMMMMMMMM
 `^^^^^^MMMMMMM  MMMMMMMMMMMMMMMMMMM
       ````^^^^  ^^MMMMMMMMMMMMMMMMM
                      ````^^^^^^MMMM
                      """)
print("ezfetch 1.0.0")
print("\n")
print(Fore.RED + platform.node())
print("-----------")
print("OS: ", platform.system(), platform.release())
print("CPU: ", cpu_info()['brand_raw'])
print("Uptime:", seconds_elapsed())
print(f"IP Address: {ip_address}")
print("Python Version: ", platform.python_version())
print('CPU Usage: ', psutil.cpu_percent(4),"%")
print('Ram Usage: ', psutil.virtual_memory()[2],"%", "\n")




