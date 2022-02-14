from dataclasses import fields
from enum import Enum, auto
from json import dump, load
from os import mkdir
from os.path import exists, isdir, join
from pathlib import Path
from typing import List

from pydantic import BaseModel
from rich import print
from rich.pretty import pprint
from rich.prompt import Prompt

from pydantic.dataclasses import dataclass
from anh.mil_sim.weapon import Weapon
from prompts import main_menu


def prompt_obj(cls: type):
    field_value_map = {}
    for field in cls.__fields__:
        field_value_map[field] = Prompt.ask(f'{field}')

    return field_value_map


class UnitBuilder:
    weapons = []

    def main_menu(self):
        path: Path = 'c:\\Users\\andrew\\test_data'
        self.weapons = load_data(path)

        while True:
            choice = Prompt.ask(main_menu + "\n", choices=['l', 'i', 'w', 's'])

            if choice == 'w':
                self.get_weapon()
            elif choice == 'l':
                self.list_all()
            elif choice == 's':
                save(self.weapons, path)

    def get_weapon(self):
        field_value_map = prompt_obj(Weapon)
        self.weapons.append(Weapon(**field_value_map))

    def list_all(self):
        print('Weapons:')

        for weapon in self.weapons:
            print(weapon)
        print('\n')


class Weapons(BaseModel):
    weapons: List[Weapon]


def save(weapons: List[Weapon], path: Path):
    if not exists(path):
        mkdir(path)
    elif not isdir(path):
        raise (Exception(f"{path} is not a directory."))

    with open(join(path, 'weapons.json'), 'w') as f:
        f.write(Weapons(weapons=weapons).json())


def load_data(path) -> List[Weapon]:
    weapons_path = join(path, "weapons.json")
    if not exists(weapons_path):
        return []

    return Weapons.parse_file(weapons_path).weapons



weapons = load_data('c:\\Users\\andrew\\test_data')
pprint(weapons)

