#!/bin/bash
if [[ $# -ne 1 ]] ; then
    echo 'first argument is service, takes values from {client, server, delay}'
    exit 0
fi

curdir=$(pwd)
#cd /apps/workspace/vr-tile-enhancement/

SERVICE=${1}
#TODO: run experiment for server and client for exp=5->20

mamba activate env_tile_streaming

python simulation.py -s $SERVICE
