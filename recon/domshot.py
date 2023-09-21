import subprocess
import sys
import json
import os

if os.geteuid() != 0:
    print("This script must be run as root")
    sys.exit(1)

domain = sys.argv[1]
if len(sys.argv) < 2:
   print("Usage: python3 domshot.py <domain>")
else:
   pass

theHarvester = subprocess.getoutput('which theHarvester')
if len(theHarvester) == 0:
    print("theHarvester not found, please install it from https://github.com/laramies/theHarvester")
else:
    pass

aquatone = subprocess.getoutput('which aquatone')
if len(aquatone) == 0:
    print("Aquatone not found, please install it from https://github.com/michenriksen/aquatone")
else:
    pass

# Run the ping command and capture the output
result = subprocess.run(["ping", "8.8.8.8", "-c", "4"], capture_output=True, text=True)

# Check if the command was successful
if result.returncode == 0:
    # Check if there is 100% packet loss
    if "100% packet loss" in result.stdout:
        print("You have no connectivity")
    else:
        print("You are connected to the Internet")
else:
    print(f"Error executing command: {result.stderr}")

theharvester_output_file = f"{domain}_theharvester.json"
command = ["theHarvester", "-d", domain, "-b", "all", "-f", theharvester_output_file]
subprocess.run(command)

with open(theharvester_output_file, "r") as f:
    data = json.load(f)

hosts = data.get("hosts", [])
with open(f"{domain}_hosts.txt", "w") as file:
    for host in hosts:
        file.write(f"{host}\n")

with open(f"{domain}_hosts.txt", 'r') as file:
    targets_content = file.read()

command = ['aquatone', '-ports', 'xlarge', '-out', f'{os.getcwd()}/aquatone/']

# Create a subprocess and provide targets_content as input
process = subprocess.Popen(command, stdin=subprocess.PIPE, text=True)
process.communicate(input=targets_content)
