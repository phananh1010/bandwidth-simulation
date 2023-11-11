# bandwidth-simulation
Simulate the impact of bandwidth fluctuation on the stalling effect during a video streaming session


# STEP0 - Preparation
First, simulate bandwidth conditions with mahimahi. Here, we set delay at 200 miliseconds, and bandwidth traces stored in a pre-defined folder path. After setting the banwidth simulation, we start the conda (mamba) environment.
NOTE: `mm-link` and `mm-delay` shell must be created at the client, so that client and server could see each other. Launching `mm` at server may cause unknown glitch.

The merged FCC bandwidth traces, converted into mahimahi format, were backuped into `onelive` cloud, in `workspace` directory, `bandwidth-simulation` sub-directory.

```
mm-delay 200 #delay 50 miliseconds
mm-link /apps/workspace/data/bandwidth-trace/pensive/fcc/202008/mahimahi/merged_trace  /apps/workspace/data/bandwidth-trace/pensive/link12Mbps.trace  #uplink downlink
    mm-link /apps/workspace/data/bandwidth-trace/pensive/link3Mbps.trace  /apps/workspace/data/bandwidth-trace/pensive/link3Mbps.trace  #uplink downlink
mamba activate env_tile_streaming
```
# STEP 1 - use the program

#### What does it do?
This program simulate the stall when sending package from client to server.The client will read the frame size stored in file at './logs/...'. Each file in the log folder represent a list of frame size for a video streaming session. This program will send each frame in byte-array format to the server, under network fluctuation. (Assume you have done step 0)

The arrival timestamp for each frame will be logged, and we simulate total stalling time for each approach.

#### How to run it?
a) Use `.sh` script to start the server, it will run `n` server process, each server corresponds to a file in the `./logs/` folder.
```
./runexp.sh -s server
```
b) Use `.sh` script to start the clients. This script will run `n` client process, each corresponds to a file in the `./logs/` folder.
```
./runexp.sh -s client
```
c) Simulate the playback to calculate playback stall
```
./runexp.sh -s delay
```

d) Use this Python code to get delay for each experiment. Note that each experiment correspond to a file in the `./logs/` folder
```
import pickle
pickle.load(open('./logs/delay', 'rb'))#bandwidth mean is 1.5Mbps
```

e) Use this python code to get the name of the experiment, given the experiment id (expid)
```
import msorganizer

fparse = msgorganizer.FILEPARSER()
meta = fparse.return_metadict()         
meta
```
