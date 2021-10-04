import os
import sys


def bypass_port_22():
    if sys.platform.startswith('linux'):
        os.system('sudo ufw allow 22/tcp')
    elif sys.platform.startswith('darwin'):
        os.system('sudo pfctl -d')
        os.system('sudo nano /etc/pf.conf')
        os.system('sudo pfctl -f /etc/pf.conf')
        os.system('sudo pfctl -E')
    elif sys.platform.startswith('win32'):
        os.system('netsh advfirewall firewall add rule name="NetBIOS UDP Port 22" dir=in action=allow protocol=UDP localport=22')
        os.system('netsh advfirewall firewall add rule name="NetBIOS UDP Port 22" dir=out action=allow protocol=UDP localport=22')
    else:
        os.system('sudo pfctl -d')
        os.system('sudo nano /etc/pf.conf')
        os.system('sudo pfctl -f /etc/pf.conf')
        os.system('sudo pfctl -E')


bypass_port_22()
