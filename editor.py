from github import Github
from env import token

# First create a Github instance:
github = Github(token)

# Globals
python_repos = []

# Get all repos and analyze their tags
# add repos tagged with python to an array and print it


def analyze_repos(user):
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
    if user in str(yaml_repo.decoded_content):
        tidy_content(yaml_repo.decoded_content.decode("utf-8"))
    #repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")
    print('Done')


def tidy_content(content_as_string):
    tidy = content_as_string.splitlines()
    dictionary = dict()
    all_dictionaries = []
    for index, value in [x.split(": ") for x in tidy]:
        if index in dictionary:
            all_dictionaries .append(dictionary)
            dictionary = dict()
        else:
            dictionary[index] = value
    all_dictionaries.append(dictionary)
    print(all_dictionaries)


user = 'leslie.alldridge@gmail.com'
analyze_repos(user)
