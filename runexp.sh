#!/bin/bash

#TODO: run experiment for server and client for exp=5->20

mamba activate env_tile_streaming

for i in {0..15}; 
do 
python server.py $i&
sleep .5
python client.py $i&
sleep 25
done;