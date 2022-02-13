from collections import Sequence
from dataclasses import dataclass

from anh.mil_sim.weapon import Weapon


@dataclass
class Individual:
    tile: str
    weapons: Sequence[Weapon]

