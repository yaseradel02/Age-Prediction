# Age Prediction Using ANN

## Overview
A deep learning project that predicts a person's age from a facial image using an Artificial Neural Network (ANN). The model is deployed through a Streamlit web application.

## Dataset
- **Dataset:** [UTKFace – Kaggle](https://www.kaggle.com/datasets/jangedoo/utkface-new/data)
- Contains over 20,000 facial images with age, gender, and race labels.
- Images were resized to 32×32 pixels, converted to grayscale, and normalized.

## Model
- **Algorithm:** Artificial Neural Network (ANN)
- **Hidden Layers:** Dense layers with ReLU activation
- **Regularization:** Dropout
- **Optimizer:** Adam
- **Loss Function:** Mean Absolute Error (MAE)
- **Data Split:** 70% Training, 15% Validation, 15% Testing

## Streamlit App
The application allows users to:
- Upload a facial image.
- Take a picture using their webcam.
- Predict the person's estimated age.

## How to Run
1. Clone or download the repository.
2. Install the required libraries:

   `pip install -r requirements.txt`

3. Make sure `age_model.keras` is in the same folder as `app.py`.
4. Run the application:

   `streamlit run app.py`

## Limitations
- Predictions may be affected by lighting, image quality, and facial angles.
- The model may produce inaccurate predictions for certain age groups.
- The application is designed for educational purposes.

## Tools Used
Python, TensorFlow, Keras, Pandas, NumPy, Scikit-learn, Pillow, and Streamlit.
