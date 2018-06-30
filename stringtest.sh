#!./stringtest.sh


stringuno=$1
stringdos=$2
cargs=$#
if [$cargs -ne 2]; then
	echo "ERROR EROOR EEEROOORRROROR"
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


	
	
	
