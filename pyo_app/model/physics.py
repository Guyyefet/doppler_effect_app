import numpy as np

def compute_position(position, velocity, time):
    new_position = position + velocity * time
    return new_position 