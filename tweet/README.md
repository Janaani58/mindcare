# 🔹 Depression Detection App

A web-based application using Python Flask that detects early signs of depression from user input text. The system accepts user text (simulating social media posts), processes it using a machine learning model, and classifies the emotional state.

## 📋 Project Description

Build a web-based application using Python Flask that detects early signs of depression from user input text. The system should accept user text (simulating social media posts), process it using a machine learning model (such as an Attention-based Bi-LSTM), and classify the emotional state. The application should display a depression risk score along with simple feedback. The UI should be clean and user-friendly using HTML and CSS. The backend should handle prediction logic and return results dynamically.

## 📁 Folder Structure

```
project/
│
├── app.py
├── templates/
│     └── index.html
├── static/
│     └── style.css
└── README.md
```

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install flask
```

### 2. Run the application

```bash
python app.py
```

### 3. Open in browser

Navigate to:
```
http://127.0.0.1:5000
```

## 🎨 Features

- ✅ Clean, user-friendly UI
- ✅ Real-time text analysis
- ✅ Risk classification (Low, Moderate, High)
- ✅ Responsive design
- ✅ Easy backend integration

## 🔧 Next Steps (Important 🚀)

Currently, this uses **dummy keyword-based logic** for demonstration.

To make it production-ready with your ML model:

1. **Replace the `predict_depression()` function** with your actual model
2. **Load your trained Bi-LSTM model** using:

```python
from tensorflow.keras.models import load_model

# Load your model
model = load_model('your_model.h5')

def predict_depression(text):
    # Tokenize and preprocess text
    # Pass through model for prediction
    # Return risk classification
    pass
```

3. **Add tokenization** (if using Bi-LSTM):

```python
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
```

## 📦 Requirements

- Python 3.7+
- Flask
- TensorFlow/Keras (for ML model integration)

## 📝 License

This is a starter template for educational purposes.
