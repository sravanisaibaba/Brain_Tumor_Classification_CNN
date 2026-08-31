import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

model=load_model("Brain_Tumor_cnn.keras")

#class names
class_names=["glioma",
             "meningioma",
             "notumor",
             "pituitary"
]

#Title
st.title("🧠 Brain Tumor Dection Using CNN")
#Upload image
uploaded_file=st.file_uploader(
    "Upload an MRI Scan Image to classify brain tumor",
    type=["jpg","jpg","png"]
)


if uploaded_file is not None:
    img=Image.open(uploaded_file).convert("RGB")
    st.image(img,caption="Uploaded MRI Image",use_container_width=True)
    img=img.resize((224,224))
    img_array=image.img_to_array(img)
    img_array=img_array/255.0
    img_array=np.expand_dims(img_array,axis=0)
    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    confidence = np.max(prediction) * 100

    st.success(f"Prediction:{class_names[predicted_index]}")
    st.info(f"Confidence:{confidence:2f}%")

   
 