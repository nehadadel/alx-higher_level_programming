#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""


import sys
import requests


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    Path_parameters = {'owner': owner_name, 'repo': repository_name}
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url, params=Path_parameters)
    commits = r.json()  # Get the list of commits

    try:
        for i in range(10):
            # Access the 'sha' attribute of each commit
            commit_sha = commits[i].get("sha")
            author = commits[i].get("commit").get("author")
            print("{}: {}".format(commit_sha, author.get("name")))
    except IndexError:
        pass
