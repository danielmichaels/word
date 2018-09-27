"""
Helpers file
"""


def json_definition(json_):
    results = json_['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definition = [x['definitions'][0] for x in results]
    examples = [x['examples'][0]['text'] for x in results]

    for x in definition:
        print(x)

    for y in examples:
        print(y)
