'''
Thanks a ton to my buddy Aqeeb Hussain for his help with improving my original code
'''

import subprocess
import sys
import json
import os
import argparse

def usage():
	if len(sys.argv) != 2:
		print("Usage: python3 domshot.py <domain>")

def get_perms():
	if os.geteuid() != 0:
		print("Root permissions required!")

def check_installed(pkg, link):
	if len(pkg) == 0:
		print(f"{pkg} not found. Install this from: {link}")

def check_connectivity():
	# Run the ping command and capture the output
	result = subprocess.run(["ping", "8.8.8.8", "-c", "4"], capture_output=True, text=True)
	# Check if the command was successful
	if result.returncode == 0:
		# Check if there is 100% packet loss
		if "100% packet loss" in result.stdout:
			return False
		else:
			return True

def main():
	get_perms()
	parser = argparse.ArgumentParser(description='Automation script for reconnaissance purposes.')
	parser.add_argument('-d', '--domain', help='Domain to query.', required=True)
	args = parser.parse_args()

	theHarvester = subprocess.getoutput('which theHarvester')
	aquatone = subprocess.getoutput('which aquatone')
	check_installed(theHarvester, 'https://github.com/laramies/theHarvester')
	check_installed(aquatone, 'https://github.com/michenriksen/aquatone')
	conn = check_connectivity()
	if conn == True:
		pass
	elif conn == False:
		raise Exception(conn)
	

	theharvester_output_file = f"{args.domain}_theharvester.json"
	command = ["theHarvester", "-d", f"{args.domain}", "-b", "all", "-f", theharvester_output_file]
	subprocess.run(command)

	with open(theharvester_output_file, "r") as f:
		data = json.load(f)

	hosts = data.get("hosts", [])
	with open(f"{args.domain}_hosts.txt", "w") as file:
		for host in hosts:
			file.write(f"{host}\n")

	with open(f"{args.domain}_hosts.txt", 'r') as file:
		targets_content = file.read()
	

	command = ["aquatone", "-ports", "xlarge", "-out", f"{os.getcwd()}/aquatone/"]
	


	# Create a subprocess and provide targets_content as input
	process = subprocess.Popen(command, stdin=subprocess.PIPE, text=True)
	process.communicate(input=targets_content)
main()
