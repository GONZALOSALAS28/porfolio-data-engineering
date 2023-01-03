import os
import time
import json
import pandas as pd
import requests

from dotenv import load_dotenv
from twilio.rest import Client
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from datetime import datetime

from bs4  import BeautifulSoup

load_dotenv()

query = 'Toluca'
api_key = os.getenv('API_KEY_WAPI')
# Armado de la URL
url_clima = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'
response = requests.get(url_clima).json()
breakpoint()
