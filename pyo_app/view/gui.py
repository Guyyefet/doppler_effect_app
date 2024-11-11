import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

def create_slider(ax, label, valmin, valmax, valinit):
    return Slider(ax, label, valmin, valmax, valinit=valinit, color='lightblue')

def create_gui():
    # Set up the figure and axis
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.3)
    ax.set_xlim(-600, 600)
    ax.set_ylim(-600, 600)
    ax.set_aspect('equal')
    
    # Create a blank grid
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])

    # Slider parameters
    slider_params = [
        ('Speed', 0.1, 2000.0, 500),
        ('Source X', -600.0, 600.0, -500),
        ('Source Y', -600.0, 600.0, 0)
    ]

    # Create sliders
    sliders = []
    for i, (label, valmin, valmax, valinit) in enumerate(slider_params):
        ax_pos = [0.15, 0.2 - i*0.05, 0.65, 0.03]
        slider = create_slider(plt.axes(ax_pos), label, valmin, valmax, valinit)
        sliders.append(slider)

    # Create start button
    start_button = Button(plt.axes([0.8, 0.5, 0.1, 0.04]), 'Start', 
                         color='lightgoldenrodyellow', hovercolor='0.975')

    return fig, ax, sliders, start_button

def get_slider_values(sliders):
    return [slider.val for slider in sliders]