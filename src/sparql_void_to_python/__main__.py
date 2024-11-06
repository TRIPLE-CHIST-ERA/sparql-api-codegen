import typer

from sparql_void_to_python import __version__
from sparql_void_to_python.api import Api
from sparql_void_to_python.settings import BOLD, CYAN, END, Settings, parse_settings

cli = typer.Typer()


@cli.command("hello")
def cli_hello(
    name: str = typer.Argument("World", help="Who to greet"),
    settings: str = typer.Option(None, help="Path to the settings file"),
    output: str = typer.Option(None, "-o", help="Path to the output file"),
    verbose: bool = typer.Option(True, help="Display logs"),
) -> None:
    conf = parse_settings(settings) if settings else Settings()
    api = Api(conf)
    if output:
        if verbose:
            print(f"Writing to file {BOLD}{CYAN}{output}{END}")
        with open(output, "w") as file:
            file.write(api.hello_world(name))
    else:
        print(api.hello_world(name))


@cli.command("version")
def cli_version() -> None:
    print(__version__)


if __name__ == "__main__":
    cli()
