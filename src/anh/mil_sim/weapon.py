from pydantic import BaseModel


class Weapon(BaseModel):
    name: str
    range: int
    damage: int
    penetration: int

