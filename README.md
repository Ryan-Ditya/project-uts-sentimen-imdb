# 🎬 Proyek UTS Machine Learning: Analisis Sentimen IMDb

Ini adalah repositori untuk proyek Ujian Tengah Semester mata kuliah Machine Learning.

## 🧑‍💻 Tim Pelaksana
**Nama Tim:** CHINTA’S PROPERTY

| NIM | Nama Mahasiswa | Peran |
| :--- | :--- | :--- |
| 221112635 | Rizki Anwar Nasution | Ketua |
| 221111648 | Muhammad Fauzi Hasibuan | Anggota |
| 221112003 | Mhd Ryan Ditya | Anggota |

---

## 📝 Deskripsi Proyek
Aplikasi ini adalah sistem **Analisis Sentimen** yang dilatih pada dataset IMDb 50k Movie Reviews. Tujuan dari sistem ini adalah untuk mengklasifikasikan (memprediksi) apakah sebuah ulasan film memiliki sentimen **positif** atau **negatif**.

## 🤖 Model
Model yang digunakan untuk proyek ini dan diimplementasikan dalam demo adalah **Multinomial Naive Bayes (MNB)**, yang dilatih menggunakan fitur **TF-IDF**.

Model ini dipilih karena:
1.  Konsistensi dengan judul proyek (Multinomial Naive Bayes).
2.  Memberikan akurasi yang sangat tinggi ($\mathbf{90.37\%}$) setelah optimasi fitur.
3.  Memiliki kecepatan prediksi (*inference*) yang sangat cepat, ideal untuk *deployment* demo lokal.

## 💻 Teknologi (Laporan Poin 7)
* **Bahasa Pemrograman:** Python
* **Training & Analisis:** Google Colab, Scikit-learn, NLTK, Pandas
* **Aplikasi Demo:** Streamlit
* **File Penting:** Terdapat file `.pkl` yang berisi model dan *vectorizer* yang sudah dilatih.

---

## 🚀 Cara Menjalankan (Demo Lokal)

Ikuti langkah-langkah ini untuk menjalankan aplikasi web demo di komputer lokalmu:

1.  *Clone* repositori ini.
2.  Pastikan **Python** (disarankan versi **3.11**) ter-*install*.
3.  Di *Virtual Environment* (*venv*) proyek, *install* semua *library* yang dibutuhkan:
    ```bash
    pip install -r requirements.txt
    ```
4.  Jalankan aplikasi web demo menggunakan Streamlit:
    ```bash
    streamlit run app.py
    ```
Aplikasi akan terbuka otomatis di *browser* Anda pada alamat `http://localhost:8501`.
