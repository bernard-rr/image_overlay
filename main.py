import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Title
st.title("Fixed Text Overlay on Image")

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Get user input text
    text = st.text_input("Enter text to overlay on the image")

    if text:
        # Fixed parameters
        font_size = 24
        font_color = "#000000"
        text_x = 10
        text_y = 10

        # Open the image using PIL
        image = Image.open(uploaded_image)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Load a font
        font = ImageFont.truetype("arial.ttf", font_size)

        # Draw the text on the image
        draw.text((text_x, text_y), text, font=font, fill=font_color)

        # Display the image with the overlay
        st.image(image, caption="Image with Text Overlay", use_column_width=True)
