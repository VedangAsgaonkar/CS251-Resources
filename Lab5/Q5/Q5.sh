#!/bin/bash

awk '{ sub("\r$", ""); print }' sample.txt > unix.txt

awk '
BEGIN{}
FILENAME == "covid_status.html" && /State Name:&nbsp/ {
	split($0 , randomdata , "even\">")
	split(randomdata[2], state_name , "</div>")
	split(randomdata[3], total_case , "</div>")
	state[state_name[1]]=total_case[1]
}

END{
	for(i in state){
		print state[i] "," i 
	}
}
' covid_status.html > output1.txt

awk '
BEGIN{}
FILENAME=="output1.txt"{
	state[$2]=$1
}
FILENAME=="unix.txt"{
	print state[$1] " ," $1
}
' FS="," output1.txt unix.txt | sort -k1n | awk -F " ," '{print $2 " " $1}' > output.txt

rm unix.txt
rm output1.txt