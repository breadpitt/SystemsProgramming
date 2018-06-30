#!/bin/bash
stringuno=$1
stringdos=$2

if [ $# -ne 2 ]; then

	echo "2 arguments needed; Not 2 arguments supplied"
	exit	

elif [[ "$stringuno" == "$stringdos" ]]; then
	echo "EQUAL"

elif [[ "$stringuno" < "$stringdos" ]]; then
	echo "$stringuno"
	echo "$stringdos"

else 
	echo "$stringdos"
	echo "$stringuno"
fi


	
	
	
