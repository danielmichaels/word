import configparser
import os

import requests

from output import thesaurus_printer, definition


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
        url = self.base_url + '/entries/en/' + word.lower()
        json_ = self.call_api(url)
        definition(json_, 'definitions')

    def thesaurus(self, word):
        both = '/synonyms;antonyms'
        url = self.base_url + '/entries/en/' + word.lower() + both
        json_ = self.call_api(url)
        thesaurus_printer(json_, 'synonyms')
        # printer(json_, 'antonyms')

    def antonyms(self):
        pass

    def synonyms(self):
        pass

    def run(self):
        """Used prior to plumbing in click."""
        pass


w = Word()
w.definition('gentrification')
w.definition('ace')
# w.thesaurus('house')
# w.thesaurus('ace')
