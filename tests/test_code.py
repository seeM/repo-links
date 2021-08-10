from click.testing import CliRunner
import os
from repo_links.cli import cli


def test_bitbucket(mock_repo):
    runner = CliRunner()
    with runner.isolated_filesystem():
        assert [] == os.listdir(".")
        mock_repo("bitbucket.org")

        runner = CliRunner()
        result = runner.invoke(cli, ["code"], catch_exceptions=False)
        assert 0 == result.exit_code
        assert "https://bitbucket.org/seem/test-repo\n" == result.output


def test_github(mock_repo):
    runner = CliRunner()
    with runner.isolated_filesystem():
        assert [] == os.listdir(".")
        mock_repo("github.com")

        result = runner.invoke(cli, ["code"], catch_exceptions=False)
        assert 0 == result.exit_code
        assert "https://github.com/seem/test-repo\n" == result.output
