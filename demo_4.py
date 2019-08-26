import click


@click.command()
@click.option("--count", "-c", type=int, default=1, help="Repetitions")
@click.argument("name")
def cli(name, count):
    """
    Say hello
    """
    for i in range(count):
        print(f"{i} Hello {name}")


if __name__ == '__main__':
    cli()
