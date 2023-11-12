#!/bin/bash
if [[ $# -le 1 ]] ; then
    echo 'first argument is service, takes values from {client, server, delay}, second argument is sim mode, takes values from {new-run, continue}'
    echo $#
    exit 0
fi

if [[ $# -gt 3 ]] ; then
    echo 'first argument is service, takes values from {client, server, delay}, second argument is sim mode, takes values from {new-run, continue}'
    echo $#
    exit 0
fi

curdir=$(pwd)
#cd /apps/workspace/vr-tile-enhancement/

SERVICE=${1}
SIMMODE=${2}
#TODO: run experiment for server and client for exp=5->20

mamba activate env_tile_streaming

python simulation.py -s $SERVICE -m $SIMMODE
