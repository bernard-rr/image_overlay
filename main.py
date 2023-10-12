import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Load the image
image_path = 'your_image.jpg'  # Replace with your image path
image = Image.open(image_path)

# Define text to overlay
text_to_overlay = "Your Text Here"

# Define text position (x, y) and other parameters
text_position = (100, 100)  # Adjust the (x, y) coordinates as needed
text_color = "white"
font_path = "/workspaces/image_overlay/Raleway/static/Raleway-BoldItalic.ttf"
font_size = 36

# Create a drawing context
draw = ImageDraw.Draw(image)

# Load the specified font
font = ImageFont.truetype(font_path, font_size)

# Draw the text on the image
draw.text(text_position, text_to_overlay, fill=text_color, font=font)

# Display the modified image in Streamlit
st.image(image, use_column_width=True)

# Optionally, save the image with the overlay
image_with_overlay_path = "image_with_overlay.jpg"
image.save(image_with_overlay_path)

# Display the image with overlay for download
st.markdown(f"**[Download Image with Overlay]({image_with_overlay_path})**")
