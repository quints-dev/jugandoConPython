import os
import subprocess

#os.system("ls")
#os.system("ls -l")
#subprocess.run(["ls"])
#subprocess.run(["ls","-l"])
#subprocess.run(["ls","-l","README.md"])

"""command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])"""

command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])