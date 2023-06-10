import os
from os.path import exists, join
import click


@click.group()
def anh():
    print("Anh")


@anh.command()
def init():
    cwd = os.getcwd()
    repo_dir = join(cwd, '.anh')
    if exists(repo_dir):
        print(".anh directory already exists.")
    else:
        os.mkdir(repo_dir)
        print(".anh directory created.")

@anh.command()
def test():
    print("Hello!")
