from enum import Enum, auto
from typing import Sequence

from rich.text import Text
from rich.prompt import Prompt
from rich import print

from anh.mil_sim.weapon import Weapon
from prompts import main_menu

class BuilderState(Enum):
    MAIN_MENU = auto(),
    ADD_INDV = auto(),
    ADD_WEAPON = auto()


class UnitBuilder:
    state: BuilderState = BuilderState.MAIN_MENU
    weapons = []

    def main_menu(self):

        while True:
            choice = Prompt.ask(main_menu, choices=['l', 'i', 'w'])

            if choice == 'w':
                self.get_weapon()
            elif choice == 'l':
                self.list_all()

    def get_weapon(self):
        name = Prompt.ask('Name? ')

        self.weapons.append(Weapon(name=name))

    def list_all(self):
        print('Weapons:')

        for weapon in self.weapons:
            print(f'\t{weapon.name}')
        print('\n\n')


UnitBuilder().main_menu()
