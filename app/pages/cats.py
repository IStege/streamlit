import streamlit as st
import requests
import numpy as np
from PIL import Image

st.set_page_config(page_title="Test-app about cats", layout="centered", page_icon="🐱")

def get_cat_fact():
    url_facts = "https://catfact.ninja/fact"
    response_facts = requests.get(url=url_facts).json()

    return response_facts["fact"]

@st.cache
def get_cached_cat_fact():
    return get_cat_fact()

@st.cache
def get_image(query):
    url_images = "https://api.giphy.com/v1/gifs/search"
    params_images = {'api_key' : st.secrets.giphy_api_key, 'q' : query,'limit' : 10}
    response_images = requests.get(url=url_images, params=params_images).json()
    return response_images['data'][np.random.randint(0,10)]['embed_url']

st.markdown("<h1 align='center'> Cats! 🐱<h1>", unsafe_allow_html=True)

page_columns = st.columns(3)
image = Image.open('raw_data/IMG_0032.jpg')

st.markdown("### Did you know?")
placeholder = st.empty()
if st.checkbox('Keep facts cached', value=False):
    placeholder.markdown(f"**{get_cached_cat_fact()}**", unsafe_allow_html=True)
else:
    placeholder.markdown(f"**{get_cat_fact()}**", unsafe_allow_html=True)

st.markdown("#")

query = st.text_input("Search a GIF")

while not query:
    page_columns[1].image(image, caption='Kushi', width=240)
    st.stop()

st.markdown("###")

st.write(
    f'<iframe src="{get_image(query)}" align="right" width="480" height="240">', unsafe_allow_html=True
)
