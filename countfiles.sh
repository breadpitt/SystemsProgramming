#!/bin/bash

count=0;
lsoutput=$(ls);
for i in [$lsoutput];
	do (( count++ ));
done
echo $count
if [ $count -gt 10 ]; then
	echo "More than 10 files"
elif [ $count -e 10 ]; then
	echo "Exactly 10 files"
else
	echo " Less that 10 files"
fi

#echo $lsoutput
