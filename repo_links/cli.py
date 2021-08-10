import click
from click_default_group import DefaultGroup  # type: ignore
import re
from typing import Union, Tuple

from . import git
from .code import get_code_url
from .ci import get_ci_url


@click.group(
    cls=DefaultGroup,
    default="code",
)
@click.version_option()
def cli():
    pass


def validate_lines(
    ctx: click.core.Context, param: click.core.Option, value: Union[str, None]
):
    if value is None:
        return

    pat = r"^([0-9]*)$"
    match = re.match(pat, value)
    if match is not None:
        return int(match.groups()[0])

    pat = r"^([0-9]*):([0-9]*)$"
    match = re.match(pat, value)
    if match is not None:
        start, end = match.groups()
        return int(start), int(end)

    raise click.BadParameter("format must be <int> or <int>:<int>")


@cli.command()
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    default=".",
    required=False,
)
@click.option("--lines", type=click.UNPROCESSED, callback=validate_lines, default=None)
def code(path: str, lines: Union[int, Tuple[int, int], None]) -> None:
    repo = git.get_repo(path)
    url = get_code_url(repo, path, lines)
    click.echo(url)


@cli.command()
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=True, dir_okay=True),
    default=".",
    required=False,
)
def ci(path: str) -> None:
    repo = git.get_repo(path)
    url = get_ci_url(repo)
    click.echo(url)
