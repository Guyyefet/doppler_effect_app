# model/__init__.py
from .objects import MovingObject
from .physics import compute_position

# This allows:
from model import MovingObject  # instead of from model.objects import SimulationObject