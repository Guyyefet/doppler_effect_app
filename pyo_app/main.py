import time
import matplotlib.pyplot as plt
from audio import start_pyo_server
from gui import create_gui

if __name__ == "__main__":
    fig, ani, moving_object, static_object, sliders, reset_button = create_gui()
    plt.show()
    start_pyo_server.start()