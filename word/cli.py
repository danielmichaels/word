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
            click.echo(f'synonyms: {word}')
        elif antonyms:
            click.echo(f'antonyms: {word}')
        else:
            lookup.definition(word)
    except JSONDecodeError as e:
        print(e)
        print('word does not exist')


if __name__ == '__main__':
    cli()
