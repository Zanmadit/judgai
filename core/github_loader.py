from github import Github
import base64

g = Github()  

def load_repo(github_url: str):
    parts = github_url.rstrip("/").split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub URL")

    owner = parts[-2]
    repo = parts[-1]

    return g.get_repo(f"{owner}/{repo}")

def get_readme(repo):
    readme = repo.get_readme()
    return base64.b64decode(readme.content).decode("utf-8")

def get_file_list(repo):
    tree = repo.get_git_tree(repo.default_branch, recursive=True).tree
    return [f.path for f in tree if f.type == "blob"]
