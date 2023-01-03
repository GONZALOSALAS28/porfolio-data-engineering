
import pandas as pd
from twilio.rest import Client
from datetime import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_date():

    input_date = datetime.now()
    input_date = input_date.strftime("%Y-%m-%d")

    return input_date

def request_wapi(api_key,query):

    url_clima = 'http://api.weatherapi.com/v1/forecast.json?key='+api_key+'&q='+query+'&days=1&aqi=no&alerts=no'

    try :
        response = requests.get(url_clima).json()
    except Exception as e:
        print(e)

    return response

def get_forecast(response, i):
  date = response['forecast']['forecastday'][0]['hour'][i]['time'].split()[0]
  hour = int(response['forecast']['forecastday'][0]['hour'][i]['time'].split()[1].split(':')[0])
  condition = response['forecast']['forecastday'][0]['hour'][i]['condition']['text']
  temp = float(response['forecast']['forecastday'][0]['hour'][i]['temp_c'])
  rain = response['forecast']['forecastday'][0]['hour'][i]['will_it_rain']
  prob_rain = response['forecast']['forecastday'][0]['hour'][i]['chance_of_rain']

  return date, hour, condition, temp, rain, prob_rain

def create_df(data):

    col = ['Date','Hour','Condition','Temperature','Rain','Prob_Rain']
    df = pd.DataFrame(data,columns=col)
    df = df.sort_values(by = 'Hour',ascending = True)

    current_hour = datetime.now().hour
    df = df[df['Hour']==current_hour]
    df_rain = df[['Hour','Condition', 'Rain', 'Prob_Rain', 'Temperature']]
    df_rain = df_rain.to_string(index=False)

    return df_rain


def send_message(message):

    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    phone_number = os.getenv('PHONE_NUMBER')
    my_phone_number = os.getenv('MY_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              body=message,
                              from_=phone_number,
                              to=my_phone_number
                          )

    return message.sid