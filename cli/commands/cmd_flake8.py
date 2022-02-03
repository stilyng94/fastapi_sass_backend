import subprocess
from typing import Optional

import typer

app = typer.Typer()


@app.command("format")
def cli(path: str = typer.Argument("app")):
    cmd = "autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place {0} " \
          "--exclude=__init__.py".format(path)
    return subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    app()
