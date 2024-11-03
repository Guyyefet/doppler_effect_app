import numpy as np
from model.objects import SimulationObject
from view.animation import create_animation, start_animation, stop_animation
from utils.constants import FPS, DURATION

class SimulationPresenter:
    def __init__(self, fig, ax, sliders, start_button):
        self.fig = fig
        self.ax = ax
        self.sliders = sliders
        self.start_button = start_button
        self.static_obj = None
        self.moving_obj = None
        self.animation = None
        self.is_running = False
        
        self.start_button.on_clicked(self.handle_button_click)

    def initialize_simulation(self):
        self.static_obj, self.moving_obj, self.animation = create_animation(
            self.fig, self.ax, self.sliders)

    def handle_button_click(self, event):
        if not self.is_running:
            if not self.animation:
                self.initialize_simulation()
            start_animation(self.animation)
            self.start_button.label.set_text('Restart')
            self.is_running = True
        else:
            stop_animation(self.animation)
            self.initialize_simulation()
            start_animation(self.animation)
        self.fig.canvas.draw_idle()