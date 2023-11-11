from collections import deque 
import numpy as np
import pickle
import sys
import time
import argparse

import header
import msgorganizer
import imp
import server
import client
imp.reload(header)


parser = argparse.ArgumentParser()
parser.add_argument('-s', '--service')      # option that takes a value
parser.add_argument('-f', '--ipnbOnly')

args = parser.parse_args()
if args.ipnbOnly != None:
        service = header.DEV_MODE
elif args.service == None or args.service not in {header.CLIENT, header.SERVER, header.DELAY, header.DEV_MODE}:
        print ('ERROR: must specify -s (service), service take values [{header.CLIENT, header.SERVER, header.DELAY}]')
        raise
else:
        service     = args.service

class PlaybackBuffer:
    #BUFFER_SIZE = 10 #10 frames max
    #BUFFERING_MAX = 5 #everytime buffering, fill 5 frames
    #BUFFERING_MIN = 1 #everytime buffer size less than 0, start the buffering
    
    def __init__(self, playback_log, fps):
        #TODO: simulate buffer stalling[hgg]
        #INPUT: playback_log is the arrival time (system time) of all playback frame
        
#         self.playback_logdict = {}  #dict structure, log the arrival of frame. Format - systemTime:playbackTime 
#         self.system_time_list  = playback_log #list of arrival system time for frame
#         for tiidx, ti in enumerate(self.system_time_list):
#             self.playback_logdict[ti] = tiidx/fps
        self.playback_log = deque([[fidx, ti] for fidx, ti in enumerate(playback_log)])
        self.buffer       = deque([])
        
    def receive(self, system_time):
        #TODO: supplement buffer with data, given system time pop all frame from playback_log, and push to buffer
        # NOTE: for a given system time, multiple or no frames may arrive
        while (len(self.playback_log) > 0) and self.playback_log[0][1] < system_time:
            fidx, ti = self.playback_log.popleft()
            self.buffer.append(fidx)
            
        
    def pop(self, frame_idx):
        #TODO: return the frame with indexed by frame_idx from buffer, if available, else return -1
        while len(self.buffer) > 0 and self.buffer[0] < frame_idx: #remove all item from buffer until playback time
            self.buffer.popleft()
            
        if len(self.buffer) == 0:
            return -1
        elif self.buffer[0] == frame_idx:
            return self.buffer.popleft()
        elif self.buffer[0] > frame_idx:
            return -1
        else:
            raise

class Playback:
    def __init__(self, expid):
        self.expid = expid
        self.fps   = header.FPS
        self.fp    = header.LOG_FILETEMPLATE.format(expid)
        self.delay_list      = []
        self.fparse = msgorganizer.FILEPARSER()
        self.meta = fparse.return_metadict()[expid]
        
    #### INTERFACE FUNCTIONS
    def play(self, verbose=True):
        playbackRawData = pickle.load(open(self.fp, 'rb'))
        ##################DEBUG CODE, REMOVE AFTER#################
        #playbackRawData = self.insert()
        ##################
        pb              = PlaybackBuffer(playbackRawData, self.fps)
        playback_time   = 0
        fps             = self.fps
        frame_idx       = int(playback_time * fps)
        for system_time in np.arange(0, self.meta['length'], 1/fps):
            pb.receive(system_time)
            is_frame  = pb.pop(frame_idx)
            if verbose==True: print (f'have frame? {is_frame}, buffer: {len(pb.buffer)}')
            if is_frame > -1:
                frame_idx += 1
            else:
                self.delay_list.append(1/fps)
                
    def get_delay(self):
        return sum(self.delay_list)

#INTERFACE FUNCTIONALITY
    
def sim_server():
    #TODO: simulate transferring packets of server for all experiments
    for port_offset, expid in enumerate(expid_list):
        server.run(expid, port_offset)
    return

def sim_client():
    #TODO: simulate transferring packets of clients for all experiments
    for port_offset, expid in enumerate(expid_list):
        client.run(expid, port_offset)
        time.sleep(35)
    return 

def sim_delay():
    #TODO: go through all experiment, run experiment, get delay for each experiment, dumpto file
    #    NOTE: use log files produces by sim_server function
    result_dict = {}
    for expid in expid_list:
        pl = Playback(expid)
        pl.play()
        delay = pl.get_delay()
        result_dict[expid] = delay
        pickle.dump(result_dict, open(header.LOG_DELAY, 'wb'))

fparse = msgorganizer.FILEPARSER()
meta = fparse.return_metadict()         
expid_list = list(meta.keys())        
if __name__ == '__main__':
    if service == header.CLIENT:
        print ('processing client')
        sim_client()
    elif service == header.SERVER:
        print ('processing server')
        sim_server()
    elif service == header.DELAY:
        print ('processing delay')
        sim_delay()