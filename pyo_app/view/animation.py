from matplotlib.animation import FuncAnimation
from utils.constants import FPS, DURATION, INITIAL_OBJECT_POSITION
import numpy as np

def create_animation(presenter, fig, ax):
    # Create scatter plot and show initial position
    source_scatter = ax.scatter(
        INITIAL_OBJECT_POSITION[0],
        INITIAL_OBJECT_POSITION[1],
        c='red', 
        s=100, 
        label='Sound Source'
    )
    
    # Add listener reference point at origin
    ax.scatter([0], [0], c='blue', s=100, label='Listener')
    # ax.legend()

    def update_frame(frame):
        # Get updated state from presenter
        current_position = presenter.update_simulation(frame)
        
        # Only handle visualization
        source_scatter.set_offsets(current_position.reshape(1, -1))
        
        return [source_scatter]

    animation = FuncAnimation(
        fig, 
        update_frame, 
        frames=int(FPS*DURATION), 
        interval=1000/FPS, 
        repeat=False, 
        blit=True
    )
    animation.event_source.stop()

    return animation