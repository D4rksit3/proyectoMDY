import sys
import traceback
import socket
try:
    for cont in range(1,int(sys.argv[1])):
        puerto=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        puerto.settimeout(5000)
        conexion = puerto.connect_ex((sys.argv[2],cont))
        if conexion == 0:
            print(str(cont)+":OPEN")
        puerto.close
except:
    traceback.print_exc()
    print("USAGE python port_scanner.py MAXPORT IP")