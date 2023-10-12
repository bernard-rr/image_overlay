import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Define the path to the font file
font_path = "/workspaces/image_overlay/Raleway/static/Raleway-BoldItalic.ttf"

def overlay_text_on_image(image, text):
    try:
        img = Image.open(image)
        draw = ImageDraw.Draw(img)
        
        # Define fixed parameters for text overlay
        position = (100, 100)  # Change this to your desired position
        text_color = (255, 255, 255)  # Change this to your desired text color
        text_size = 36  # Change this to your desired text size

        # Load the font
        font = ImageFont.truetype(font_path, text_size)

        # Overlay the text on the image
        draw.text(position, text, fill=text_color, font=font)
        
        return img
    except Exception as e:
        return None

st.title("Image Text Overlay App")

# Upload image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Get user input
    text = st.text_input("Enter text to overlay on the image")

    if st.button("Overlay Text"):
        if text:
            st.write("Image with Overlay:")
            overlaid_image = overlay_text_on_image(uploaded_image, text)
            if overlaid_image:
                st.image(overlaid_image, caption="Image with Overlay", use_column_width=True)
            else:
                st.error("An error occurred while processing the image.")

st.write("Note: You cannot edit the parameters as they are fixed.")
