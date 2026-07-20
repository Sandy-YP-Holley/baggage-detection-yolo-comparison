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

