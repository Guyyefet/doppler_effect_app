# model/__init__.py
from .objects import SimulationObject
from .physics import compute_position

# This allows:
from model import SimulationObject  # instead of from model.objects import SimulationObject