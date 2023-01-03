import os


from tqdm import tqdm
from utils import request_wapi,get_forecast,create_df,send_message,get_date


query = 'Toluca'
api_key = os.getenv('API_KEY_WAPI')
# Armado de la URL
input_date= get_date()
response = request_wapi(api_key,query)

data = []

for i in tqdm(range(len(response['forecast']['forecastday'][0]['hour'])),colour = 'green'):

    data.append(get_forecast(response,i))

df_rain = create_df(data)

message = '\nHola! \n\n\n El pronostico del tiempo hoy '+ input_date +' en ' + query +' es : \n\n\n ' + str(df_rain)

# Send Message
message_id = send_message(message)

print('Mensaje Enviado con exito ' + message_id)
