import os
import time
from flask import Flask, render_template, request
from ultralytics import YOLO

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load kedua model sesuai dengan nama file asli Anda
model_v8 = YOLO('best_yolov8_final.pt')
model_v11 = YOLO('best_yolov11_final.pt')  # Sudah diperbaiki dengan huruf 'v'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "Tidak ada file yang diunggah"
        file = request.files['file']
        if file.filename == '':
            return "Nama file kosong"
        
        if file:
            # 1. Simpan foto asli dari user
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # 2. Jalankan Prediksi YOLOv8 & Hitung Waktu Kecepatannya
            start_v8 = time.time()
            res_v8 = model_v8(filepath)
            time_v8 = round((time.time() - start_v8) * 1000, 2)
            
            output_v8 = 'v8_' + file.filename
            res_v8[0].save(filename=os.path.join(app.config['UPLOAD_FOLDER'], output_v8))
            
            # 3. Jalankan Prediksi YOLOv11 & Hitung Waktu Kecepatannya
            start_v11 = time.time()
            res_v11 = model_v11(filepath)
            time_v11 = round((time.time() - start_v11) * 1000, 2)
            
            output_v11 = 'v11_' + file.filename
            res_v11[0].save(filename=os.path.join(app.config['UPLOAD_FOLDER'], output_filename := output_v11))
            
            return render_template('index.html', 
                                   original=file.filename, 
                                   pred_v8=output_v8, time_v8=time_v8,
                                   pred_v11=output_v11, time_v11=time_v11)
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)