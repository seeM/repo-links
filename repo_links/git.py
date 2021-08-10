from dataclasses import dataclass
from pathlib import Path
import re
import subprocess

from .typing import PathLike


class NotAGitRepoError(Exception):
    pass


class NoGitRemoteError(Exception):
    pass


def git(args, path: PathLike = Path(".")) -> subprocess.CompletedProcess:
    path = Path(path)
    dir_path = path.parent if path.is_file() else path
    try:
        proc = subprocess.run(
            args,
            check=True,
            capture_output=True,
            text=True,
            cwd=dir_path,
        )
    except subprocess.CalledProcessError as exception:
        msg = "fatal: not a git repository (or any of the parent directories): .git\n"
        if exception.stderr == msg:
            raise NotAGitRepoError(f"'{path}' is not a git repository")
        raise exception
    return proc


def get_git_root(path: PathLike = Path(".")) -> Path:
    proc = git(["git", "rev-parse", "--show-toplevel"], path)
    git_root = Path(proc.stdout.strip())
    return git_root


def get_current_branch(path: PathLike = Path(".")) -> str:
    proc = git(["git", "branch", "--show-current"], path)
    branch = proc.stdout.strip()
    return branch


@dataclass
class Remote:
    vcs: str
    org: str
    repo: str


def get_remote(path: PathLike = Path(".")) -> Remote:
    proc = git(["git", "remote", "--verbose"], path)
    pat = r"git@(.*):(.*)/(.*)\.git"
    match = re.search(pat, proc.stdout)
    if match is None:
        raise NoGitRemoteError(f"'{path}' has no remote")
    vcs, org, repo = match.groups()
    remote = Remote(vcs, org, repo)
    return remote


@dataclass
class Repo:
    git_root: Path
    remote: Remote
    branch: str


def get_repo(path: PathLike = Path(".")) -> Repo:
    git_root = get_git_root(path)
    remote = get_remote(path)
    branch = get_current_branch(path)
    return Repo(git_root, remote, branch)
