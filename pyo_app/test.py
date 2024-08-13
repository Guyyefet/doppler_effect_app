import matplotlib.pyplot as plt
from gui2 import create_gui
from animation2 import create_animation

a = 2

if __name__ == "__main__":
    fig, ax, sliders, start_button = create_gui()
    static_obj, moving_obj, animation = create_animation(fig, ax, sliders)
    plt.show()