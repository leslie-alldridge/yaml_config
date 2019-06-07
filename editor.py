# edits the team .yml to remove a user, repo in progress
from github import Github
from env import token

# First create a Github instance:
github = Github(token)

# Globals
python_repos = []

# Get all repos and analyze their tags
# add repos tagged with python to an array and print it


def analyze_repos():
    print('Checking repositories, please wait a moment...')
    # Get repo
    repo = github.get_repo(
        'leslie-alldridge/yaml_config')
    # List all contents
    contents = repo.get_contents("")
    # Get item with path="team.yml"
    yaml_repo = ""
    for content in contents:
        if content.name == 'team.yml':
            yaml_repo = content
        else:
            print('not team yaml')
    print(yaml_repo)
    # See if email address exists, and if so, remove it
    if 'leslie.alldridge@gmail.com' in str(yaml_repo.decoded_content):
        print(str(yaml_repo.decoded_content))

    #repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")
    print('Done')


analyze_repos()
