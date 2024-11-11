from colorama import init, Fore
init()

def log_moving_update(type_update, old_val, new_val):
    print(f"{Fore.RED}Sound Source {type_update}: {old_val} -> {new_val}{Fore.RESET}")