import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import os

def admin_panel():
    st.write("Admin Panel")

    # Admin authentication
    username = st.text_input("Admin Username")
    password = st.text_input("Admin Password", type="password")
    
    admin_credentials = {
        "admin1": "password1",
        "admin2": "password2",
        "admin3": "password3",
    }

    if username in admin_credentials and password == admin_credentials[username]:
        st.success(f"Logged in as {username}")
        st.session_state.is_admin = True
    else:
        st.error("Authentication failed")
        st.stop()

    # List to store uploaded images
    uploaded_images = []

    # Image upload and parameter settings
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        text = st.text_input("Text to overlay")
        font_name = st.selectbox("Font Family", ["Arial", "Times New Roman", "Raleway"])
        font_size = st.number_input("Font Size", min_value=1, value=36)
        text_color = st.color_picker("Text Color", "#ffffff")
        position_x = st.number_input("X Position", min_value=0, value=100)
        position_y = st.number_input("Y Position", min_value=0, value=100)

        if st.button("Overlay Text"):
            image = overlay_text_on_image(uploaded_image, text, font_name, font_size, text_color, position_x, position_y)
            st.image(image, caption="Image with Overlay", use_column_width=True)
            # Append the uploaded image to the list
            uploaded_images.append(image)

    return uploaded_images

def overlay_text_on_image(image, text, font_name, font_size, text_color, position_x, position_y):
    try:
        img = Image.open(image)
        draw = ImageDraw.Draw(img)
        font = ImageFont.load_default()

        if font_name == "Raleway":
            font_path = "/workspaces/image_overlay/Raleway/static/Raleway-BoldItalic.ttf"
            if os.path.exists(font_path):
                font = ImageFont.truetype(font_path, font_size)

        draw.text((position_x, position_y), text, fill=text_color, font=font)
        return img
    except Exception as e:
        st.error("An error occurred while processing the image.")
        return None
