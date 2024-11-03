import numpy as np

def compute_position(position, velocity, time, motion_type='constant', offset=np.array([0.0, 0.0])):
    """
    Calculate position based on specified motion type and offset.
    Args:
        position: numpy array [x, y] - current position
        velocity: numpy array [vx, vy] - velocity vector
        time: float - time delta since last update
        motion_type: string - type of motion calculation to use
        offset: numpy array [x, y] - position offset from sliders
    Returns:
        numpy array of new position [x, y]
    """
    position = np.array(position, dtype=np.float64)
    velocity = np.array(velocity, dtype=np.float64)
    offset = np.array(offset, dtype=np.float64)
    time = float(time)

    # Calculate base position according to motion type
    if motion_type == 'constant':
        new_position = position + velocity * time
    elif motion_type == 'accelerating':
        # Example: constant acceleration
        acceleration = velocity  # Using velocity as acceleration for example
        new_position = position + velocity * time + 0.5 * acceleration * time * time
    else:
        raise ValueError(f"Unknown motion type: {motion_type}")

    # Add offset to final position
    return new_position + offset