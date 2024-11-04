# model/__init__.py
from .objects import StaticObject, MovingObject
from .physics import compute_position

# This allows:
from model import StaticObject, MovingObject  # instead of from model.objects import SimulationObject