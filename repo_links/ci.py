from pathlib import Path
from typing import Optional
from .git import Repo
from .typing import PathLike


def get_ci_url(repo: Repo) -> str:
    ci = _get_ci(repo.git_root)
    if ci == "github":
        return _get_github_actions_url(repo)
    elif ci == "circleci":
        return _get_circleci_url(repo)
    raise RuntimeError()


def _get_ci(git_root: PathLike) -> Optional[str]:
    git_root = Path(git_root)
    for p in git_root.iterdir():
        if p.name == ".github":
            return "github"
        if p.name == ".circleci":
            return "circleci"
    return None


def _get_github_actions_url(repo: Repo) -> str:
    remote = repo.remote
    url = (
        f"https://{remote.vcs}/{remote.org}/{remote.repo}/actions"
        f"?query=branch%3A{repo.branch}"
    )
    return url


def _get_circleci_url(repo: Repo) -> str:
    remote = repo.remote
    vcs_base = remote.vcs.split(".")[0]
    url = (
        f"https://app.circleci.com/pipelines/{vcs_base}/{remote.org}/{remote.repo}"
        f"?branch={repo.branch}"
    )
    return url
