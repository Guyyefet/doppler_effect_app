from colorama import init, Fore
init()

def log_slider_change(slider_name, val):
    print(f"{Fore.RED}Slider Change - {slider_name}: {val} {Fore.RESET}")