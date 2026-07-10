import streamlit as st
import os
import time
from ultralytics import YOLO
from PIL import Image

st.set_page_config(layout="wide")
st.title("Simulasi Komparasi Eksperimen Computer Vision")
st.subheader("Studi Kasus: Deteksi Barang Bawaan (Backpack/Luggage)")

# Load model lokal
model_v8 = YOLO('best_yolov8_final.pt')
model_v11 = YOLO('best_yolov11_final.pt')

# Sudah diperbaiki menjadi st.file_uploader
uploaded_file = st.file_uploader("Upload Foto Uji", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Simpan sementara
    img = Image.open(uploaded_file)
    img_path = "temp_image.jpg"
    img.save(img_path)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image(img, caption="Foto Asli", use_container_width=True)
        
    with col2:
        start = time.time()
        res_v8 = model_v8(img_path, conf=0.50)
        t_v8 = round((time.time() - start) * 1000, 2)
        res_v8[0].save("v8_out.jpg")
        st.image("v8_out.jpg", caption=f"Hasil YOLOv8 ({t_v8} ms)", use_container_width=True)
        
    with col3:
        start = time.time()
        res_v11 = model_v11(img_path, conf=0.50)
        t_v11 = round((time.time() - start) * 1000, 2)
        res_v11[0].save("v11_out.jpg")
        st.image("v11_out.jpg", caption=f"Hasil YOLO11 ({t_v11} ms)", use_container_width=True)
