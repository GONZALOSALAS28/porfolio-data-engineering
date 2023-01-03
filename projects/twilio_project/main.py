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
from tqdm import tqdm

load_dotenv()

def get_forecast(response, i):
  date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
  hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
  condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
  temp = float(response['forecast']['forecastday'][0]['hour'][i]['temp_c'])
  rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
  prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']

  return date, hour, condition, temp, rain, prob_rain

query = 'Toluca'
api_key = os.getenv('API_KEY_WAPI')
# Armado de la URL
url_clima = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'
response = requests.get(url_clima).json()

data = []

for i in tqdm(range(len(response['forecast']['forecastday'][0]['hour'])),colour = 'green'):

    data.append(get_forecast(response,i))
col = ['Date','Hour','Condition','Temperature','Rain','Prob_Rain']
df = pd.DataFrame(data,columns=col)
df = df.sort_values(by = 'Hora',ascending = True)
breakpoint()
