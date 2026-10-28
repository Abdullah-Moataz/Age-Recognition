# 🎂 Age Prediction Using CNN

A deep learning web application that predicts a person's approximate age from a facial image using a **Convolutional Neural Network (CNN)**.

The model was trained on the **UTKFace dataset** and deployed using **Streamlit**, allowing users to upload an image or capture a photo directly from their camera.

### 🚀 Live Demo

**[Try the Age Prediction App](https://age-recognition-2fjqgnnkozxxykrpgxhden.streamlit.app/)**

## 📌 Project Overview

This project explores **age estimation using deep learning**.

Unlike age-group classification, the model uses **regression** to predict a numerical age rather than assigning a person to a predefined age category.

The application provides two input methods:
- 📁 **Upload Image:** Select a facial image from your device.
- 📸 **Take Photo:** Capture a photo directly using your camera.

## 📊 Dataset

The project uses the **UTKFace dataset**, which contains over 20,000 facial images with ages ranging from 0 to 116 years.

Each image filename includes information about:
- Age
- Gender
- Ethnicity

For this project, only **age** is used as the prediction target.

### Data Preprocessing

1. Extract age labels from image filenames.
2. Resize images to **48 × 48 pixels**.
3. Convert images to RGB format.
4. Normalize pixel values to the range **0–1**.
5. Split the dataset into training and validation sets.

## 🧠 CNN Architecture

The model uses a Convolutional Neural Network to extract facial features and estimate age.

**Model Pipeline:**

`Input Image → Conv2D → MaxPooling2D → Conv2D → MaxPooling2D → Feature Extraction → Dense Layers → Predicted Age`

### Model Configuration

| Parameter | Value |
|---|---|
| Model Type | CNN |
| Task | Age Regression |
| Input Shape | 48 × 48 × 3 |
| Optimizer | Adam |
| Loss Function | MAE |
| Evaluation Metric | MAE |
| Output | Predicted Age |

## 📈 Model Performance

The initial model achieved a validation **Mean Absolute Error (MAE) of approximately 14.42 years**.

This means the model's predictions differ from actual ages by approximately 14 years on average.

The model is an educational implementation, and its predictions should be treated as estimates rather than accurate age measurements.

## 🛠️ Technologies Used

- **Python** — Programming language
- **TensorFlow / Keras** — CNN development and training
- **NumPy** — Numerical operations
- **Scikit-learn** — Dataset splitting and evaluation
- **Pillow** — Image preprocessing
- **Matplotlib** — Training visualization
- **Streamlit** — Web application development
- **Google Colab** — Model training

## 💻 Running Locally

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/age-recognition.git
cd age-recognition
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run age.py
```

Make sure the trained model file (`age_model.keras`) is available in the project directory.

## 🔮 Future Improvements

- Improve model performance by experimenting with additional CNN layers.
- Apply data augmentation to improve generalization.
- Experiment with transfer learning using pretrained models.
- Add automatic face detection and cropping.
- Improve age prediction accuracy through hyperparameter tuning.

## 📝 Conclusion

This project demonstrates how CNNs can be applied to facial age estimation using regression.

It also provides practical experience in image preprocessing, deep learning model training, evaluation, and deployment through an interactive Streamlit application.

**Note:** The application is intended for educational purposes.
