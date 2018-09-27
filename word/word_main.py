import configparser
import os

import requests

from word.helpers import json_definition


class Word:
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.word.cfg'))

    def __init__(self):
        self.oxford_api_key = self.config['OXFORD']['OXFORD_API_KEY']
        self.oxford_app_id = self.config['OXFORD']['OXFORD_APP_ID']
        self.base_url = 'https://od-api.oxforddictionaries.com:443/api/v1'

    def call_api(self, url):
        params = {"app_id": self.oxford_app_id, "app_key": self.oxford_api_key}
        response = requests.get(url, headers=params)
        return response.json()

    def definition(self, word):
        entries = '/entries/en/'  # hardcoded for english currently
        url = self.base_url + entries + word.lower()
        json_ = self.call_api(url)
        json_definition(json_)

    def thesaurus(self):
        pass

    def antonyms(self):
        pass

    def synonyms(self):
        pass

    def run(self):
        """Used prior to plumbing in click."""
        pass


w = Word()
# w.definition('lexicon')
# w.definition('wordsmith')
# w.definition('logophile')
w.definition('ace')
