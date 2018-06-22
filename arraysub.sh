#!./arraysub.sh

quoteone="You cannot shake hands with a clenched fist."
quotetwo="Whoever is happy will make others happy too."
quotethree="Let us be grateful to people who make us happy."
quotefour="Very little is needed to make a happy life."
quotefive="Be happy for this moment. This moment is your life."

QARRAY=("$quoteone", "$quotetwo", "$quotethree", "$quotefour", "$quotefive")

# this for loop made sense to me but bash was not a fan
#for i in "${QARRAY[@]}"
#do 
#	echo ${i//happy/sloppy}

echo ${QARRAY[*]//happy/sloppy}
unset QARRAY
