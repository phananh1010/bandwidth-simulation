# bandwidth-simulation
Simulate the impact of bandwidth fluctuation on the stalling effect during a video streaming session


## Step 0 - Preparation
First, simulate bandwidth conditions with mahimahi. Here, we set delay at 200 miliseconds, and bandwidth traces stored in a pre-defined folder path. After setting the banwidth simulation, we start the conda (mamba) environment.
NOTE: `mm-link` and `mm-delay` shell must be created at the client, so that client and server could see each other. Launching `mm` at server may cause unknown glitch.

The merged FCC bandwidth traces, converted into mahimahi format, were backuped into `onelive` cloud, in `workspace` directory, `bandwidth-simulation` sub-directory.

```
mm-delay 200 #delay 50 miliseconds
mm-link /apps/workspace/data/bandwidth-trace/pensive/fcc/202008/mahimahi/merged_trace  /apps/workspace/data/bandwidth-trace/pensive/link12Mbps.trace  #uplink downlink
mamba activate env_tile_streaming
```
