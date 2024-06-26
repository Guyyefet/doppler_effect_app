import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from matplotlib.animation import FuncAnimation
from utils import compute_position, reset_animation, update_animation_frame
from constants import *

def create_gui():
    # Set up the figure and axis
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.3)
    ax.set_xlim(-600, 600)
    ax.set_ylim(-600, 600)
    ax.set_aspect('equal')
    static_object = plt.scatter(*STATIC_OBJECT_POSITION, c='blue', s=100, label='Static Object')
    moving_object = plt.scatter(*MOVING_OBJECT_POSITION, c='red', s=100, label='Moving Object')

    # Create sliders 
    speed_slider = Slider(plt.axes([0.15, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow'), 'Speed', 0.1, 2000.0, valinit=MOVING_OBJECT_SPEED)
    static_obj_x_slider = Slider(plt.axes([0.15, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow'), 'Static obj X', -600.0, 600.0, valinit=0)
    static_obj_y_slider = Slider(plt.axes([0.15, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow'), 'Static obj Y', -600.0, 600.0, valinit=0)
    moving_obj_x_slider = Slider(plt.axes([0.15, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow'), 'Moving obj X', -600.0, 600.0, valinit=-500)
    moving_obj_y_slider = Slider(plt.axes([0.15, 0.0, 0.65, 0.03], facecolor='lightgoldenrodyellow'), 'Moving obj Y', -600.0, 600.0, valinit=0)

    sliders = [speed_slider, static_obj_x_slider, static_obj_y_slider, moving_obj_x_slider, moving_obj_y_slider] 
    
    # Initialize object positions
    object_positions = compute_position(MOVING_OBJECT_POSITION, MOVING_OBJECT_SPEED, DURATION, FPS)

    # Create animation
    ani = FuncAnimation(fig, update_animation_frame, fargs=(moving_object, object_positions, static_object, STATIC_OBJECT_POSITION), frames=len(object_positions), blit=True, interval=1000/FPS)

    # Create reset button
    reset_button = Button(plt.axes([0.8, 0.5, 0.1, 0.04]), 'Restart', color='lightgoldenrodyellow', hovercolor='0.975')
    reset_button.on_clicked(lambda event: reset_animation(
        event,
        speed_slider,
        moving_obj_x_slider,
        moving_obj_y_slider,
        static_obj_x_slider,
        static_obj_y_slider,
        DURATION,
        FPS,
        moving_object,
        static_object,
        ani
    ))

    # Show the plot with animation
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    return fig, ani, moving_object, static_object, sliders, reset_button