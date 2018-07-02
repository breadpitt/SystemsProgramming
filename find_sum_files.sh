#!/bin/bash

filetype=$1
count=0

function findfiles {
	foundoutput=$(find $2 -name "*$1" -type f)
	echo $foundoutput
}

#findoutput=$(find $2 -name "*$1" -type f )

if [ $# -ne 2 ]; then

	echo "2 arguments needed; Not 2 arguments supplied"
	exit	
elif [ -d $2 ]; then

	echo "That's a directory"
	#	foundfiles=$(findoutput)
	foundfiles=$(findfiles)
	for i in [$foundfiles];
		do (( count++ ));
		echo $foundfiles
	done

else
	echo "Argument 2 is not a valid directory"

fi
echo $count
