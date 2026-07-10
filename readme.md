# Comparative Analysis of YOLOv8 and YOLO11 for Baggage Detection

Aplikasi simulasi berbasis web (Flask) untuk membandingkan performa akurasi dan kecepatan inferensi antara dua generasi algoritma Object Detection: **YOLOv8** dan **YOLO11** (Studi Kasus: Deteksi Barang Bawaan / Backpack & Luggage). Proyek ini ditujukan untuk memenuhi eksperimen Penulisan Ilmiah / Tugas Akhir di Universitas Gunadarma.

## 🚀 Fitur Utama
- **Dual-Model Inference:** Menjalankan prediksi objek menggunakan dua arsitektur model berbeda secara bersamaan dalam satu kali klik.
- **Inference Time Comparison:** Menghitung dan menampilkan waktu komputasi (dalam milidetik) secara *real-time* berbasis CPU lokal.
- **Interactive Web UI:** Antarmuka web responsif dan bersih untuk mempermudah proses demonstrasi di depan dosen penguji.

## 📊 Hasil Eksperimen (Matriks Evaluasi)
Eksperimen dilakukan menggunakan dua skenario data uji: Skenario 1 (Baseline 200 Citra) dan Skenario 2 (Fine-Tuning Upgrade 963 Citra) dengan hasil sebagai berikut:

| Algoritma | Dataset | Epoch | Precision | Recall | mAP50 | Kecepatan (CPU) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **YOLOv8 Baseline** | 200 Citra | 20 | 65.6% | 47.6% | 54.8% | ~3.2 ms |
| **YOLO11 Baseline** | 200 Citra | 20 | 71.1% | 42.7% | 51.4% | ~4.1 ms |
| **YOLOv8 Final** | 963 Citra | 50 | **99.5%** | **99.9%** | 99.0% | **~3.6 ms** |
| **YOLO11 Final** | 963 Citra | 50 | 98.5% | 99.8% | **99.4%** | ~5.2 ms |

## 🛠️ Cara Instalasi & Menjalankan di Lokal

### 1. Clone Repositori
git clone [https://github.com/USERNAME_ANDA/NAMA_REPO_ANDA.git](https://github.com/USERNAME_ANDA/NAMA_REPO_ANDA.git)
cd NAMA_REPO_ANDA

### 2. Install Dependencies
Pastikan Python sudah terinstall di perangkat Anda, lalu jalankan perintah:
pip install flask ultralytics torch torchvision

### 3. Jalankan Aplikasi
python app.py
Buka browser Anda dan akses alamat http://127.0.0.1:5000.

### 📊 Hasil Eksperimen & Metrik EvaluasiPengujian dilakukan secara adil (fair comparison) melalui dua tahap: Tahap Baseline (200 citra, 20 epoch) dan Tahap Upgrade Fine-Tuning (963 citra, 50 epoch). Berikut adalah rekapitulasi data performa kedua model:Arsitektur ModelDatasetEpochPrecisionRecallmAP50Waktu Inferensi (CPU)YOLOv8 (Baseline)200 Citra2065.6%47.6%54.8%~3.2 msYOLO11 (Baseline)200 Citra2071.1%42.7%51.4%~4.1 msYOLOv8 (Final)963 Citra5099.5%99.9%99.0%~3.6 msYOLO11 (Final)963 Citra5098.5%99.8%99.4%~5.2 msAnalisis Singkat untuk Sidang:Peningkatan Skala Data: Penambahan data dari 200 menjadi 963 citra (melalui teknik augmentasi Roboflow) terbukti mendongkrak nilai akurasi (mAP50) kedua model dari kisaran 50% menjadi 99%.Komparasi Model Final: YOLOv8 unggul sangat tipis pada nilai kedekatan tebakan (Precision 99.5%) dan kecepatan komputasi. Namun, YOLO11 terbukti memiliki arsitektur yang lebih stabil dalam mengenali batas objek spasial (mAP50 99.4%) serta lebih kebal terhadap masalah False Positive (halusinasi objek latar belakang).🛠️ Cara Menjalankan Aplikasi di Lokal (Laptop)
