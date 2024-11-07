from matplotlib.animation import FuncAnimation
from utils.constants import FPS, DURATION
import numpy as np

def create_animation(fig, ax, static_obj, moving_obj, get_velocity, get_offset):
    # Create scatter plots
    static_scatter = ax.scatter(*static_obj.get_state(), c='blue', s=100, label='Static Object')
    moving_scatter = ax.scatter(*moving_obj.get_state(), c='red', s=100, label='Moving Object')

    def update_frame(frame):
        current_time = frame / FPS
        
        # Get current values from presenter
        velocity = get_velocity()
        offset = get_offset()
        
        # Update moving object with current values
        moving_obj.update(
            time=current_time,
            velocity=velocity,
            offset=offset
        )

        # Update scatter positions
        static_scatter.set_offsets([static_obj.get_state()])
        moving_scatter.set_offsets([moving_obj.get_state()])
        
        return static_scatter, moving_scatter

    animation = FuncAnimation(fig, update_frame, frames=int(FPS*DURATION), 
                            interval=1000/FPS, repeat=False, blit=True)
    animation.event_source.stop()

    return animation