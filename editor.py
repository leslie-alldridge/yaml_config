from github import Github
from env import token

# First create a Github instance:
github = Github(token)

# Get repo
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
    output = []
    for key_value in tidy:
        key, value = key_value.split(': ', 1)
        if not output or key in output[-1]:
            output.append({})
        output[-1][key] = value
    print(output)


user = 'leslie.alldridge@gmail.com'
analyze_repos(user)
