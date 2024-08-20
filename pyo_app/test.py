import matplotlib.pyplot as plt
from gui2 import create_gui
from animation2 import create_animation, start_animation, stop_animation

# def create_button_handler(animation, button):
#     is_running = False

#     def on_button_click(event):
#         nonlocal is_running
#         if is_running:
#             stop_animation(animation)
#             button.label.set_text('Start')
#             is_running = False
#         else:
#             start_animation(animation)
#             button.label.set_text('Stop')
#             is_running = True

#     return on_button_click

if __name__ == "__main__":
    fig, ax, sliders, start_button = create_gui()
    static_obj, moving_obj, animation = create_animation(fig, ax, sliders)
    
    # on_button_click = create_button_handler(animation, start_button)
    # start_button.on_clicked(on_button_click)
    
    plt.show()