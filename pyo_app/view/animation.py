from matplotlib.animation import FuncAnimation
from model.objects import StaticObject, MovingObject
from utils.constants import FPS, DURATION
import numpy as np

def create_animation(fig, ax, sliders):
    # Get initial positions from sliders
    static_pos = np.array([sliders[1].val, sliders[2].val], dtype=np.float64)
    moving_pos = np.array([sliders[3].val, sliders[4].val], dtype=np.float64)
    velocity = np.array([sliders[0].val, 0], dtype=np.float64)
    
    static_obj = StaticObject(static_pos)
    moving_obj = MovingObject(moving_pos, velocity)

    # Create scatter plots once
    static_scatter = ax.scatter([], [], c='blue', s=100, label='Static Object')
    moving_scatter = ax.scatter([], [], c='red', s=100, label='Moving Object')

    def update_frame(frame):
        current_time = frame / FPS
        
        # Get current values from sliders
        static_pos = np.array([sliders[1].val, sliders[2].val], dtype=np.float64)
        offset = np.array([sliders[3].val, sliders[4].val], dtype=np.float64)
        velocity = np.array([sliders[0].val, 0], dtype=np.float64)

        # Update objects with current values
        static_obj.update(position=static_pos)
        moving_obj.update(time=current_time, velocity=velocity, offset=offset)

        static_scatter.set_offsets(static_obj.get_state()[np.newaxis])
        moving_scatter.set_offsets(moving_obj.get_state()[np.newaxis])
        
        return static_scatter, moving_scatter

    animation = FuncAnimation(fig, update_frame, frames=int(FPS*DURATION), 
                            interval=1000/FPS, repeat=False, blit=True)
    animation.event_source.stop()

    return static_obj, moving_obj, animation

def start_animation(animation):
    animation.event_source.start()

def stop_animation(animation):
    animation.event_source.stop()