#!/bin/bash

if [ $# -ne 2 ]; then

	echo "2 arguments needed; Not 2 arguments supplied"
	exit	

else

	X=$1
	Y=$2
	echo $((X*Y))
fi

