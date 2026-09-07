import os
import subprocess

# Run the ls command using os
os.system("ls")

# Display detailed information about SystemAdmin.py
subprocess.run(["ls", "-l", "SystemAdmin.py"])

command = "uname"
commandArgument = "-a"

print(f"Gathering system information with command: {command} {commandArgument}")

subprocess.run([command, commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])