import streamlit as st

def user_panel(uploaded_images):
    st.write("User Panel")

    text = st.text_input("Enter text to overlay on images")
    
    if not uploaded_images:
        st.warning("No images uploaded by admin yet.")
        return

    selected_image = st.selectbox("Select an image:", uploaded_images)

    if text:
        st.image(selected_image, caption="Image with Overlay", use_column_width=True)
        st.markdown(f"Overlay Text: **{text}**")
