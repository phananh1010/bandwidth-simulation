## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##CLIENT

import socket
import time
import pickle
import glob

host = "localhost"
port = 1890

#fp = './data/compressed/compress_adv_2740/compress_201.pkl'
fp_list = glob.glob('./data/compressed/compress_adv_2740/*')
dat_dict = {fp:open(fp, 'rb').read() for fp in fp_list}

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#socket.SOCK_STREAM)
#for i in range(1):#send 1 package, 
for fp in fp_list:
    dat = dat_dict[fp]
    s.sendto(dat, (host, port))
s.close()
time.sleep(0.5)