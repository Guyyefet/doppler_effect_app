from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from objects2 import SimulationObject
from constants import FPS, DURATION
import numpy as np

def create_animation(fig, ax, sliders):
    # Extract values from sliders
    speed = sliders[0].val
    static_x, static_y = sliders[1].val, sliders[2].val
    moving_x, moving_y = sliders[3].val, sliders[4].val

    static_obj = SimulationObject(np.array([static_x, static_y]))
    moving_obj = SimulationObject(np.array([moving_x, moving_y]), speed)

    objects = [static_obj, moving_obj]

    def update_frame(frame):
        current_time = frame / FPS
        
        # Update object positions
        for obj in objects:
            obj.update(time=current_time)

        # Clear only the artists, not the entire axis
        for artist in ax.collections + ax.lines:
            artist.remove()

        # Plot objects
        for obj in objects:
            state = obj.get_state()
            ax.scatter(*state['position'], c='blue' if state['speed'] == 0 else 'red', s=100)

        return ax.collections

    animation = FuncAnimation(fig, update_frame, frames=int(FPS*DURATION), interval=1000/FPS, repeat=False, blit=True)
    
    return static_obj, moving_obj, animation

def start_animation(animation):
    animation.event_source.start()

def stop_animation(animation):
    animation.event_source.stop()