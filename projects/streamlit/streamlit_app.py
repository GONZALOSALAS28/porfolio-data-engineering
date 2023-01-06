import streamlit as st
import pandas as pd
import numpy as np

st.title('Basic Streamlit app')
from PIL import Image
image = Image.open('')
st.image(image, caption='Sunrise by the mountains')

if st.button('It works!'):
    st.balloons()