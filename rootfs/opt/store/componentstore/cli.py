"""Enable CLI."""
import click


@click.command()
@click.option('--port', '-P', default=9999, help='port number.')
@click.option('--redishost', '-RH', default=None, help='Redis host.')
@click.option('--redisport', '-RP', default=None, help='Redis port.')
def cli(port, redishost, redisport):
    """CLI for this package."""
    from componentstore.server import run_server
    run_server(port, redishost, redisport)


cli()  # pylint: disable=E1120
