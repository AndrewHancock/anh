import click


@click.group()
def cred():
    pass


@cred.command()
@click.argument('id')
@click.argument('user_name')
def add(id, user_name):
    print(f"Adding credential `{id}` with user name `{user_name}")

