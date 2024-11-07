import typer

from sparql_void_to_python import __version__
from sparql_void_to_python.generate_code import generate_code_for_endpoint

cli = typer.Typer()


@cli.command()
def cli_gen(
    endpoint: str = typer.Argument(None, help="SPARQL Endpoint URL"),
    folder: str = typer.Argument(None, help="Folder where to create the python package, will be also the package name"),
    ignore: list[str] = typer.Option(None, "-i", help="List of classes to ignore"),
    version: bool = typer.Option(False, help="Display version"),
    # verbose: bool = typer.Option(True, help="Display logs"),
) -> None:
    if version:
        print(__version__)
    else:
        generate_code_for_endpoint(endpoint, folder, ignore)


if __name__ == "__main__":
    cli()
