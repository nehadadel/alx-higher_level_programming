#!/usr/bin/python3
"""
"""


import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    Path_parameters = {'owner': owner_name, 'repo': repository_name}
    url = 'https://api.github.com/repos/{}/{}/commits'.format(sys.argv[2], sys.argv[1])


    r = requests.get(url, params=Path_parameters)
    commits = r.json()  # Get the list of commits

    for commit in commits:
        commit_sha = commit['sha']  # Access the 'sha' attribute of each commit
        author = commit['committer']
        print("{}: {}".format(commit_sha, author.get("name")))
