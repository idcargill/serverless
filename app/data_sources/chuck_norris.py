import os
import requests
from dotenv import load_dotenv
from urllib import parse
from datetime import datetime
import json

load_dotenv()

message = {
  'No_Data': 'Something went wrong...it was probably your fault.'
}

class Chuck_Norris:
    base_url = os.environ.get('CHUCK_NORIS_BASE_URL')
    # chuck_joke_url = f'{base_url}?category={category}'
    random_joke_url = os.environ.get('RANDOM_JOKE_URL') or 'https://api.chucknorris.io/jokes/random'
    test_resp = 'Chuck will kill you hard'

    def __init__(self):
      self.last_request = None
      self.categories_cache = []
      self.categories_url = os.environ.get('CHUCK_NORIS_CATEGORIES_URL') or 'https://api.chucknorris.io/jokes/categories'

    def update(self):
      res = requests.get(f'{self.categories_url}')
      categories = res.json()
      self.categories_cache = categories
    
    def get_categories(self):
      if self.last_request is None:
        now = datetime.now()
        self.last_request = now.date()
        self.update()
        return self.categories_cache
      elif  datetime.now().date != self.last_request:
        self.last_request = datetime.now().date()
        self.update()
        return self.categories_cache
      else:
        return self.categories_cache

    def get_category_joke(self, category):
      self.get_categories()
      if category in self.categories_cache:
        res = requests.get(f'{self.random_joke_url}?category={category}')
        data = res.json()
        return data['value']
      else:
        return message

      
    def get_random_joke(self):
      res = requests.get(f'{self.random_joke_url}')
      data = res.json()
      if data:
        return data
      else:
        return 'Nothing to report'

cn = Chuck_Norris()