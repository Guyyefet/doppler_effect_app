import numpy as np
from model.objects import MovingObject
from view.animation import create_animation
from utils.constants import FPS, INITIAL_OBJECT_POSITION, INITIAL_OBJECT_SPEED

class SimulationPresenter:
    def __init__(self, fig, ax, sliders, start_button):
        self.fig = fig
        self.ax = ax
        self.start_button = start_button
        
        # Animation state
        self.is_running = False
        self.simulation_time = 0
        self.animation = None
        
        # Map sliders
        self.slider_map = {
            'speed': sliders[0],
            'position_x': sliders[1],
            'position_y': sliders[2]
        }
        
        # Create object
        self.moving_object = MovingObject(INITIAL_OBJECT_POSITION, INITIAL_OBJECT_SPEED)
        
        # Connect UI events
        # for slider in sliders:
        #     slider.on_changed(self.on_slider_change)
        self.start_button.on_clicked(self.handle_button_click)

    def get_parameters_from_sliders(self):
        return {
            'position': np.array([
                self.slider_map['position_x'].val,
                self.slider_map['position_y'].val
            ]),
            'velocity': np.array([
                self.slider_map['speed'].val/50,
                0
            ])
        }

    def update_simulation(self, frame):
        if self.is_running:
            self.simulation_time = frame / FPS
            sliders_params = self.get_parameters_from_sliders()
            
            # Update physics
            self.moving_object.update(
                time=self.simulation_time,
                velocity=sliders_params['velocity']
            )
            
            absulote_position = self.moving_object.position + sliders_params['position']

            # Get physics state and add offset
            return absulote_position
        
        # If not running, just return current state with offset
        return self.get_parameters_from_sliders()['position']

    def initialize_simulation(self):
        self.simulation_time = 0
        self.animation = create_animation(self, self.fig, self.ax)
        # self.get_parameters_from_sliders(self)

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