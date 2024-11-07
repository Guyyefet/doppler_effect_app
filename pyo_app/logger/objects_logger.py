from colorama import init, Fore
init()

def log_static_update(old_pos, new_pos):
    print(f"{Fore.BLUE}Static Object Position: {old_pos} -> {new_pos}{Fore.RESET}")

def log_moving_update(type_update, old_val, new_val):
    print(f"{Fore.RED}Moving Object {type_update}: {old_val} -> {new_val}{Fore.RESET}")