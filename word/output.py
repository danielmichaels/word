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

    except KeyError:
        pass


def etymology(json_):
    list_of_origins = []
    try:
        etymologies = item_generator(json_, 'etymologies')
        num = 1
        for etymol in etymologies:
            list_of_origins.append(etymol)
        if len(list_of_origins) >= 1:
            click.echo('\nOrigin\'s')
            for origin in list_of_origins:
                click.echo(f"{num}. {origin[0]}")
                num += 1
    except KeyError:
        pass


