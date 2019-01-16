"""Enable CLI."""
import click


@click.command()
@click.option(
    '--port', '-P', default=9999, help='port number.')
def cli(port):
    """CLI for this package."""
    from componentstore.server import run_server
    run_server(port)


cli()  # pylint: disable=E1120
