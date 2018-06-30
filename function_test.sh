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
	
	if [ "$Z" -eq "1" ]; then
		echo 1 #stopping condition
		return
	fi	
		a='expr $Z - 1'
		b=$(returnFactorial $a)
		echo $(($Z * $b))

}

echo "$(returnFactorial $Z)"
#factval=$(returnFactorial)
#echo $factval

#echo $(returnFactorial)


fi
