import click


@click.command()
@click.argument('word')
@click.option('--thesaurus', '-t', is_flag=True,
              help='Get all thesaurus output for word.')
@click.option('--synonyms', '-s', is_flag=True,
              help='Return synonyms for given word.')
@click.option('--antonyms', '-a', is_flag=True,
              help='Return antonyms for given word.')
def cli(word, thesaurus, synonyms, antonyms):
    if thesaurus:
        click.echo(f'thesaurus {word}')
    elif synonyms:
        click.echo(f'synonyms: {word}')
    elif antonyms:
        click.echo(f'antonyms: {word}')
    else:
        click.echo(f"Here\n\nis the defintion of\n{word}")


if __name__ == '__main__':
    cli()
