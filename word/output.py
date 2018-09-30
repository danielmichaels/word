import click


def item_generator(json_input, lookup_key):
    if isinstance(json_input, dict):
        for k, v in json_input.items():
            if k == lookup_key:
                yield v
            else:
                yield from item_generator(v, lookup_key)
    elif isinstance(json_input, list):
        for item in json_input:
            yield from item_generator(item, lookup_key)


def thesaurus_generator(json_, key):
    words = list()
    for item in item_generator(json_, key):
        for xx in item:
            vals = xx['id']
            words.append(vals)
    splits = ", ".join(x for x in words)
    return splits


def thesaurus_printer(json_, caller=None):
    try:
        t = thesaurus_generator(json_, caller)
        click.echo(t)
    except KeyError:
        pass


def definition(json_, caller):
    try:
        words = item_generator(json_, caller)
        for word in words:
            click.echo(word[0].capitalize())
        etymology(json_)

    except KeyError as e:
        pass


def etymology(json_):
    try:
        etymologies = item_generator(json_, 'etymologies')
        click.echo('\nOrigin\'s')
        num = 1
        for etymol in etymologies:
            click.echo(f"{num}. {etymol[0]}")
            num += 1
    except KeyError as e:
        pass


