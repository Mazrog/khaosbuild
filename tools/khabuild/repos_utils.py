import os
from repos_list import repos

def get_url(repo_name):
    for repo in repos:
        if repo['name'] == repo_name:
            return repo['url']

def get_dependencies(repo_name):
    for repo in repos:
        if repo["name"] == repo_name:
            return repo["dep"]