#!/bin/bash

X=$1
Y=$2
Z=$3
factresult=

if [ $# -ne 3 ]; then
	echo "3 command line arguments needed (first 2 for add/multiply third for factorial); Not 3 command line arguments provided"
else 


function returnSum {

	sumresult=$((X + Y))
	echo "$sumresult"
}

sumval=$(returnSum)
echo $sumval

function returnProduct {

	productresult=$((X*Y))
	echo "$productresult"
}

productval=$(returnProduct)
echo $productval


function returnFactorial {
	
	if [[ $Z -lt 2 ]]; then
		echo 1 #stopping condition
	else
		echo $(( $Z * $(returnFactorial $(( $Z - 1 )))))
	fi		

}

factval=$(returnFactorial)
echo $factval


fi
