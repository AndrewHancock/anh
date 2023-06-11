import os
import sys
from os.path import exists, join
import click
from anh.cred import cred


@click.group()
@click.pass_context
def anh(ctx):
    cwd = os.getcwd()
    repo_dir = join(cwd, '.anh')
    if not exists(repo_dir) and not ctx.invoked_subcommand == 'init':
        print("Repo does not exist. Aborting.")
        ctx.abort()


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

anh.add_command(cred)

if __name__ == '__main__':
    anh(sys.argv[1:])
