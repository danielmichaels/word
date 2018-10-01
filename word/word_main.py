import configparser
import os

import click
import requests

from output import thesaurus_printer, definition


class Word:
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.word.cfg'))

    def __init__(self):
        self.oxford_api_key = self.config['OXFORD']['OXFORD_API_KEY']
        self.oxford_app_id = self.config['OXFORD']['OXFORD_APP_ID']
        self.base_url = 'https://od-api.oxforddictionaries.com:443/api/v1'
        self.entries_url = '/entries/en/'
        self.thesaurus_url = '/synonyms;antonyms'

    def call_api(self, url):
        params = {"app_id": self.oxford_app_id, "app_key": self.oxford_api_key}
        try:
            response = requests.get(url, headers=params)
            return response.json()
        except requests.exceptions.ConnectionError as e:
            click.echo(f"Connection Error encountered! {e}")

    def definition(self, word):
        url = self.base_url + self.entries_url + word.lower()
        json_ = self.call_api(url)
        definition(json_, 'definitions')

    def thesaurus(self, word):
        url = self.base_url + self.entries_url + word.lower() + self.thesaurus_url
        json_ = self.call_api(url)
        thesaurus_printer(json_, 'both')

    def antonyms(self, word):
        url = self.base_url + self.entries_url + word.lower() + self.thesaurus_url
        json_ = self.call_api(url)
        thesaurus_printer(json_, 'antonyms')

    def synonyms(self, word):
        url = self.base_url + self.entries_url + word.lower() + self.thesaurus_url
        json_ = self.call_api(url)
        thesaurus_printer(json_, 'synonyms')

