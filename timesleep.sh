#!/bin/bash	

X=$(date +%s)
sleep 10
Y=$(date +%s)

echo $((Y-X))
