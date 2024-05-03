import streamlit as st
from PIL import Image
import requests
from io import BytesIO
from agents import interior_design_for
import os
import shutil
from dotenv import load_dotenv

load_dotenv()

st.title('Interior Designer AI Assistant')

empty_room_url = st.sidebar.text_input("URL for Empty Room Image")

if empty_room_url:
    try:
        response = requests.get(empty_room_url)
        empty_room_image = Image.open(BytesIO(response.content))
        st.sidebar.image(empty_room_image, caption='Empty Room Image', use_column_width=True)
    except Exception as e:
        st.sidebar.error("Failed to download the image. Check the URL and try again.")

room_type = st.sidebar.selectbox(
    'Select Room Type',
    ('-', 'Living Room', 'Kitchen', 'Home Office', 'Coffee Shop', 'Restaurant', 
     'Office', 'Toilet', 'Bedroom', 'Bathroom', 'Dining Room', 'Study Room', 
     'Gaming Room', 'Attic', 'Other'),
    index=0
)

reference_style_url = st.sidebar.text_input("URL for Reference Style Image")

if reference_style_url:
    try:
        response = requests.get(reference_style_url)
        reference_style_image = Image.open(BytesIO(response.content))
        st.sidebar.image(reference_style_image, caption='Reference Style Image', use_column_width=True)
    except Exception as e:
        st.sidebar.error("Failed to download the image. Check the URL and try again.")

design_requirements = st.sidebar.text_area("Enter Design Requirements", height=300)

if empty_room_url and reference_style_url and design_requirements and room_type != '-':
    generate_button = st.sidebar.button('Generate')
else:
    generate_button = False
    st.sidebar.button('Generate', disabled=True)
    st.sidebar.warning('Please provide all required information to proceed.')

if generate_button:
    output_dir = 'output'
    
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        
    with st.spinner('Generating your custom interior design...'):
        interior_design_for(room_type, empty_room_url, reference_style_url, design_requirements)
        st.success("Generation complete!")
    
    # Display images in a grid layout
    files = os.listdir(output_dir)
    files.sort()
    if files:
        cols = st.columns(len(files))  # Creating a dynamic number of columns based on the number of images
        for col, file in zip(cols, files):
            image_path = os.path.join(output_dir, file)
            image = Image.open(image_path)
            col.image(image, caption=file, use_column_width=True)
    else:
        st.write("No images to display.")