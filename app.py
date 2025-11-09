import streamlit as st
import joblib
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import os

# ----------------------------------------------------------------------
# BAGIAN INI HARUS SAMA PERSIS DENGAN DI COLAB
# ----------------------------------------------------------------------

# Download NLTK resources (penting untuk server deployment)
# Kita sembunyikan outputnya agar tidak muncul di web
@st.cache_resource
def download_nltk_resources():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('punkt_tab')
    print("NLTK resources downloaded.")

download_nltk_resources()

# Definisikan stopwords dan lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Fungsi preprocessing (HARUS SAMA PERSIS dengan di Colab)
def preprocess_text(text):
    # (4a) Pembersihan data: Hapus tag HTML
    text = re.sub(r'<[^>]+>', '', text)
    # (4a) Pembersihan data: Hapus non-alfabet dan (4b) Normalisasi
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())
    # (4b) Tokenisasi
    tokens = nltk.word_tokenize(text)
    # (4b) Hapus stopwords dan Lemmatization
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return " ".join(cleaned_tokens)

# ----------------------------------------------------------------------
# BAGIAN MEMUAT MODEL
# ----------------------------------------------------------------------

# Path ke file model dan vectorizer
MODEL_PATH = 'sentiment_model_lr.pkl'
VECTORIZER_PATH = 'tfidf_vectorizer.pkl'

# Fungsi untuk memuat model (agar di-cache)
@st.cache_resource
def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        vectorizer = joblib.load(VECTORIZER_PATH)
        return model, vectorizer
    except FileNotFoundError:
        return None, None
    except Exception as e:
        st.error(f"Error saat memuat model: {e}")
        return None, None

# Muat model dan vectorizer
model, vectorizer = load_model()

# ----------------------------------------------------------------------
# BAGIAN TAMPILAN WEB (USER INTERFACE)
# (Untuk Laporan Poin 8.b.i)
# ----------------------------------------------------------------------

st.set_page_config(page_title="Analisis Sentimen IMDb", page_icon="🎬")
st.title("🎬 Analisis Sentimen Ulasan Film IMDb")
st.caption("Dibuat menggunakan Logistic Regression & Streamlit")
st.markdown("---")

if model is None or vectorizer is None:
    st.error(f"Gagal memuat file model! Pastikan file `{MODEL_PATH}` dan `{VECTORIZER_PATH}` ada di folder yang sama dengan `app.py`.")
else:
    # Area input teks
    user_input = st.text_area("Masukkan ulasan film Anda di sini:", 
                              height=150, 
                              placeholder="Contoh: This movie was fantastic! The acting was superb...")

    # Tombol Analisis
    if st.button("Analisis Sentimen", type="primary"):
        if user_input:
            # (Untuk Laporan Poin 8.b.ii - Contoh Input & Output)
            
            # 1. Preprocess input
            with st.spinner('Membersihkan teks...'):
                cleaned_input = preprocess_text(user_input)
            
            # 2. Vectorize input
            with st.spinner('Mengubah teks menjadi vektor...'):
                vectorized_input = vectorizer.transform([cleaned_input])
            
            # 3. Prediksi
            with st.spinner('Memprediksi sentimen...'):
                prediction = model.predict(vectorized_input)
                probability = model.predict_proba(vectorized_input)
            
            # 4. Tampilkan hasil
            st.markdown("---")
            st.subheader("Hasil Analisis:")
            
            if prediction[0] == 1:
                prob_percent = probability[0][1] * 100
                st.success(f"**SENTIMEN: POSITIF** (Tingkat keyakinan: {prob_percent:.2f}%)")
                st.balloons()
            else:
                prob_percent = probability[0][0] * 100
                st.error(f"**SENTIMEN: NEGATIF** (Tingkat keyakinan: {prob_percent:.2f}%)")
        else:
            st.warning("Mohon masukkan ulasan terlebih dahulu.")