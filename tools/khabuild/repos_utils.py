import os
from repos_list import repos

def get_url(repo_name):
    for repo in repos:
        if repo['name'] == repo_name:
            return repo['url']

def get_dependencies(repo_name):
    repos_dict = {}
    for repo in repos:
        repos_dict[repo["name"]] = repo
    
    dep_set = set(repos_dict[repo_name]["dep"])

    for dep in dep_set:
        for sub_dep in repos_dict[dep]["dep"]:
            dep_set.add(sub_dep)
    
    return list(dep_set)
