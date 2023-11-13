# Forked by noobcoderwastaken

import os
from colorama import Fore
import subprocess

print(Fore.GREEN + "[+] Welcome to Gshell\n")

current_directory = os.getcwd()

while True:
    user_input = input(Fore.RED + f"{current_directory}>")

    if user_input.startswith("cd "):
        directory = user_input[3:]
        try:
            os.chdir(directory)
            current_directory = os.getcwd()
        except FileNotFoundError:
            print(f"Directory not found: {directory}")

    elif user_input.lower() == "exit":
        break
    else:
        try:
            subprocess.run(user_input, shell=True)
        except Exception as e:
            print(f"Error: {e}")