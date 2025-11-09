# Proyek UTS Machine Learning: Analisis Sentimen IMDb

Ini adalah repositori untuk proyek Ujian Tengah Semester mata kuliah Machine Learning.

## 📝 Deskripsi Proyek
Aplikasi ini adalah sistem analisis sentimen yang dilatih pada dataset IMDb 50k Movie Reviews.
Tujuan dari aplikasi ini adalah untuk memprediksi apakah sebuah ulasan film memiliki sentimen positif atau negatif.

## 🤖 Model
Model yang digunakan untuk deployment adalah **Logistic Regression**, yang dilatih menggunakan fitur **TF-IDF**.
Model ini dipilih karena memberikan akurasi yang solid (sekitar 89-90%) dengan ukuran file yang kecil dan kecepatan prediksi yang sangat tinggi, ideal untuk deployment web.

## 💻 Teknologi (Laporan Poin 7)
* **Bahasa:** Python
* **Training:** Google Colab, Scikit-learn, TensorFlow/Keras, NLTK, Pandas
* **Deployment:** Streamlit
* **Hosting:** (Nanti diisi Hugging Face Spaces atau Streamlit Cloud)

## 🚀 Cara Menjalankan
1. Clone repositori ini.
2. Pastikan Python ter-install.
3. Install semua library dengan `pip install -r requirements.txt`.
4. Jalankan aplikasi dengan `streamlit run app.py`.