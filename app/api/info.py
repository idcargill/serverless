from http.server import BaseHTTPRequestHandler
from data_sources.chuck_norris import cn
import json

text = {
  "Title": 'Chuck Norris Facts',
  "Instructions": 'Go to api/ random or <category> to get random or categorical facts about Chuck Norris',
  "Routes": ['/api/', '/api/fact', '/api/date', '/api/cf?category=<category>' ],
  "Categories": cn.get_categories()
}
json_text = json.dumps(text, indent=4)
  
class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'application/json')
    self.end_headers()
    self.wfile.write(f'{json_text}'.encode())
    return
      
