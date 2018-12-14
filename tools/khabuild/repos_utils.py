import os
from anytree import Node, LevelOrderIter

from repos_list import repos

def get_url(repo_name):
    return repos[repo_name]['url']

def active_repos():
    """
    Returns a list containing all repositories found in the src folder that are defined in the repos_list.py file.
    """
    src_dir = set(os.listdir(os.getenv("KHAOS_SRC")))
    listed_dir = set([k for k in repos])

    return src_dir.intersection(listed_dir)

def active_projects():
    """
    Returns a list containing all repositories found in the src folder that are defined in the repos_list.py file as 'project'.
    """
    src_dir = set(os.listdir(os.getenv("KHAOS_SRC")))
    listed_dir = set([k for k, rep in repos.items() if rep["type"] == "project"])

    return src_dir.intersection(listed_dir)


def get_dependencies(repo_name):
    """
    Returns a list with unique occurence of a repository dependancies.
    """
    dep_set = set(repos[repo_name]["dep"])

    for dep in dep_set:
        for sub_dep in repos[dep]["dep"]:
            dep_set.add(sub_dep)
    
    return list(dep_set)

def get_dependency_tree(repo_name):
    """
    Returns a list sorted children to ancestors from the repository tree structure with root repo_name.
    """
    root = Node(repo_name)

    parent = root
    repo = repos[repo_name]
    dep_list = repo["dep"]
    while dep_list:
        pass
