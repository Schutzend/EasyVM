import os
import subprocess
import time

print("Création de l'image disque")
img_name = input("Nom du fichier(Précisez le chemin d'accès ainsi que son nom en terminant par l'extension .qcow2 !!!)")
img_size = input("Entrez la taille en Go de la machine")

command = f"sudo qemu-img create -f qcow2 {img_name} {img_size}G"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("QEMU command requires root permissions !! Please enter your password")

#Displaying problems if there is an error executing the command
output, error = process.communicate()
return_code = process.returncode
print(output)
print(error)
print(return_code)

iso = input("For launch the OS installation, enter the Iso file directory :")

print("Launching OS Installation in 15 sec ...")
print("After install, shutdown the VM and back to the script to press Y")
time.sleep(15)

print("Launching VM...")
command = f"sudo qemu-system-x86_64 -m 2048 -hda {img_name} -cdrom {iso} -boot d"
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
print("QEMU command requires root permissions !! Please enter your password")

#Displaying problems if there is an error executing the command
output, error = process.communicate()
return_code = process.returncode
print(output)
print(error)
print(return_code)

final = input("Have you shutdown the VM ?")
if final == "Y" :
    print("you can launch the VM")
    time.sleep(3)
    os.system('clear')
    exec(open('main.py').read())

else :
    print("Error in process. Please retry")
    time.sleep(3)
    os.system('clear')
    exec(open('main.py').read())

