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

Skewed Data: The age distribution is imbalanced, which may affect training and reduce prediction accuracy for underrepresented age groups.

Incorrect Labels: Some images have inaccurate age labels, which can negatively affect model performance.

Data Cleaning: A complete review and correction of mislabeled images was not feasible due to the significant time required.

Image Quality: Lighting, facial angles, and image quality may affect prediction accuracy.
