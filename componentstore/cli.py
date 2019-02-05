"""Enable CLI."""
import click


@click.command()
@click.option('--port', '-P', default=9999, help='port number.')
@click.option('--redishost', '-RH', default=None, help='Redis host.')
@click.option('--redisport', '-RP', default=None, help='Redis port.')
@click.option('--nocache', is_flag=True, help='Redis port.')
@click.option('--username', '-U', default='pi', help='Username.')
@click.option('--password', '-P', default='raspberry', help='Password.')
@click.option('--no_auth', is_flag=True, help='Disable auth.')
@click.option('--ha_path', default='/config', help='Full path to HA config dir.')
def cli(port, redishost, redisport, nocache, username, password, no_auth,
        ha_path):
    """CLI for this package."""
    from componentstore.server import run_server
    run_server(ha_path, username, password, no_auth, port, redishost,
               redisport, nocache)


cli()  # pylint: disable=E1120
