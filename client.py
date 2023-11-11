## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##CLIENT
### This client open one connection, and dump all frames

import socket
import time
import pickle
import sys


import msgorganizer
import header

host = header.IP
port = header.PORT

def run(expid, port_offset=0):
    #TODO: start server accept, with expid for msgOrganizer, and socket port = header.port + offset
    msg = msgorganizer.Msg(expid)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port + port_offset))
    for fp, dat in msg:
        print (f'Send {len(dat)} bytes')
        s.sendall(dat)
        time.sleep(1/header.FPS)
    s.close()
    
    
if __name__=="__main__":
    if len(sys.argv) != 2:
        print ('!!!!!!!!!!!!!!!!!!ERROR, must provide expid!!!!!!!!!!!!!!!!!!!!!')
        raise
    expid = int(sys.argv[1]) #experimental identifier
    run(expid)


