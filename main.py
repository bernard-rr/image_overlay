import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Function to overlay text on the image
def overlay_text(image_path, text, position=(10, 10), font_size=20, font_color=(255, 255, 255)):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("https://fonts.gstatic.com/s/raleway/v15/1Ptug8zYS_SKggPNyC0IT4ttDfCmxA.woff", font_size)
    draw.text(position, text, font=font, fill=font_color)
    return img

# Streamlit app
st.title("Image Overlay App")

# Upload the image
image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

# Input field for the overlay text
text = st.text_input("Enter text for overlay", value="Sample Text")

if image is not None:
    # Display the original image
    st.image(image, caption="Original Image", use_container_width=True)

    # Add overlay text to the image
    overlayed_image = overlay_text(image, text)
    
    # Display the image with overlay
    st.image(overlayed_image, caption="Image with Overlay", use_container_width=True)
