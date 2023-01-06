import streamlit as st
import pandas as pd
from PIL import Image

# Tools

import folium
from shapely.geometry import Polygon
import numpy as np
import random
import time
from pyproj import Geod

from shapely import wkt
from geopandas import datasets, GeoDataFrame, read_file, points_from_xy

from folium.plugins import MeasureControl
from folium.plugins import MarkerCluster

from utils import GetLatLon2,cal_dist,distance_estac,transform_df_map,marker_rest
from streamlit_folium import folium_static

import os
from dotenv import load_dotenv

load_dotenv()
image = Image.open('images_streamlit/1_Fuel-prices.jpg')

st.sidebar.image(image , caption="Nearby Oil App",width = 256)
app_mode = st.sidebar.selectbox("Choose app mode", ["Run App","About Me"])

if app_mode == 'Run App':
  st.title('Nearby Oil Station App')
  st.markdown('App Description')

  df_map = pd.read_csv('DF_STATIONS.csv')
  cities =  list(df_map['Municipio'].unique())

  # Crear columnas usar st.columns especificando el ancho de las columnas
  c1,c2,c3,c4,c5 = st.columns((1,6,6,6,1))

  choose_city =  c2.selectbox("Choose city", cities)

  central_location = c2.text_input('Central Location', 'CC Multiplaza , Bogotá')

  DEVELOPER_KEY = os.getenv('API_KEY')

  if len(central_location) != 0 :
    R = GetLatLon2(central_location,DEVELOPER_KEY)
    geo
    breakpoint()

elif app_mode == "About Me":
  pass