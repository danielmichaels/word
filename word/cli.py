from json import JSONDecodeError

import click

from word_main import Word


@click.command()
@click.argument('word')
@click.option('--thesaurus', '-t', is_flag=True,
              help='Get all thesaurus output for word.')
@click.option('--synonyms', '-s', is_flag=True,
              help='Return synonyms for given word.')
@click.option('--antonyms', '-a', is_flag=True,
              help='Return antonyms for given word.')
def cli(word, thesaurus, synonyms, antonyms):
    lookup = Word()
    try:
        if thesaurus:
            lookup.thesaurus(word)
        elif synonyms:
            lookup.synonyms(word)
        elif antonyms:
            lookup.antonyms(word)
        else:
            lookup.definition(word)
    except JSONDecodeError:
        click.echo(f"Word: '{word}' not found!")
        click.echo("Please check spelling and try again.")


if __name__ == '__main__':
    cli()
