from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_Get(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    # parse Url
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string = parse.parse_qsl(url_components)
    dic = (query_string)

    return 'Hello'
    # Make API call with requests