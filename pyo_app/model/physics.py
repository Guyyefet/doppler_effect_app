from utils.constants import SPEED_OF_SOUND, BASE_FREQUENCY, OBSORVER_POSITION, FPS
import numpy as np

def compute_position(position, velocity):
    # Use a fixed time step (delta time) based on FPS
    dt = 1.0 / FPS
    new_position = position + velocity * dt
    return new_position

def calculate_doppler_shift(source_position, source_velocity):
    direction = OBSORVER_POSITION - source_position
    distance = np.linalg.norm(direction)
    
    if distance == 0:
        return BASE_FREQUENCY
    
    direction = direction / distance
    
    radial_velocity = np.dot(source_velocity, direction)
    
    observed_frequency = BASE_FREQUENCY * (SPEED_OF_SOUND / (SPEED_OF_SOUND - radial_velocity))
    
    return observed_frequency
