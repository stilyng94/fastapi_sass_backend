import subprocess
import os
from typing import Optional

import typer

app = typer.Typer()

DEFAULT_PATH = os.path.join("app", "tests")


@app.command("test")
def cli(path: str = typer.Argument(DEFAULT_PATH)):
    cmd = "pytest {0}".format(path)
    return subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    app()
