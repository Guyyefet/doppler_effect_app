import numpy as np
from model.objects import StaticObject, MovingObject
from view.animation import create_animation

class SimulationPresenter:
    def __init__(self, fig, ax, sliders, start_button):
        self.fig = fig
        self.ax = ax
        self.sliders = sliders
        self.start_button = start_button
        
        # Create objects with initial slider values
        self.static_obj = self.create_static_object()
        self.moving_obj = self.create_moving_object()
        self.animation = None
        
        # Connect slider events
        self.sliders[1].on_changed(self.on_static_position_change)
        self.sliders[2].on_changed(self.on_static_position_change)
        
        self.start_button.on_clicked(self.handle_button_click)

    def create_static_object(self):
        static_pos = np.array([self.sliders[1].val, self.sliders[2].val], dtype=np.float64)
        return StaticObject(static_pos)

    def create_moving_object(self):
        moving_pos = np.array([self.sliders[3].val, self.sliders[4].val], dtype=np.float64)
        velocity = np.array([self.sliders[0].val/50, 0], dtype=np.float64)
        return MovingObject(moving_pos, velocity)

    def on_static_position_change(self, val):
        pos = np.array([self.sliders[1].val, self.sliders[2].val], dtype=np.float64)
        self.static_obj.update(position=pos)
        self.fig.canvas.draw_idle()

    def get_current_velocity(self):
        return np.array([self.sliders[0].val/50, 0], dtype=np.float64)

    def get_moving_offset(self):
        return np.array([self.sliders[3].val, self.sliders[4].val], dtype=np.float64)

    def initialize_simulation(self):
        self.animation = create_animation(
            self.fig, 
            self.ax, 
            self.static_obj,
            self.moving_obj,
            self.get_current_velocity,
            self.get_moving_offset
        )

    def start_simulation(self):
        self.animation.event_source.start()

    def stop_simulation(self):
        self.animation.event_source.stop()

    def handle_button_click(self, event):
        if not self.animation:
            self.initialize_simulation()

        if not self.animation.event_source._interval == 0:
            self.start_simulation()
            self.start_button.label.set_text('Restart')
        else:
            self.stop_simulation()
            self.initialize_simulation()
            self.start_simulation()
        self.fig.canvas.draw_idle()