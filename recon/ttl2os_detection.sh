#!/bin/bash

echo "############################# OS DETECTION SCRIPT #############################"

echo "TTL-based OS detection bash script created by Mattia Campagnano (The S@vvy_G33k)"

echo

# TTL-based OS detection bash script created by Mattia Campagnano (The S@vvy_G33k) on Tue 24 Aug 2021 05:17:55 PM EDT
# Arguments: 

# a) Argument 1: list of iP addresses to check
# b) Argument 2: output file 

file=$1 
output=$2

if [ $# -ne 2 ]
	then
		echo "Not enough arguments supplied. Usage: ./os_ttl_detection.sh <IP list> <output file>" && exit 1
fi
x=$(cat $file)

#Loop through IP addresses

for ip in $(echo $x)
do

# Extract TTL value from ping command output and store it to a variable.


        ttl=$(ping -c1 $ip | grep "ttl=" | awk -F":" '{print $2}' | awk '{print $2}' | sed 's/ttl=/ /g')

# Echo statement for debugging purposes

        #echo $ttl


# Based on the value of the TTL variable, determine what OS is presumably running on each target hosts. 


        if [[ "$ttl" -lt 65 ]]
        then
                echo "$ip runs Linux" >> "$output"

        elif [[ "$ttl" -gt 64 ]] && [[ "$ttl" -le 128 ]]
        then
                echo "$ip runs Windows" >> "$output"
	
	elif [[ "$ttl" -gt 250 ]] && [[ "$ttl" -le 255 ]]
        then
        
                echo "$ip runs Cisco" >> "$output"
        
     

	   fi
done
