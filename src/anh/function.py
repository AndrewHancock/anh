from typing import Callable
import inspect


def add(x: int, y: int):
    """A function to add stuff.
    :param x: A number, x
    :param y: A number, y
    :return: A number, x + y
    """
    return x + y


def print_function(fun: Callable):
    print(f'{ fun.__name__}{inspect.signature(fun)}')
    print(f'{str(fun.__doc__).splitlines()[0]}')

print_function(add)