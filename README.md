# 🩺 Smart Dermatology – AI-Powered Skin Disease Detection System

A machine learning-based skin disease detection application developed using Python, TensorFlow/Keras, OpenCV, and Scikit-learn. The system analyzes skin lesion images and predicts potential skin diseases using trained CNN and SVM models through an interactive desktop GUI.

This project demonstrates image preprocessing, deep learning model development, machine learning classification, medical image analysis, and desktop application integration.

---

## 📊 Project Overview

The objective of this project is to assist in the early detection of skin diseases by analyzing uploaded skin images and providing disease predictions through a user-friendly graphical interface.

The application supports:

* Image-based skin disease detection
* CNN-based classification
* SVM-based classification
* Interactive desktop GUI
* Automated image preprocessing
* Disease prediction and diagnosis support

---

## ✅ Key Highlights

* 🧠 Convolutional Neural Network (CNN) implementation
* 📈 Support Vector Machine (SVM) classification
* 🖼️ Image preprocessing and feature extraction
* 🩺 Skin disease prediction system
* ⚡ Real-time diagnosis through GUI
* 📊 Model evaluation and comparison
* 💾 Pre-trained model deployment using TensorFlow
* 🎯 User-friendly desktop application

---

## 🧰 Tech Stack

### Machine Learning & Deep Learning

* Python
* TensorFlow
* Keras
* Scikit-learn
* NumPy
* Pandas

### Image Processing

* OpenCV
* Pillow

### Visualization

* Matplotlib

### Desktop Application

* Tkinter

---

## 🔬 Project Workflow

### 1. 📂 Dataset Preparation

A skin disease image dataset was collected and organized into training and testing sets.

The preprocessing pipeline includes:

* Image loading
* Image resizing
* Normalization
* Data preparation for model training
* Dataset visualization and analysis

---

### 2. 🧠 CNN Model Development

A Convolutional Neural Network was designed and trained to identify skin diseases from image inputs.

Model capabilities include:

* Feature extraction using convolution layers
* Pattern learning from skin lesion images
* Disease classification
* Prediction generation

The trained model was exported as:

```text
model.h5
```

for deployment within the application.

---

### 3. 📈 SVM Model Development

A Support Vector Machine model was trained and evaluated alongside the CNN model.

Key objectives:

* Feature-based classification
* Performance comparison with CNN
* Alternative prediction approach

The trained model was saved as:

```text
svm_model.pkl
```

---

### 4. 🖥️ Desktop Application Integration

The trained models were integrated into a graphical desktop application.

Application features include:

* Image upload functionality
* Disease diagnosis
* Prediction display
* Interactive user interface
* Fast local execution

Workflow:

1. User selects an image.
2. Image is preprocessed.
3. Model performs prediction.
4. Predicted disease is displayed.
5. Diagnosis information is presented to the user.

---

## 📈 Features Implemented

### Data Processing

* Image preprocessing
* Dataset preparation
* Data visualization

### Machine Learning

* CNN training
* SVM training
* Model comparison

### Application Development

* Desktop GUI implementation
* Image upload system
* Prediction engine
* Result visualization

### Deployment

* Model serialization
* Local application deployment
* Pre-trained model integration

---

## 📁 Project Structure

```text
Smart-Dermatology
│
├── Smart_Dermatology.py
├── model.h5
├── svm_model.pkl
├── README.md
│
├── Practice_Model
│   ├── PracticeModels.ipynb
│
├── Readme_images
│   ├── DatasetPlot.png
│   ├── Datasetdf.png
│   ├── ModelArch.png
│   ├── ModelEvaluation.png
│   └── Samleimagefromdataset.png
│
├── Skin Cancer Detector.ipynb
├── Skin Disease Detection CNN.ipynb
├── Skin Disease Detection SVM.ipynb
├── Compare model.ipynb
└── using SVM.ipynb
```

---

## ▶️ Running the Project

### Install Dependencies

```bash
pip install tensorflow keras numpy pandas matplotlib pillow scikit-learn opencv-python
```

### Run Application

```bash
python Smart_Dermatology.py
```

### Application Workflow

1. Launch the application.
2. Click **Choose** to select a skin image.
3. Click **Diagnose**.
4. View the predicted skin disease.

---

## 📊 Model Components

### CNN Model

* Deep learning-based image classification
* Trained using TensorFlow/Keras
* Saved as `model.h5`

### SVM Model

* Machine learning classification model
* Trained using Scikit-learn
* Saved as `svm_model.pkl`

---

## 🚀 Future Improvements

* Higher accuracy through larger datasets
* Multi-disease classification support
* Cloud deployment
* Web-based interface
* Explainable AI visualizations
* Mobile application integration
* Real-time dermatologist assistance

---

## 📬 Contact

Made with ❤️ by **Bishwaman Das**
