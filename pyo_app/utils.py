import numpy as np

def compute_position(initial_position, speed, duration, fps=30):
    t = np.linspace(0, duration, duration * fps)
    position = [(initial_position[0] + speed * ti, initial_position[1]) for ti in t]
    return position

# Update function for animation
def update_animation_frame(frame, moving_object, moving_object_position, static_object, static_object_position):
    moving_object.set_offsets(moving_object_position[frame])
    static_object.set_offsets(static_object_position)
    return moving_object, static_object

def reset_animation(event, speed_slider, moving_obj_x_slider, moving_obj_y_slider, static_obj_x_slider, static_obj_y_slider, duration, fps, moving_object, static_object, ani):
    # Get values from sliders
    speed = speed_slider.val
    moving_obj_x = moving_obj_x_slider.val
    moving_obj_y = moving_obj_y_slider.val
    static_obj_x = static_obj_x_slider.val
    static_obj_y = static_obj_y_slider.val

    # Compute new positions
    moving_object_initial_position = [moving_obj_x, moving_obj_y]
    moving_object_position = compute_position(moving_object_initial_position, speed, duration, fps)
    static_object_position = [static_obj_x, static_obj_y]

    # Update the animation with new positions
    ani.event_source.stop()
    ani.frame_seq = ani.new_frame_seq()
    ani._init_draw()  # Reinitialize drawing
    ani._args = (moving_object, moving_object_position, static_object, static_object_position)
    ani.event_source.start()

    return moving_object_position, static_object_position, moving_object, static_object

