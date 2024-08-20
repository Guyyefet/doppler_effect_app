from objects2 import SimulationObject
from constants import FPS, DURATION
import numpy as np

class SimulationController:
    def __init__(self):
        self.objects = []
        self.is_running = False
        self.current_time = 0

    def create_object(self, position, speed=0):
        obj = SimulationObject(np.array(position, dtype=float), speed)
        self.objects.append(obj)
        return len(self.objects) - 1  # Return object ID

    def update(self, dt):
        if self.is_running:
            self.current_time += dt
            for obj in self.objects:
                obj.update(time=dt)

    def start_simulation(self):
        self.is_running = True

    def stop_simulation(self):
        self.is_running = False

    def reset_simulation(self):
        self.current_time = 0
        self.is_running = False

    def update_object(self, object_id, **kwargs):
        if 0 <= object_id < len(self.objects):
            self.objects[object_id].update(**kwargs)

    def get_object_states(self):
        return [obj.get_state() for obj in self.objects]

def create_simulation_controller():
    return SimulationController()