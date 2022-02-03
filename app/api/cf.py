from http.server import BaseHTTPRequestHandler
from urllib import parse
from data_sources.chuck_norris import cn
import json

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url = self.path
    query = parse.parse_qsl(url)
    data = cn.get_category_joke(query[0][1])
    print(data)
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(f'{data}'.encode())
    return
