import numpy as np
from model.physics import compute_position

class StaticObject:
    def __init__(self, position):
        self.position = position

    def update(self, position):
        self.position = position
        from logger.objects_logger import log_static_update
            

    def get_state(self):
        return self.position

class MovingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, time, velocity, offset=np.array([0, 0])):
        self.velocity = velocity
        self.position = compute_position(
            self.position,
            self.velocity,
            time,
            offset=offset
        )

    def get_state(self):
        return {
            'position': self.position,
            'velocity': self.velocity
        }