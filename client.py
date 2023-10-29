## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##CLIENT
### This client open one connection, and dump all frames

import socket
import time
import pickle


import msgorganizer


host = "10.0.0.56"
port = 1891

msg = msgorganizer.Msg('./data/compressed/compress_adv_2740/*')
#fp = './data/compressed/compress_adv_2740/compress_201.pkl'
#fp_list = glob.glob('./data/compressed/compress_adv_2740/*')
#dat_dict = {fp:open(fp, 'rb').read() for fp in fp_list}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#for i in range(1):#send 1 package, 
for fp, dat in msg:
    s.sendall(dat)
    time.sleep(1/33)
s.close()
