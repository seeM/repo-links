from setuptools import setup  # type: ignore
import os

VERSION = "0.1.0"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="repo-links",
    description="Quickly open URLs related to your repos",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Wasim Lorgat",
    url="https://github.com/seem/repo-links",
    version=VERSION,
    packages=["repo_links"],
    entry_points="""
        [console_scripts]
        repo-links=repo_links.cli:cli
    """,
    install_requires=["click", "click-default-group"],
    extras_require={"test": ["pytest"]},
    tests_require=["repo-links[test]"],
)
