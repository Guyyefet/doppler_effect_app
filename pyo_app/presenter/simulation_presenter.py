import numpy as np
from model.objects import Source
from view.animation import create_animation
from utils.constants import FPS, INITIAL_SOURCE_POSITION, INITIAL_SOURCE_SPEED

class SimulationPresenter:
    def __init__(self, fig, ax, sliders, start_button):
        self.fig = fig
        self.ax = ax
        self.start_button = start_button
        
        # Animation state
        self.is_running = False
        self.simulation_time = np.float32(0)
        self.animation = None
        
        # Map sliders
        self.slider_map = {
            'speed': sliders[0],
            'position_x': sliders[1],
            'position_y': sliders[2]
        }
        
        # Create object
        self.source = Source(INITIAL_SOURCE_POSITION, INITIAL_SOURCE_SPEED)
        
        # Connect UI events
        self.start_button.on_clicked(self.handle_button_click)

    def get_parameters_from_sliders(self):
        return {
            'position': np.array([
                self.slider_map['position_x'].val,
                self.slider_map['position_y'].val
            ], dtype=np.float32),
            'velocity': np.array([
                self.slider_map['speed'].val,
                0
            ], dtype=np.float32)
        }

    def update_simulation(self, frame):
        if self.is_running:
            sliders_params = self.get_parameters_from_sliders()         
            self.source.update(
                velocity=sliders_params['velocity']
            )
            
            absolute_position = self.source.position + sliders_params['position']
            return absolute_position
        
        return self.get_parameters_from_sliders()['position']

    def initialize_simulation(self):
        self.simulation_time = 0
        self.source = Source(INITIAL_SOURCE_POSITION, INITIAL_SOURCE_SPEED)  # Reset source object
        self.animation = create_animation(self, self.fig, self.ax)

    def start_simulation(self):
        self.is_running = True
        self.animation.event_source.start()

    def stop_simulation(self):
        self.is_running = False
        self.animation.event_source.stop()

    def handle_button_click(self, event):
        if not self.animation:
            self.initialize_simulation()

        if not self.is_running:
            self.start_simulation()
            self.start_button.label.set_text('Restart')
        else:
            self.stop_simulation()
            self.initialize_simulation()
            self.start_simulation()
