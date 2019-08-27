import click


@click.command()
@click.option("--count", "-c", default=1)
@click.argument("name")
def cli(name, count):
    for i in range(count):
        print(f"{i} Hello {name}")


if __name__ == '__main__':
    cli()
