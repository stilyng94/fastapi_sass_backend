import subprocess
import click


@click.command("test-coverage")
@click.argument("path", default="app")
def cli(path):
    cmd = "pytest --cov={0} --cov-report=term-missing".format(path)
    return subprocess.run(cmd, shell=True)
