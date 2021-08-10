import os
import pytest
from click.testing import CliRunner
from repo_links.cli import cli


@pytest.fixture
def mock_ci_repo(tmp_path):
    def _mock_ci_repo(ci):
        (tmp_path / ci).mkdir()

    return _mock_ci_repo


def test_circleci(mock_repo):
    runner = CliRunner()
    with runner.isolated_filesystem():
        assert [] == os.listdir(".")
        mock_repo("github.com", ci=".circleci")

        result = runner.invoke(cli, ["ci"], catch_exceptions=False)
        assert 0 == result.exit_code
        assert (
            "https://app.circleci.com/pipelines/github/seem/test-repo?branch=main\n"
            == result.output
        )
