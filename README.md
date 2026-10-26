# UTKFace Age Prediction

A deep learning project that predicts a person's age from a facial image using an **Artificial Neural Network (ANN)**.

**Live App:** [Try the Age Prediction App](https://utkface-age-prediction.streamlit.app/)

## Dataset & Model
- **Dataset:** [UTKFace (Kaggle)](https://www.kaggle.com/datasets/jangedoo/utkface-new/data)
- **Preprocessing:** 32 × 32 grayscale images, normalized to 0–1
- **Model:** ANN using Keras, ReLU, Dropout, and Adam
- **Test MAE:** 8.64 years

## App Features
- Upload a face image or take a photo using a webcam.
- Get an estimated age prediction.

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Place the trained `age_model.keras` file in the same folder as `app.py`.

## Limitations
Predictions may be affected by lighting, image angles, and image quality. This project is for educational purposes.
