from colorama import init, Fore
init()

def log_moving_update(position, velocity):
    print(
        f"{Fore.GREEN}Sound Source -> "
        f"{Fore.BLUE}Position:[{position[0]:.2f}, {position[1]:.2f}] "
        f"{Fore.YELLOW}Velocity: [{velocity[0]:.2f}, {velocity[1]:.2f}]"
        f"{Fore.RESET}"
    )