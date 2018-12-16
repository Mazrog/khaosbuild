import os
import shutil
import click
from subprocess import run
from dotenv import dotenv_values

import repos_utils
from git import git
from cmake import cmake
from repos_list import repos

# Factorized functions

def get_config(env=None):
    if not env:
        env = dotenv_values(os.path.join(os.getenv("KHAOS_ROOT"), "project.env"))

    if env["CMAKE_BUILD_TYPE"] in [ "DEBUG", "RELEASE", "RELWITHDEBINFO", "MINSIZEREL" ]:
        config = env["CMAKE_BUILD_TYPE"]
    else:
        config = "DEBUG"
    
    return config

def get_build_paths():
    config = get_config().title()   # title function to capitalize first letter to have a proper path
    build_dir = os.getenv("KHAOS_BUILD")
    paths = [
        os.path.join(build_dir, "cache", config),
        os.path.join(build_dir, "bin", config),
        os.path.join(build_dir, "lib", config),
        os.path.join(build_dir, "include", config)
    ]

    return paths

def build_config_tree():
    paths = get_build_paths()

    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)


# Auto-complete

def get_repos(ctx, args, incomplete):
    """
    Autocomplete -> get repo's name from repos_list according to what has been entered.
    """
    return [ repo["name"] for repo in repos if repo["name"].startswith(incomplete) ]

def get_active_repos(ctx, args, incomplete):
    """
    Autocomplete -> get repo's name from pulled repos according to what has been entered.
    """
    actives = repos_utils.active_repos()
    return [ repo for repo in actives if repo.startswith(incomplete)]

def get_projects(ctx, args, incomplete):
    """
    Autocomplete -> get project's name from pulled repos of projects according to what has been entered.
    """
    projects = repos_utils.active_projects()
    return [repo for repo in projects if repo.startswith(incomplete)]

# Click commands

@click.group()
def main():
    """
    CLI managing the different projects for KhaOS Studio.
    """
    pass

@main.command()
def clean():
    """
    Clean build directory.
    """
    paths = get_build_paths()

    click.echo("Cleaning build directories...\n")

    for path in paths:
        try:
            click.echo("- Cleaning %s..." % path)
            shutil.rmtree(path)
        except FileNotFoundError:
            click.echo("-- Not found! Continuing...")
    
    build_config_tree()

@main.command()
@click.argument('project', autocompletion=get_projects)
def configure(project):
    """
    Configure a single project passed in argument
    """
    if project not in repos_utils.active_projects():
        with click.Context(configure) as ctx:
            click.echo(configure.get_help(ctx))
        return

    project_dep = repos_utils.get_dependencies(project)
    cmake.configure(project, project_dep)
    click.echo("Project %s has been configured!" % project)

@main.command()
def pre_build():
    """
    Does some pre-build process (reloading CMake Cache)
    """
    env = dotenv_values(os.path.join(os.getenv("KHAOS_ROOT"), "project.env"))
    config = get_config(env)
    cmake.reload(config, env)

@main.command()
def status():
    """
    Show git status of every repository.
    """

    for repo in repos_utils.active_repos():
        git.status(repo)

@main.command()
@click.argument('repo', required=False, autocompletion=get_repos)
@click.option('-i', '--ignore-dependencies', 'ignore_dependencies', is_flag=True, help='Ignore repo\'s dependencies while pulling.')
def pull(repo, ignore_dependencies):
    """
    Pull differents repos
    """
    click.echo("Gathering repositories data...")

    if repo:
        repos_to_pull = [ repo ]
        if not ignore_dependencies:
            repos_to_pull += repos_utils.get_dependencies(repo)
        
        for rep in repos_to_pull:
            repo_url = repos_utils.get_url(rep)
            git.pull(repo_url, rep)
    else:
        for repo in repos:
            git.pull(repo["url"], repo["name"])

@main.command()
@click.argument('repo', required=False, autocompletion=get_active_repos)
@click.option('-c', '--clean', 'clean_flag', is_flag=True, help='Clean before build')
def build(repo, clean_flag):
    """
    Building projects
    """

    config = get_config()
    build_dir = os.path.join(os.getenv("KHAOS_BUILD"), "cache", config.title())

    if clean_flag:
        clean()
    
    target = repo if repo else "all"
    cmake.make(build_dir, target)
            