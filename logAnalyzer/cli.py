import click

from .helper import extractLJ


@click.command()
@click.argument("tarball")
def cli(tarball):
    print(f"tarball: {tarball}")
    extractLJ(tarball)


if __name__ == "__main__":
    cli()
