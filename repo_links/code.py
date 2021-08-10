from pathlib import Path
from typing import Union, Tuple
from .git import Repo
from .typing import PathLike


def get_code_url(
    repo: Repo,
    path: PathLike,
    lines: Union[int, Tuple[int, int], None],
):
    if repo.remote.vcs == "bitbucket.org":
        return _get_bitbucket_url(repo, path, lines)
    elif repo.remote.vcs == "github.com":
        return _get_github_url(repo, path, lines)
    raise RuntimeError()


def _get_bitbucket_url(
    repo: Repo,
    path: PathLike,
    lines: Union[int, Tuple[int, int], None],
):
    path = Path(path)
    rel_path = path.absolute().relative_to(repo.git_root)
    url = f"https://{repo.remote.vcs}/{repo.remote.org}/{repo.remote.repo}"
    if rel_path != Path("."):
        url += f"/src/{repo.branch}/{rel_path}"
    if lines is not None:
        if isinstance(lines, int):
            url += f"#lines-{lines}"
        else:
            start, end = lines
            url += f"#lines-{start}:{end}"
    return url


def _get_github_url(
    repo: Repo,
    path: PathLike,
    lines: Union[int, Tuple[int, int], None],
):
    path = Path(path)
    rel_path = path.absolute().relative_to(repo.git_root)
    url = f"https://{repo.remote.vcs}/{repo.remote.org}/{repo.remote.repo}"
    if rel_path != Path("."):
        url += f"/blob/{repo.branch}/{rel_path}"
    if lines is not None:
        if isinstance(lines, int):
            url += f"#L{lines}"
        else:
            start, end = lines
            url += f"#L{start}-L{end}"
    return url
