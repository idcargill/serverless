from http.server import BaseHTTPRequestHandler

text = '''
        Welcome to Chuck Norris Facts

        Here you can find out about Chuck Norris.  
        Also you can check the date for no reason. 

        Go somewhere else for facts.  
        This is not the place, this is only the intro page.

        For real information visit:
                /api/info    



                                  ....or just leave. 
'''

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text')
    self.end_headers()
    self.wfile.write(f'{text}'.encode())
    return
