# from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests

# class handler(BaseHTTPRequestHandler):

#   def do_Get(self):
#     self.send_response(200)
#     self.send_header('Content-type', 'text/plain')

#     # parse Url
#     url_path = self.path
#     url_components = parse.urlsplit(url_path)
#     query_string = parse.parse_qsl(url_components)
#     dic = (query_string)

#     self.wfile.write('Hello')
#     self.end_headers()
    
#     # Make API call with requests



from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    return 