import click

DEBUG = False


@click.group()
@click.option("--debug/--no-debug", "-d", help="Debug flag")
def cli(debug):
    "Click demo"
    global DEBUG
    DEBUG = debug


@cli.command()
@click.option("--count", "-c", default=1, help="Repetitions")
@click.argument("name")
def hello(name, count):
    """
    Say hello
    """
    if DEBUG:
        print(f"Debug={DEBUG}")
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
