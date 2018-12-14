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

def build_single_repo(repo_name, clean_flag, build=True):
    # src_path = os.getenv("KHAOS_SRC")

    # cache_dir = os.path.join(os.getenv("KHAOS_BUILD"), "cache", repo_name, cmake.config)
    # inc_dir = os.path.join(os.getenv("KHAOS_BUILD"), "include", repo_name)

    # if os.path.exists(cache_dir):
    #     if clean_flag:
    #         click.echo("Cleaning %s..." % repo_name)

    #         for path in [ cache_dir, inc_dir ]:
    #             try:
    #                 click.echo("Deleting tree %s" % path)
    #                 shutil.rmtree(path)
    #             except FileNotFoundError:
    #                 click.echo("Not found! Continuing...")
    
    # if not os.path.exists(cache_dir):
    #     os.makedirs(cache_dir)
    
    # click.echo("Building %s..." % repo_name)

    # cmake.configure(os.path.join(src_path, repo_name), wd=cache_dir)

    # if build:
    #     cmake.make(cache_dir)
    pass

# Auto-complete

def get_repos(ctx, args, incomplete):
    return [ repo_name for repo_name in repos if repo_name.startswith(incomplete) ]

def get_active_repos(ctx, args, incomplete):
    actives = repos_utils.active_repos()
    return [ repo for repo in actives if repo.startswith(incomplete)]

def get_projects(ctx, args, incomplete):
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
    env = dotenv_values(os.path.join(os.getenv("KHAOS_ROOT"), "project.env"))
    cmake.configure(project, env, project_dep)

@main.command()
def status():
    """
    Show git status of every repository.
    """

    for repo in repos_utils.active_repos():
        git.status(repo)

@main.command()
@click.argument('repo', required=False, autocompletion=get_repos)
def pull(repo):
    """
    Pull differents repos
    """
    click.echo("Gathering repositories data...")

    if repo:
        repo_url = repos_utils.get_url(repo)
        git.pull(repo_url, repo)
    else:
        for rep_name, repo_details in repos.items():
            git.pull(repo_details['url'], rep_name)

@main.command()
@click.argument('repo', required=False, autocompletion=get_active_repos)
@click.option('-c', '--clean', is_flag=True, help='Clean before build')
def build(repo, clean):
    """
    Building projects
    """

    if repo:
        build_single_repo(repo, clean)
    else:
        for rep in repos_utils.active_repos():
            build_single_repo(rep, clean)
