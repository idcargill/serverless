from http.server import BaseHTTPRequestHandler
from urllib import parse
from data_sources.chuck_norris import cn
import json

class handler(BaseHTTPRequestHandler):


  def do_GET(self):
    joke = cn.get_random_joke()['value']
    res_text = f'Chuck Noris Fact: \n{joke}'
    
    self.send_response(200)
    self.send_header('Content-type', 'text')
    self.end_headers()
    self.wfile.write(f'{res_text}'.encode())
    return