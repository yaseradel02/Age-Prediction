import streamlit as st
import numpy as np
from PIL import Image
from pathlib import Path
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Age Prediction")

st.title("Age Prediction")
st.write("Upload a face photo or take a picture with your webcam.")

# The model file goes in the same folder as this app.
model_path = Path(__file__).parent / "age_model.keras"

@st.cache_resource
def get_model():
    return load_model(model_path, compile=False)

if not model_path.exists():
    st.warning("Add your trained 'age_model.keras' file to this app folder.")
    st.stop()

# Choose how to provide a photo.
option = st.radio("Choose an option:", ["Upload Image", "Use Webcam"], horizontal=True)

if option == "Upload Image":
    photo = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])
else:
    photo = st.camera_input("Take a photo")
    st.caption("The webcam option takes a photo; it does not predict continuously from video.")

if photo is not None:
    image = Image.open(photo)
    st.image(image, caption="Your photo", width=280)

    if st.button("Predict Age"):
        # Same image preprocessing as during training.
        image = image.convert("L")
        image = image.resize((32, 32))
        image_array = np.array(image, dtype=np.float32) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        try:
            model = get_model()
            prediction = model.predict(image_array, verbose=0)
            predicted_age = float(prediction[0][0])
            st.success(f"Predicted age: {round(predicted_age)} years")
            st.caption("This is an estimate and may not match the person's actual age.")
        except Exception as error:
            st.error(f"Prediction failed: {error}")
