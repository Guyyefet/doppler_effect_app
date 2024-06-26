import numpy as np
from pyo import *

# Initialize the server
s = Server().boot()

def doppler_siren(frequency, car_speed, observer_speed, duration, sample_rate=44100):
    # Constants
    speed_of_sound = 343.0  # Speed of sound in air in m/s

    # Time vector
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

    # Calculate Doppler-shifted frequencies
    relative_speed = car_speed - observer_speed  # m/s
    if relative_speed >= 0:
        freqs = frequency * ((speed_of_sound + observer_speed) / (speed_of_sound - car_speed))
    else:
        freqs = frequency * ((speed_of_sound - observer_speed) / (speed_of_sound + car_speed))

    # Create a frequency modulation array
    freq_mod = np.full_like(t, freqs)

    # Create a table from the frequency modulation array
    mod_table = LinTable(freq_mod.tolist())  # Convert numpy array to list

    # Create an oscillator that reads the table
    mod_freq = Osc(table=mod_table, freq=1/duration, mul=frequency)

    # Use the modulated frequency to create the final sound
    modulated_siren = Sine(freq=mod_freq, mul=0.5).out()

    # Start the server and play the sound
    s.start()
    time.sleep(duration)
    s.stop()

# Parameters
frequency = 1000  # 1kHz siren frequency
duration = 10  # 10 seconds duration
car_speed = 30 / 3.6  # Convert 30 km/h to m/s
observer_speed = 0  # Observer is stationary

doppler_siren(frequency, car_speed, observer_speed, duration)
