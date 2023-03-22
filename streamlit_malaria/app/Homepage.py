# imports

import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import time
from streamlit.components.v1 import html
from streamlit_extras.switch_page_button import switch_page

# images used in the page opened here
Image.open('images/Cell-Homepage2.png')
# malaria_parasite_bright = Image.open('images/Cell-Homepage2.png')
malaria_parasite_red = Image.open('images/Cell-Homepage2.png')
red_cell_rotated = Image.open('images/Home-Red-Cell.png')
malari_eye_logo = Image.open('images/Malaria-Logo.png')
malaria_parasite = Image.open('images/Malaria-Parasite.jpeg')
africa_spread = Image.open('images/Africa-Spread-PhotoRoom.png')
malari_logo_home = Image.open('images/Homepage-Logo.png')

# page configuration...

# page title, tab icon, layout

st.set_page_config(page_title='Malari-Eye | AI Diagnostics',
                   page_icon=malari_eye_logo,
                   layout='wide'
)

# CSS-styling file opening for customisation of page

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

# malari-eye slogan top of page

st.markdown("<h1 style='text-align: center; color: white; font-family: Monaco; font-size: 100%;'>Microscopy results with the speed of RDTs.</h1>",
             unsafe_allow_html=True)

# straight line divider

st.markdown("""<hr style="height:1px; border:none; color:#FFFFFF; background-color:#FFFFFF;" /> """, unsafe_allow_html=True)
st.text('')

# malari_eye logo
# col_00, col_11 = st.columns([6,1])
# col_11.image(malari_eye_logo)
# st.text('')
# st.text('')

# malari-eye homepage image (left) with title and logo (right)

col_image, col_title = st.columns(2)
with col_image:
    st.image(red_cell_rotated)
with col_title:
    st.markdown("<h1 style='text-align: right; color: white; font-family: Monaco; font-size: 600%; text-shadow: 3px 3px grey; margin: 0px 10px; padding: 0px'>malari-</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: right; color: white; font-family: Monaco; font-size: 850%; text-shadow: 3px 3px grey; margin: 0px 10px; padding: 0px'>eye</h1>", unsafe_allow_html=True)
    # malari_eye logo
    st.text('')
    st.image(malari_logo_home)

# another divider

st.markdown("""<hr style="height:1px; border:none; color:#FFFFFF; background-color:#FFFFFF;" /> """, unsafe_allow_html=True)
st.text('')
st.text('')

# two columns with Africa map image and text

with st.container():
    col__1, col__2 = st.columns([2,3])
    with col__2:
        st.image(africa_spread)
    with col__1:
        # empty space before text next to map
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')
        st.text('')

        st.markdown("<h4 style='text-align: left; color: white; font-family: Monaco; font-size: 150%; letter-spacing: 2px; text-shadow: 2px 2px grey; line-height: 1.5'>1 million people die from malaria every year, primarily in the WHO African Region.</h4>",
                    unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: left; color: white; font-family: Monaco; font-size: 200%; text-shadow: 1px 1px grey; line-height: 1.5'>We are part of the solution.</h4>",
                    unsafe_allow_html=True)

# another divider
st.text('')
st.text('')
st.markdown("""<hr style="height:1px; border:none; color:#FFFFFF; background-color:#FFFFFF;" /> """, unsafe_allow_html=True)
st.text('')
st.text('')
st.text('')

# information about the model with button to Testing page on sidebar

with st.container():
    col1, col2 = st.columns([1,2])
    col1.text('')
    col1.text('')
    col1.markdown("<h4 style='text-align: left; color: black; font-family: Monaco; font-size: 150%; text-shadow: 1px 1px grey; padding: 3px 20px 8px 20px; line-height: 1.5'>A Vision Transformer for malaria-paratysized cell identification.</h4>",
                    unsafe_allow_html=True)
    col1.text('')
    if col1.button('TEST OUR PRODUCT', key=0):
        # function to make st.buttons take user to pages on side bar (from streamlit-extras)
        switch_page('Testing')
    col2.image(malaria_parasite_red)
