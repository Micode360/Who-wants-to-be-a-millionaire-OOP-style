import colorama
from colorama import Fore

def colored_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def welcome_message():
    colorama.init()
    print(Fore.BLUE + "╔" + "═" * 47 + "╗")
    print(Fore.BLUE + "║" + " " * 47 + "║")
    print(Fore.BLUE + "║" + " " * 2 + "WELCOME TO WHO WANTS TO BE A MILLIONAIRE!!!" + " " * 2 + "║")
    print(Fore.BLUE + "║" + " " * 47 + "║")
    print(Fore.BLUE + "╚" + "═" * 47 + "╝")
