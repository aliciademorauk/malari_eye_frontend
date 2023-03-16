import streamlit as st
import numpy as np
from PIL import Image
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import time

# images:

malaria_parasite_bright = Image.open('./images/Cells-Background.jpeg')
malari_eye_logo = Image.open('./images/Malaria-Logo.png')
malaria_parasite = Image.open('./images/Malaria-Parasite.jpeg')
bounding_boxes_img = Image.open('./images/Rounded-Boxes.png')
blood_microscope_slide = Image.open('./images/Rounded-Hands-Slide.png')
purple_cells = Image.open('./images/Purple-Cells-PhotoRoom.png')
arnaud_photo = Image.open('./images/Arnaud-Pro-Circle.png')
alicia_photo = Image.open('./images/Alicia-Pro-Circle.png')
mark_photo = Image.open('./images/Mark-Pro-Circle.png')
transformer_diagram = Image.open('./images/Transformer-Diagram-Rounded.png')

# page configuration...

# 1. page title, layout

st.set_page_config(page_title='Malari-Eye | The Project',
                   page_icon=malari_eye_logo,
                   layout='wide'
)

# malari_eye logo

col_00, col_11 = st.columns([7,1])
col_11.image(malari_eye_logo)

# CSS styling file opening for customisation

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}<style>', unsafe_allow_html=True)

# start of page
st.markdown("<h4 style='text-align: left; color: white; font-family: Monaco; font-size: 200%; text-shadow: 1px 1px grey; line-height: 1.5'>About the Project</h4>",
                    unsafe_allow_html=True)
st.markdown("""<hr style="height:1px; border:none; color:#FFFFFF; background-color:#FFFFFF;" /> """, unsafe_allow_html=True)

# how it works in steps
st.text('')
st.text('')
st.text('')
st.markdown("<h4 style='text-align: left; color: white; font-family: Monaco; font-size: 150%; text-shadow: 1px 1px grey; line-height: 1.5'>How it Works</h4>",
                    unsafe_allow_html=True)

# how it works - step 1

col11 , col22 = st.columns([2,1])
st.text('')
st.text('')
st.text('')
col11.image(blood_microscope_slide, use_column_width=True)
col22.text('')
col22.text('')
col22.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 150%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>Upload your blood sample.</h4>",
                    unsafe_allow_html=True)
col22.text('')
col22.text('')
col22.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 90%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>Using our Testing Area, connect your microscopy camera or upload a scientific image of the slide.</h4>",
                    unsafe_allow_html=True)

# how it works - step 2

col111,col222 = st.columns([1,2])
st.text('')
st.text('')
st.text('')
col111.text('')
col111.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 150%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>Our model will scan the image to detect individual cells.</h4>",
                    unsafe_allow_html=True)
col111.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 90%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>Leveraging real-time object detection, our programme encircles individual cells with bounding boxes.</h4>",
                    unsafe_allow_html=True)
col222.image(bounding_boxes_img, use_column_width=True)

# how it works - step 3

col1111,col2222 = st.columns([2,1])
st.text('')
st.text('')
st.text('')
col2222.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 150%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>Vision Transformer Model.</h4>",
                    unsafe_allow_html=True)
col2222.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 90%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>Our model makes a prediction on each input cell based on what it has learned from 80,000 categorized cells.</h4>",
                    unsafe_allow_html=True)
col1111.image(transformer_diagram)

# how it works - step 4

col11111,col22222 = st.columns([1,2])
st.text('')
st.text('')
st.text('')
col11111.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 150%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>Cells are classified into infection categories.</h4>",
                    unsafe_allow_html=True)
col11111.markdown("<h4 style='font-family: Monaco; text-align: left; color: black; font-size: 90%; text-shadow: 1px 1px grey; padding: 30px 30px 10px 30px; line-height: 1.5'>If an infection is detected, our model labels the cell based on its spreading stage: Ring, Trophozoite, Schizont, Gametocyte.</h4>",
                    unsafe_allow_html=True)
col22222.image(purple_cells)

# meet the team photos and names

st.markdown("<h4 style='text-align: left; color: white; font-family: Monaco; font-size: 150%; text-shadow: 1px 1px grey; line-height: 1.5'>Meet the Team</h4>",
                    unsafe_allow_html=True)
st.markdown("""<hr style="height:1px; border:none; color:#FFFFFF; background-color:#FFFFFF;" /> """, unsafe_allow_html=True)
st.text('')
st.text('')
st.text('')
meet_the_team_space0, meet_the_team_1, meet_the_team_2, meet_the_team_3, meet_the_team_space4 = st.columns([1,3,3,3,1])
meet_the_team_3.image(alicia_photo)
meet_the_team_3.markdown("<h4 style='text-align: center; color: white; font-family: Monaco; font-size: 100%; text-shadow: 1px 1px grey'>Alicia de Mora Losana</h4>", unsafe_allow_html=True)
meet_the_team_2.image(arnaud_photo)
meet_the_team_2.markdown("<h4 style='text-align: center; color: white; font-family: Monaco; font-size: 100%; text-shadow: 1px 1px grey'>Arnaud Plantenga</h4>", unsafe_allow_html=True)
meet_the_team_1.image(mark_photo)
meet_the_team_1.markdown("<h4 style='text-align: center; color: white; font-family: Monaco; font-size: 100%; text-shadow: 1px 1px grey'>Mark White</h4>", unsafe_allow_html=True)
