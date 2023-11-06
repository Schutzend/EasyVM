import subprocess
import os

print("The QEMU package is not installed") 
qemu_request = input("Do you want install QEMU ? [Y/N]")
if qemu_request == str("Y") :
    print("After install, please restart script")
    print("What's your system ? :")
    print("[1] : Debian")
    print("[2] : Arch")
    os_choice = input("Select your OS : ")

    if os_choice == "1" :
        #QEMU installation for Debian
        command = "sudo apt install qemu-system"
        try :
            print("The QEMU installation requires root permissions !! Please enter your password")
            subprocess.check_call(command, shell=True)
        except subprocess.CalledProcessError as e :
            print("Can't install QEMU. Please do it manually")
            print(f"Error : {e}")

        os.system("clear")
        print("Installation finished")
        exec(open('main.py').read())

    if os_choice == "2":
        #QEMU installation for Arch
        command = "sudo pacman -S qemu-full"
        try :
            print("The QEMU installation requires root permissions !! Please enter your password")
            subprocess.check_call(command, shell=True)
        except subprocess.CalledProcessError as e :
            print("Can't install QEMU. Please do it manually")
            print(f"Error : {e}")
            
        os.system("clear")
        print("Installation finished")
        exec(open('main.py').read())