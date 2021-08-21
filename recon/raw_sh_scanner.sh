#!/bin/sh 

################### DESCRIPTION #########################################
# Raw bash port scanner leveraging /dev/tcp, created by Mattia Campagnano
# (The_S@vvy_G33k) on Wed 11 Aug 2021 08:08:56 AM EDT

# Originally published by Mattia Campagnano as LOTL_scanner.sh (https://github.com/matticamp/LOTL_scanner/blob/main/LOTL_scanner.sh)
# It will read in a list of IP addresses from a user-provided text file
# and will use /dev/tcp to scan ports 1 thru 65,535 for each target IPs.

#########################################################################
IP_list=$1


if [ $# -ne 1 ]
	then
		echo "Not enough arguments supplied. Usage: ./raw_sh_scanner.sh <IP list>" && exit 1
fi

#Creating a variable storing the value of the IP_list variable (the file path)
base=$(echo $IP_list)

# Loop through all ports
for port in {1..65535}; do          

# Loop through all IP addresses stored in the file whose path is stored in the base variable
	for ip in $(cat $base);	do 
	
# For each IP address, connect to all 65,535 ports, discard errors and indicate
# which port is open for which IP

		timeout 1 bash -c "echo >/dev/tcp/$ip/$port" 2>/dev/null &&
        echo "port $port is open for $ip"
	done	
done

# Print "done" on screen when scan is completed.
echo "Done"

