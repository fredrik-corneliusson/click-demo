import click


@click.group()
def cli():
    "Click demo"
    pass


@cli.command()
@click.option("--count", "-c", default=1, help="Repetitions")
@click.argument("name")
def hello(name, count):
    """
    Say hello
    """
    for i in range(count):
        print(f"{i} Hello {name}")


@cli.command()
@click.option("--count", "-c", default=1, help="Repetitions")
@click.argument("name")
def bye(name, count):
    """
    Say bye
    """
    for i in range(count):
        print(f"{i} Bye {name}")


if __name__ == '__main__':
    cli()
