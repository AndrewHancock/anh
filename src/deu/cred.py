import click
from keyring import set_password, get_password
from getpass import getpass
from os.path import join, exists
from os import mkdir

from pydantic import BaseModel

from deu.repo import Repo
from deu.repo import pass_repo


class CredEntry(BaseModel):
    key: str
    user_name: str


class CredRepo(BaseModel):
    cred_entries: list[CredEntry]


_cred_repo = None
@click.group()
@pass_repo
def cred(repo):
    global _cred_repo
    _cred_repo = read_cred_repo(repo)


@cred.command()
@click.argument('service_name')
@click.argument('user_name')
@pass_repo
def add(repo, service_name, user_name):
    password = getpass(f"Password for {user_name}[{service_name}]: ")
    print("Password 'set'. (debug mode. password not actually set.")
    # set_password(service_name, user_name, password)

    entry = CredEntry(key=service_name, user_name=user_name)
    _cred_repo.cred_entries.append(entry)

    write_cred_repo(repo, _cred_repo)


@cred.command()
def list():
    print("Credential entries:")
    for e in _cred_repo.cred_entries:
        print(f"\tKey: {e.key}\tUser Name: {e.user_name}")


def read_cred_repo(repo: Repo) -> CredRepo:
    repo_path = join(repo.path, "cred")
    json_path = join(repo_path, "cred.json")
    if not exists(repo_path):
        return CredRepo(cred_entries=[])
    else:
        return CredRepo.parse_file(json_path)


def write_cred_repo(repo: Repo, cred_repo: CredRepo):
    repo_path = join(repo.path, "cred")
    json_path = join(repo_path, "cred.json")
    if not exists(repo_path):
        mkdir(repo_path)

    with open(json_path, "w") as f:
        f.write(cred_repo.json())
