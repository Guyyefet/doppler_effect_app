import numpy as np

class SimulationObject:
    def __init__(self, position, speed=0):
        self.position = position  # Assuming position is already a numpy array
        self.speed = speed

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        
        if 'time' in kwargs and self.speed != 0:
            self.position[0] += self.speed * kwargs['time']

    def get_state(self):
        return {
            'position': self.position,
            'speed': self.speed
        }