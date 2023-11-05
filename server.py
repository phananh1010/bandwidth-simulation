## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##SERVER
 
import socket
import time
import sys
import glob
import pickle

import msgorganizer
import header

if len(sys.argv) != 2:
    print ('ERROR, must provide expid')
    raise
expid = int(sys.argv[1]) #experimental identifier

host="0.0.0.0"
port=1891


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)


##log session, write pacte received data to file

fp_log = header.LOG_FILETEMPLATE.format(expid)
filelog = open(fp_log, 'wb')



msg = msgorganizer.Msg(expid)
#N_MESSAGE = len(glob.glob('./data/compressed/compress_adv_2740/*'))#we are suppose to receive a pre-defined number of frame, no more
print (f'will wait and receive #{len(msg)} messages')

byteidx = 0
msgidx_list = set()#list of msg index received sofar
log = []
#for i in range(N_MESSAGE):

conn, addr = s.accept()
btime0 = time.time()
print (f'Accepting new connections')
while True:
        btime = time.time()
        d = conn.recv(1024*1024)
        if not d: break
        else:
            #print (f"just received data of len:{len(d)}")
            byteidx += len(d)
            if msg.getMsgIndex(byteidx) > -1:
                if byteidx not in msgidx_list:
                    msgidx_list.add(byteidx)
                    received_time = time.time()
                    transfer_time = (received_time - btime)*1000
                    #print (f'New message received, msg_index: {len(msgidx_list)}, byte_index: {byteidx}, received_time:{received_time}, transfer_time: {transfer_time}')
                    log.append(received_time)
print (f"total transmission time for all packets: {time.time() - btime0} seconds")
log = [item - log[0] for item in log[1:]]
pickle.dump(log, filelog)

s.close()
    