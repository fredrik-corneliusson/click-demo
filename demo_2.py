import click


@click.command()
@click.argument("name")
def cli(name):
    print(f"Hello {name}")


if __name__ == '__main__':
    cli()
