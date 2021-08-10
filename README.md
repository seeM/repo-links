# repo-links

[![PyPI](https://img.shields.io/pypi/v/repo-links.svg)](https://pypi.org/project/repo-links/)
[![Changelog](https://img.shields.io/github/v/release/seem/repo-links?include_prereleases&label=changelog)](https://github.com/seem/repo-links/releases)
[![Tests](https://github.com/seem/repo-links/workflows/Test/badge.svg)](https://github.com/seem/repo-links/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/seem/repo-links/blob/main/LICENSE)

Quickly open URLs related to your repos.

## How to install

    $ pip install repo-links

## Example usage

Each command prints the URL to a relevant service. For that to actually be useful, you probably want to use it in another command. For example, on MacOS you can use the `open` command to open the URL in the default browser.

The command below would open your repo's page on it's code management system.

    $ open $(repo-links code)

## Open a repo in a code management system

The `code` command prints a URL to the repo's code management system. The details are automatically pulled from your locally setup git remotes. Without any additional arguments, it'll open the repo's root page in your code management system.

    $ repo-links code

You can also point to a specific file or directory.

    $ repo-links code ./repo_links/cli.py

You can optionally specify either a single line or a range of lines to have them selected (useful when collaborating on code snippets).

    $ repo-links code ./repo_links/cli.py --lines 12
    $ repo-links code ./repo_links/cli.py --lines 12:15

Currently supported code management systems:

- GitHub
- Bitbucket

## Open your repo in a CI/CD platform

The `ci` command opens a repo's CI/CD platform page. The platform is determined by whether their configuration files exist locally (e.g. a `.github` folder for GitHub Actions).

    $ repo-links ci

Currently supported CI/CD platforms:

- CircleCI

## Building your own plugins

_Under construction. `repo-links` is planning to support plugins._

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd repo_links
    python -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest
