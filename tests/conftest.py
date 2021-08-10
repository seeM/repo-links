import os
import subprocess
import pytest


@pytest.fixture
def mock_repo(tmp_path):
    def _mock_repo(vcs=None, ci=None):
        os.chdir(tmp_path)
        subprocess.run(["git", "init"], check=True)
        if vcs:
            subprocess.run(
                ["git", "remote", "add", "origin", f"git@{vcs}:seem/test-repo.git"],
                check=True,
            )
            subprocess.run(["git", "checkout", "-b", "main"], check=True)
        if ci:
            (tmp_path / ci).mkdir()

    return _mock_repo
