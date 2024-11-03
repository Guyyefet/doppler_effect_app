from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from model.objects import SimulationObject
from utils.constants import FPS, DURATION
import numpy as np

def create_animation(fig, ax, sliders):
    # Extract values from sliders
    speed = sliders[0].val
    static_x, static_y = sliders[1].val, sliders[2].val
    moving_x, moving_y = sliders[3].val, sliders[4].val

    static_obj = SimulationObject(np.array([static_x, static_y]))
    moving_obj = SimulationObject(np.array([moving_x, moving_y]), np.array([speed, 0]))

    last_frame_time = 0

    def update_frame(frame):
        nonlocal last_frame_time
        current_time = frame / FPS
        dt = current_time - last_frame_time  # Time since last frame
        last_frame_time = current_time

        moving_obj.update(time=dt)  # Pass time delta instead of total time

        # Clear only the artists, not the entire axis
        for artist in ax.collections + ax.lines:
            artist.remove()

        # Plot the objects
        ax.scatter(*static_obj.position, c='blue', s=100, label='Static Object')
        ax.scatter(*moving_obj.position, c='red', s=100, label='Moving Object')
        
        return ax.collections

    animation = FuncAnimation(fig, update_frame, frames=int(FPS*DURATION), 
                            interval=1000/FPS, repeat=False, blit=True)
    animation.event_source.stop()

    return static_obj, moving_obj, animation

def start_animation(animation):
    animation.event_source.start()

def stop_animation(animation):
    animation.event_source.stop()