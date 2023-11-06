import subprocess
import os

os.system('clear')
print("Configure launching arguments")
#Launching arguments for the QEMU command
name = input("Virtual machine name : ")
img_directory = input("QCOW2 disk image directory : ")
cpu_cores = input("Number of processor cores : ")
ram = input("Number of GB of RAM memory : ")

#QEMU command in root
command = f"sudo qemu-system-x86_64 -name {name} -smp {cpu_cores} -m {ram}G -hda {img_directory}"
print("The command is running...")
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("QEMU command requires root permissions !! Please enter your password")

#Displaying problems if there is an error executing the command
output, error = process.communicate()
return_code = process.returncode
print(output)
print(error)
print(return_code)