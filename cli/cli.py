import typer

from commands import cmd_flake8, cmd_test, cmd_cov

app = typer.Typer()

app.add_typer(cmd_cov.app, name="test-coverage")
app.add_typer(cmd_test.app, name="test")
app.add_typer(cmd_flake8.app, name="formatter")


if __name__ == "__main__":
    app()
