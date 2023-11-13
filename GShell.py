import os
from colorama import Fore

commands = { 
    'help': 'helps you with the commands',
    'quit': 'close the terminal',
    'credits': 'the guy who made the terminal',
    'mkf': 'create a new file',
    'cd': 'change the current directory',
    'cdreset': 'reset the current directory to script location'
}

credits = "This shell was made by scarry(_scarry_ on discord)."

print(Fore.GREEN + "Welcome to Gshellh, Type help to get started")

exit_terminal = False
current_directory = os.getcwd()

while not exit_terminal:
    user_input = input(Fore.GREEN + f"{current_directory}>")

    if user_input == "help":
        print(Fore.BLUE + f"[+] {commands}\n")

    elif user_input == "quit":
        exit_terminal = True

    elif user_input == "credits":    
        print(Fore.BLUE + f"[+] {credits}\n")

    elif user_input.startswith("mkf"):
        file_name = user_input[4:]
        
        file_path = os.path.join(current_directory, file_name)
        
        try:
            with open(file_path, 'w') as file:
                print(Fore.BLUE + f"[+] File '{file_name}' created successfully.\n")
        except Exception as e:
            print(Fore.RED + f"[-] Error creating file '{file_name}': {str(e)}\n")

    elif user_input.startswith("cd "):
        new_directory = user_input[3:]
        
        try:
            os.chdir(new_directory)
            current_directory = os.getcwd()
            print(Fore.BLUE + f"[+] Current directory changed to '{current_directory}'\n")
        except Exception as e:
            print(Fore.RED + f"[-] Error changing directory to '{new_directory}': {str(e)}\n")

    elif user_input == "cdreset":
        script_directory = os.path.dirname(__file__)
        os.chdir(script_directory)
        current_directory = os.getcwd()
        print(Fore.BLUE + f"[+] Current directory reset to script location '{current_directory}'\n")

    else:
        print(Fore.RED + "[-] Invalid command. Type 'help' for a list of commands.\n")
