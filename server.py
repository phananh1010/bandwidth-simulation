## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##SERVER
 
import socket
import time
import sys
import glob

import msgorganizer

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

fp_log = f'./logs/datapacket_arrival_log_exp{expid}'
file = open(fp_log, 'w')



msg = msgorganizer.Msg('./data/compressed/compress_adv_2740/*')
#N_MESSAGE = len(glob.glob('./data/compressed/compress_adv_2740/*'))#we are suppose to receive a pre-defined number of frame, no more
print (f'will wait and receive #{len(msg)} messages')

byteidx = 0
msgidx_list = set()#list of msg index received sofar
#for i in range(N_MESSAGE):
while True:#always receive frames, never breaks
    conn, addr = s.accept()
    btime0 = time.time()
    print (f'Accepting new connections')
    while True:
        btime = time.time()
        d = conn.recv(1024*1024)
        if not d: break
        else:
            print (f"just received data of len:{len(d)}")
            byteidx += len(d)
            if msg.getMsgIndex(byteidx) > -1:
                if byteidx not in msgidx_list:
                    msgidx_list.add(byteidx)
                    received_time = time.time()
                    transfer_time = (received_time - btime)*1000
                    print (f'New message received, msg_index: {len(msgidx_list)}, byte_index: {byteidx}, received_time:{received_time}, transfer_time: {transfer_time}')
    
    print (f"total transmission time for all packets: {time.time() - btime0} seconds")
    
#     dat = [frame_count, received_time, transfer_time]
#     file.write(f'{dat}\n')
    
    #logging section
    
    #####parse data, to be extended if future content evaluation required
    #####message_decoded = '\n'.join(s.decode('utf-8', 'ignore') for s in message)
#    file.flush()
    