#!/bin/bash

two="2" # silly way to do this probably but new to bash
infile="alice.txt"
declare -a filearray
readarray filearray <$infile
numoflines=0 # 3736 lines total in alice.txt and 568 have two or more thes if I did it right 

while read line; do 

count=$(echo $line | grep -o "the" | wc -l)
if [ "$count" -ge "$two" ]; then
	echo $line
	(( numoflines++ ))
fi
done < $infile

echo $numoflines


# Probably works but ls gets randomly called every now and then during the program
# and I'm not sure why


