import click
from cymorton.codec import convert_lat_lon_level_to_code


@click.command()
@click.argument('lat', type=click.FLOAT)
@click.argument('lon', type=click.FLOAT)
@click.argument('z', type=click.INT)
def main(lat: float, lon: float, z: int):
    click.echo(convert_lat_lon_level_to_code(lat, lon, z))
