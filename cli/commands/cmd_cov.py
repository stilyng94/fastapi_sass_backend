import subprocess
from typing import Optional

import typer

app = typer.Typer()


@app.command("test-coverage")
def cli(path: str = typer.Argument("app")):
    cmd = "pytest --cov={0} --cov-report=term-missing".format(path)
    return subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    app()
