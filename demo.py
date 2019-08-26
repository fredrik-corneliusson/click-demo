import click

DEBUG = False
@click.group()
@click.option("--debug/--no-debug")
def cli(debug):
    """Click demo"""
    global DEBUG
    DEBUG = debug

@cli.command()
@click.argument("name")
@click.option("--count", "-c", default=1, help="number of times to say hello")
def hello(name, count):
    """
    Say hello a number of times
    """
    print(f"Debug is {DEBUG}")
    for i in range(count):
        print(f"Hello {name}")

@cli.command()
@click.argument("name")
@click.option("--count", "-c", default=1, help="number of times to say bye")
def bye(name, count):
    """
    Say bye a number of times
    """
    for i in range(count):
        print(f"Bye {name}")

if __name__ == '__main__':
    cli()
