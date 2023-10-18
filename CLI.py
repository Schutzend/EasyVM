import subprocess
import os

def check_qemu_installed():
    try :
        subprocess.check_output(["qemu-system-x86_64", "--version"])
        return True
    except :
        return False

if check_qemu_installed():
    print("Le paquet QEMU est installé")
else :
    print("Le paquet QEMU n'est pas installé")

input()