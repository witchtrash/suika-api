__version__ = '0.0.1'
import typer

cli = typer.Typer(
  name='suika-cli'
)

@cli.command()
def main():
  typer.echo(f'suika-cli v{__version__}')

if __name__ == '__main__':
  cli()
