## REFERENCE: https://stackoverflow.com/questions/15003778/i-want-to-stream-a-webcam-feed-using-socket-programming-in-python
##SERVER
import socket
import time
import sys

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
frame_count = 0
file = open(fp_log, 'a')

while True:#always receive frames, never breaks
    conn, addr = s.accept()
    message = []
    while True:
        btime = time.time()
        d = conn.recv(1024*1024)
        if not d: break
        else: message.append(d)
        received_time = time.time()
        transfer_time = (received_time - btime)*1000
        print (f"received data for frame #{frame_count}, took: {transfer_time} ms")
        
        dat = [frame_count, received_time, transfer_time]
        file.write(f'{dat}\n')
        frame_count += 1
        #logging section
    
    #parse data, to be extended if future content evaluation required
    #message_decoded = '\n'.join(s.decode('utf-8', 'ignore') for s in message)
    
    file.flush()