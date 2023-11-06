import subprocess
import os
import time

#Checking function installed QEMU package
def check_qemu_installed() :
    try :
        subprocess.check_output(["qemu-system-x86_64", "--version"])
        return True
    except :
        return False

def home() :
    print(" ______                     __      __ __  __")
    print("|  ____|                    \ \    / /|  \/  |")
    print("| |__     __ _  ___  _   _   \ \  / / | \  / |")
    print("|  __|   / _` |/ __|| | | |   \ \/ /  | |\/| |")
    print("| |____ | (_| |\__ \| |_| |    \  /   | |  | |")
    print("|______| \__,_||___/ \__, |     \/    |_|  |_|")
    print("                      __/ |")
    print("                     |___/")
    print("")
    print("----------------------------------------------")
    print("              Created by Schutzend")
    print("----------------------------------------------")
    print("Welcome to Easy VM. What do you want to do ?")
    print("[1] Launch a VM")
    print("[2] Create a QCOW2 disk image")
    menu_choice = input()

    if menu_choice == "1" :
       exec(open('launch_vm.py').read())
    else : 
       exec(open('create_vm.py').read())


#This script start here
if check_qemu_installed():
    #QEMU is installed. So, starting the VM launch function
    print("QEMU is installed. Starting in 5 secondes...")
    time.sleep(5)
    os.system('clear')
    home()
else :
    exec(open('qemu-install.py').read())