"""Enable CLI."""
import click


@click.command()
@click.option(
    '--port', '-P', default=9999, help='portnumber.')
@click.option(
    '--configdir', '-C', default='/config', help='Config dir.')
def cli(port, configdir):
    """CLI for this package."""
    from componentstore.server import run_server
    run_server(port, configdir)


cli()  # pylint: disable=E1120
