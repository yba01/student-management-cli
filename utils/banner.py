import os
import time
import shutil


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def smooth(listes):
    for text in listes:
        print(text)
        time.sleep(0.2)

def center(text):
    largeur = shutil.get_terminal_size().columns
    return "\n".join(ligne.center(largeur) for ligne in text.splitlines())


def afficher_banner():

    banner = r"""
███████╗████████╗██╗   ██╗██████╗ ███████╗███╗   ██╗████████╗
██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝████╗  ██║╚══██╔══╝
███████╗   ██║   ██║   ██║██║  ██║█████╗  ██╔██╗ ██║   ██║   
╚════██║   ██║   ██║   ██║██║  ██║██╔══╝  ██║╚██╗██║   ██║   
███████║   ██║   ╚██████╔╝██████╔╝███████╗██║ ╚████║   ██║   
╚══════╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝   ╚═╝   

███╗   ███╗ █████╗ ███╗   ██╗ █████╗  ██████╗ ███████╗██████╗ 
████╗ ████║██╔══██╗████╗  ██║██╔══██╗██╔════╝ ██╔════╝██╔══██╗
██╔████╔██║███████║██╔██╗ ██║███████║██║  ███╗█████╗  ██████╔╝
██║╚██╔╝██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║██║ ╚████║██║  ██║╚██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

    # Couleur cyan ANSI
    cyan = "\033[96m"
    reset = "\033[0m"

    clear()

    # Animation loading
    loading = "Loading Student Management CLI"
    for i in range(4):
        print(center(f"{cyan}{loading}{'.' * i}{reset}"))
        time.sleep(0.7)
        clear()

    # Apparition ligne par ligne
    for ligne in banner.splitlines():
        print(center(f"{cyan}{ligne}{reset}"))
        time.sleep(0.03)

    print("\n")
    print(center("Welcome to Student Management CLI"))
    print(center("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"))
    time.sleep(0.2)