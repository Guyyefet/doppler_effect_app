from model.physics import compute_position, calculate_doppler_shift
from utils.constants import BASE_FREQUENCY, OBSORVER_POSITION, BASE_FREQUENCY, SPEED_OF_SOUND
from logger import log_moving_update

class Source:
    def __init__(self, position, velocity):  
        self.position = position
        self.velocity = velocity
        # self.base_frequency = BASE_FREQUENCY
        # self.current_frequency = base_frequency

    def update(self, velocity):
        self.velocity = velocity
        self.position = compute_position(
            self.position,
            velocity
        )
        
        # Calculate the Doppler shifted frequency
        self.current_frequency = calculate_doppler_shift(
            self.position,
            self.velocity
        )

        log_moving_update(self.position, self.velocity)

