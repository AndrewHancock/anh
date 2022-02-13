from dataclasses import dataclass
from typing import Sequence

from anh.mil_sim.weapon import Weapon


@dataclass
class Unit:
    title: str
    sub_units: 'Unit'
    weapons: Sequence[Weapon]
