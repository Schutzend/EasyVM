import subprocess
import os
import sys

#Checking function installed QEMU package
def check_qemu_installed():
    try :
        subprocess.check_output(["qemu-system-x86_64", "--version"])
        return True
    except :
        return False

#Launching function for the QEMU virtual machine
def vm_launch():
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

#This script start here
os.system('clear')
if check_qemu_installed():
    #QEMU is installed. So, starting the VM launch function
    vm_launch()
else :
    print("The QEMU package is not installed")
    print("The installation guide is here : https://www.qemu.org/download/ ")
        
    is_installed = input("One the installation finished, press the key [Y]: ")

    if is_installed == str("Y"):
        #Clear the Terminal et restart python script
        os.system('clear')
        os.execv(sys.executable, [sys.executable] + sys.argv)