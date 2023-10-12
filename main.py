import streamlit as st
from PIL import Image, ImageDraw, ImageFont

# Title
st.title("Text Overlay on Image")

# Add the Google Font using HTML and CSS
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
        .google-font {
            font-family: 'Raleway', sans-serif;
            font-size: 24px; /* You can adjust the font size as needed */
            color: #000000; /* You can specify the font color */
        }
    </style>
    """, unsafe_allow_html=True
)

# Upload an image
uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Get user input text
    text = st.text_input("Enter text to overlay on the image")

    if text:
        # Open the image using PIL
        image = Image.open(uploaded_image)

        # Get the image dimensions
        img_width, img_height = image.size

        # Fixed parameters
        font_size = 100
        font_color = "#000000"

        # Load the Raleway font
        font = ImageFont.load_default()

        # Calculate the position to center the text
        text_width, text_height = font.getsize(text)
        text_x = (img_width - text_width) // 2
        text_y = (img_height - text_height) // 2

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Draw the text on the image
        draw.text((text_x, text_y), text, font=font, fill=font_color)

        # Display the image with the overlay
        st.image(image, caption="Image with Text Overlay", use_column_width=True)
