import os
from dotenv import load_dotenv
from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

load_dotenv()


base_url = os.environ.get("NASA_BASE_URL")
api_key= os.environ.get('NASA_API_KEY')
lon = -95.33          # float
lat = 29.78           # float
date = '2018-01-01'  # optional yyyy-mm-dd
dim = 0.15         # float w x h of image in degrees

nasa_url = f'{base_url}?lon={lon}&lat={lat}&date={date}&api_key={api_key}'

print(nasa_url)


# https://api.nasa.gov/planetary/earth/imagery?lon=100.75&lat=1.5&date=2014-02-01&api_key=DEMO_KEY
# https://api.nasa.gov/planetary/earth/imagery?lon=100.0&lat=75.0&date=2014-02-01&api_key=DEMO_KEY