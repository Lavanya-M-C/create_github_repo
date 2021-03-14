import sys
import os
from dotenv import load_dotenv
from github import Github

load_dotenv()

path = os.getenv('FOLDERPATH')
access_token = os.getenv('GITHUB_ACCESSTOKEN')

def create_project():
    folder_name = str(sys.argv[1])
    newpath = os.path.join(path,folder_name)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    user = Github(access_token).get_user()
    # repo = user.create_repo(name=folder_name, private=True)
    repo = user.create_repo(name=folder_name)
    print(f"Succesfully created repository {folder_name}")


if __name__ == '__main__':
    create_project()


