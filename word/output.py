from json import JSONDecodeError

import click


def print_definition(json_):
    """Print the definition of searched word to terminal."""
    word = json_['results'][0]['word']
    click.echo()
    click.echo(f"{word}")
    for i in json_["results"]:
        for j in i["lexicalEntries"]:
            click.echo()
            click.echo(f"({j['lexicalCategory']})")  # noun/ verb etc
            click.echo()
            for k in j["entries"]:
                etymologies = etymology(k)
                for v in k["senses"]:
                    click.echo(f"+ {v['definitions'][0].capitalize()}")

                if etymologies:
                    click.echo("\nOrigin\n")
                    click.echo(etymologies)


def etymology(json_):
    try:
        for origin in json_['etymologies']:
            return origin
        else:
            return None
    except KeyError:
        pass


def thesaurus(json_, thesaurus_: str):
    try:
        thesaurus_words = list()
        for like_word in json_[thesaurus_]:
            word = like_word['text'].capitalize()
            thesaurus_words.append(word)
        return print_lists(thesaurus_words)

    except KeyError as e:
        click.echo(e)
    except JSONDecodeError as e:
        click.echo(e)


def print_lists(list_words):
    if isinstance(list_words, list):
        click.echo(", ".join(x for x in list_words))


def print_thesaurus(json_):
    word = json_['results'][0]['word']
    click.echo()
    click.echo(word)
    for i in json_["results"]:
        for j in i["lexicalEntries"]:
            click.echo()
            click.echo(f"({j['lexicalCategory']})")  # noun/ verb etc
            click.echo()
            for k in j["entries"]:
                for v in k["senses"]:
                    thesaurus(v, 'synonyms')
                    thesaurus(v, 'antonyms')
