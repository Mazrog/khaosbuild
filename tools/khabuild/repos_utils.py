import os

from repos_list import repos

def get_url(repo_name):
    """
    Returns the repository's distant url from the config file of the repository's name passed as argument.
    """
    for repo in repos:
        if repo["name"] == repo_name:
            return repo['url']
    return None

def active_repos():
    """
    Returns a list containing all repositories found in the src folder that are defined in the repos_list.py file.
    """
    src_dir = set(os.listdir(os.getenv("KHAOS_SRC")))
    listed_dir = set([k["name"] for k in repos])

    return src_dir.intersection(listed_dir)

def get_dependencies_dict():
    rep_dep_dict = {} # dictionnary with (key, value) = (repo_name, repo_dependencies)
    for repo in repos:
        rep_dep_dict[repo["name"]] = repo["dep"]

    return rep_dep_dict

def get_dependencies(repo_name):
    """
    Returns a list with unique occurence of a repository dependancies.
    """
    rep_dep_dict = get_dependencies_dict()

    dep_list = rep_dep_dict[repo_name]
    for dep in dep_list:
        for sub_dep in rep_dep_dict[dep]:
            dep_set = set(dep_list)
            dep_set.add(sub_dep)
            dep_list = list(dep_set)

    return dep_list
