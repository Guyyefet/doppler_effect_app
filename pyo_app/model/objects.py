import numpy as np
from model.physics import compute_position

class StaticObject:
    def __init__(self, position):
        self.position = position

    def update(self, **kwargs):
        if 'position' in kwargs:
            from logger.objects_logger import log_static_update
            self.position = kwargs['position']

    def get_state(self):
        return self.position

class MovingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, **kwargs):
        if 'velocity' in kwargs:
            from logger.objects_logger import log_moving_update
            self.velocity = kwargs['velocity']
        
        if 'time' in kwargs:
            offset = kwargs.get('offset', np.array([0, 0]))
            self.position = compute_position(
                self.position, 
                self.velocity,
                kwargs['time'],
                offset=offset
            )

    def get_state(self):
        return self.position