import numpy as np
from model.physics import compute_position

class SimulationObject:
    def __init__(self, position, velocity=np.array([0.0, 0.0])):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity, dtype=float)
        self.offset = np.array([0.0, 0.0])
        self.motion_type = 'constant'

    def update(self, **kwargs):
        if 'offset' in kwargs:
            self.offset = np.array(kwargs['offset'], dtype=float)
            
        if 'velocity' in kwargs:
            self.velocity = np.array(kwargs['velocity'], dtype=float)
            
        if 'motion_type' in kwargs:
            self.motion_type = kwargs['motion_type']
            
        if 'time' in kwargs:
            self.position = compute_position(
                self.position,
                self.velocity,
                kwargs['time'],
                self.motion_type,
                self.offset
            )

    def get_state(self):
        return {
            'position': self.position,
            'velocity': self.velocity,
            'offset': self.offset,
            'motion_type': self.motion_type
        }