🧠Brain Tumor Classification Using CNN



📌PROJECT OVERVIEW

&#x20;This project is a deep learning-based Brain Tumor Classification System that uses Convolutional Neural Networks (CNN) to classify MRI brain images into four categories:



* Glioma
* Meningioma
* No Tumor
* Pituitary



The trained CNN model is integrated with a Streamlit web application, allowing users to upload an MRI image and receive a predicted tumor category along with the prediction confidence.



🎯PROJECT OBJECTIVE

The objective of this project is to develop an image classification model that can automatically identify different types of brain tumors from MRI images.



The project demonstrates the complete machine learning Workflow:

→ Data

→ Preprocessing

→ CNN Model

→ Training

→ Evaluation

→ Prediction

→ Web Deployment



📂DATASET

The dataset contains MRI brain images organized into four classes:



Class	        Description

Glioma  	Glioma tumor MRI images

Meningioma	Meningioma tumor MRI images

No Tumor	MRI images without a tumor

Pituitary	Pituitary tumor MRI images



Images are resized to 224 × 224 pixels and processed as RGB images before being provided to the CNN model.



💡CNN MODEL ARCHITECTURE

The model was developed using TensorFlow/Keras.



The main architecture includes:



* Input Layer – 224 × 224 × 3
* Convolutional Layer – 32 filters
* Max Pooling Layer
* Convolutional Layer – 64 filters
* Max Pooling Layer
* Convolutional Layer – 128 filters
* Max Pooling Layer
* Classification layer for four classes

The model was trained using the Adam optimizer and categorical classification loss.



📊MODEL PERFORMANCE

After training for 10 epochs:



Training Accuracy: 98.39%

Validation Accuracy: 86.00%

Training Loss: 0.0852

Validation Loss: 0.8329



The difference between training and validation accuracy indicates that the model has some overfitting, which can be further improved using techniques such as data augmentation, dropout, and regularization.



🌐STREAMLIT WEB APPLICATION

The trained model is integrated into a Streamlit application.



The application allows users to:



1. Upload an MRI brain image.
2. Preprocess the image automatically.
3. Pass the image through the trained CNN model.
4. Display the predicted tumor category.
5. Display the prediction confidence.



Work flow

**Upload MRI Image → CNN Model → Prediction → Confidence Score**



TECHNOLOGIES USED

* Python
* TensorFlow
* Keras
* NumPy
* Pandas
* Matplotlib
* Scikit-learn
* Streamlit
* Jupyter Notebook
* Git \& GitHub



📁PROJECT STRUCTURE

Brain\_Tumor\_Classification\_CNN/

\_\_CNN\_model\_braintumordetection.ipynb

\_\_app.py

\_\_requirements.txt

\_\_.gitignore

\_\_README.md

\_\_Brain\_tumor\_cnn.keras



Note: The trained .keras model file is not stored directly in this GitHub repository because GitHub has a 100 MB limit for individual files. The model is kept separately and is required when running the Streamlit application locally.



▶️HOW TO RUN THE PROJECT

1.Clone the Repository

git clone https://github.com/sravanisaibaba/Brain\_Tumor\_Classification\_CNN.git

2.Open the Project Folder

cd Brain\_Tumor\_Classifiction\_CNN

3.Create a Virtual environment

python -m venv venv

4.Activate the virtual environment

windows:

venv\\Scripts\\activate

5.Install dependencies

pip install -r requirements.txt

6.Add the trained model

place the trained:

Brain\_tumor\_cnn.keras

file inside the project folder.

7.Run the streamlit application

streamlit run app.py

The application will be open in your browser.



APPLICATION SCREENSHOTS

Screenshots of the Streamlit application added here to demonstrate:

Application Home Page

!\[Application Home Page](screenshots/home.png)

MRI image upload

!\[MRI Image Upload](screenshots/upload.png)

prediction result and Confidence score

!\[Prediction Result and Confidence Score](screenshots/prediction.png)





🧑‍💻FUTURE IMPROVEMENTS

&#x20;Future improvements may include:



* Data augmentation
* Dropout and regularization
* Transfer learning using models such as VGG16,ResNet or EfficientNet
* Improved validation accuracy
* Confusion matrix and classification report
* Model explainability using Grad-CAM
* Cloud deployment
* External model hosting for the trained .keras file



⚠️DISCLAIMER

This project is developed for educational and demonstration purposes.

It is not intended to replace professional medical diagnosis or clinical decision-making.



🧑‍💻Author

SravaniKedekar

Aspiring Data Analyst/Data Science Professional

