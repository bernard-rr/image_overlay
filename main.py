import streamlit as st

# Title
st.title("Google Font Text Overlay on Image")

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
        # Fixed parameters
        font_size = 24
        font_color = "#000000"
        text_x = 10
        text_y = 10

        # Display the text using the Google Font
        st.markdown(f'<p class="google-font">{text}</p>', unsafe_allow_html=True)
