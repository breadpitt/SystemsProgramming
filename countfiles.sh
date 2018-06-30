#!/bin/bash

count=0;
lsoutput=$(ls);
for i in [$lsoutput];
	do (( count++ ));
done
echo $count
#echo $lsoutput
