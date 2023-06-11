import click
from keyring import set_password, get_password
from getpass import getpass

@click.group()
def cred():
    pass


@cred.command()
@click.argument('service_name')
@click.argument('user_name')
def add(service_name, user_name):
    password = getpass(f"Password for {user_name}[{service_name}]: ")
    set_password(service_name, user_name, password)
