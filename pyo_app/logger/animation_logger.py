from colorama import init, Fore
init()

def log_slider_change(slider_name, val):
    if "static" in slider_name.lower():
        print(f"{Fore.BLUE}Slider Change - {slider_name}: {val} {Fore.RESET}")
    elif "moving" in slider_name.lower() or "speed" in slider_name.lower():
        print(f"{Fore.RED}Slider Change - {slider_name}: {val} {Fore.RESET}")