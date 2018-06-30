#!/bin/bash

$(sleep 10) &

PID=$!
echo "Sleepy sleep time"
sleep 5

$(kill $PID)
