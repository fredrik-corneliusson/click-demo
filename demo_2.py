import click


@click.command()
@click.argument("name")
def cli(name):
    for i in range(5):
        print(f"{i} Hello {name}")


if __name__ == '__main__':
    cli()
