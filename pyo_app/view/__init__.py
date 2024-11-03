# view/__init__.py
from .gui import create_gui, get_slider_values
from .animation import create_animation

# This allows:
from view import create_gui  # cleaner imports in main.py