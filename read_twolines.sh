#!./read_twolines.sh

{
	read firstline
	read secondline
	read thirdline	
} <$"alice.txt"

echo $firstline
echo $secondline
echo $thirdline


