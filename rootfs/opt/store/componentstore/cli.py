"""Enable CLI."""
import click


@click.command()
@click.option('--port', '-P', default=9999, help='port number.')
@click.option('--redishost', '-RH', default=None, help='Redis host.')
@click.option('--redisport', '-RP', default=None, help='Redis port.')
@click.option('--nocache', is_flag=True, help='Redis port.')
def cli(port, redishost, redisport, nocache):
    """CLI for this package."""
    from componentstore.server import run_server
    run_server(port, redishost, redisport, nocache)


cli()  # pylint: disable=E1120
