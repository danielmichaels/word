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
        for etymology in json_['etymologies']:
            return etymology
        else:
            return None
    except KeyError:
        pass
