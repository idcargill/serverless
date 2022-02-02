import os
from unicodedata import category
import requests
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler
from urllib import parse
from datetime import datetime

load_dotenv()

now = datetime.now()


# class Categories_Cache:
#   def __init__(self):
#     self.last_request = None
#     self.categories_cache = []
  
#   def request_categories(self):
#     res = requests.get(f'{Chuck.categories_url}')
#     categories = res.json()
#     self.categories_cache = categories

#   def update(self):
#     if self.last_request is None:
#       self.last_request = datetime.now()
#       self.request_categories()
#       return self.categories_cache
#     else:
#       return self.categories_cache

class Chuck:
    base_url = os.environ.get('CHUCK_NORIS_BASE_URL')
    chuck_joke_url = f'{base_url}?category={category}'
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

cn = Chuck()

class handler(BaseHTTPRequestHandler):
  
  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(f'{cn.get_categories()}'.encode())
    return
