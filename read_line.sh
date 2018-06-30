#!./read_line.sh

infile="alice.txt"
while read line;do 

count=$(echo $line | grep -o "the" | wc -l)
if [$count -gt 1];then
	echo $line
else
	echo "NAH BRAH"
fi
done < $infile


