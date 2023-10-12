import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os

# Function to overlay text on the image
def overlay_text(image_path, text, position=(10, 10), font_size=20, font_color=(255, 255, 255)):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font_path = "raleway.ttf"  # Path to the downloaded Raleway font file
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, font=font, fill=font_color)
    return img

# Streamlit app
st.title("Image Overlay App")

# Check if the Raleway font file exists, and if not, download it
font_path = "raleway.ttf"
if not os.path.exists(font_path):
    st.warning("Downloading Raleway font...")
    raleway_url = "https://github.com/google/fonts/raw/main/ofl/raleway/Raleway-Regular.ttf"
    raleway_response = requests.get(raleway_url)
    if raleway_response.status_code == 200:
        with open(font_path, "wb") as f:
            f.write(raleway_response.content)
        st.success("Raleway font downloaded successfully!")

# Upload the image
image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Input field for the overlay text
text = st.text_input("Enter text for overlay", value="Sample Text")

if image is not None:
    # Display the original image
    st.image(image, caption="Original Image")

    # Add overlay text to the image
    overlayed_image = overlay_text(image, text)
    
    # Display the image with overlay
    st.image(overlayed_image, caption="Image with Overlay")
