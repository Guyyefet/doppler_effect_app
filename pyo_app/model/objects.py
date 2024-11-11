import numpy as np
from model.physics import compute_position

class MovingObject:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self, time, velocity):
        self.velocity = velocity
        self.position = compute_position(
            self.position,
            velocity,
            time
        )

    # def get_state(self):
    #     return {
    #         'position': self.position,
    #         'velocity': self.velocity
    #     }