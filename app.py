# ✅ STEP 1: Cài đặt môi trường Python

# Tạo môi trường ảo (tuỳ chọn, nhưng nên dùng)
# python -m venv venv
# venv\Scripts\activate (Windows) hoặc source venv/bin/activate (Mac/Linux)

# Cài thư viện cần thiết:
# pip install streamlit PyMuPDF deep-translator

# ✅ STEP 2: Tạo file app.py

import streamlit as st
import fitz  # PyMuPDF
from deep_translator import GoogleTranslator

st.set_page_config(page_title="PDF Translator (EN→VI)", layout="wide")
st.title("📘 Dịch tài liệu PDF từ tiếng Anh sang tiếng Việt")

uploaded_file = st.file_uploader("Tải lên file PDF tiếng Anh:", type="pdf")

if uploaded_file:
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    total_pages = len(pdf_doc)

    page_number = st.number_input("Chọn trang để đọc và dịch:", min_value=1, max_value=total_pages, value=1)
    page = pdf_doc[page_number - 1]
    text_en = page.get_text()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**📄 Nội dung gốc (EN):**")
        st.text_area("", value=text_en, height=500, key="en_text", label_visibility="collapsed")

    with col2:
        st.markdown("**🌐 Bản dịch tiếng Việt (Google Translate):**")
        if text_en.strip() != "":
            with st.spinner("⏳ Đang dịch bằng Google Translate..."):
                try:
                    translated = GoogleTranslator(source='en', target='vi').translate(text_en)
                    st.text_area("", value=translated, height=500, key="vi_text", label_visibility="collapsed")
                except Exception as e:
                    st.error(f"Lỗi khi dịch: {e}")
        else:
            st.warning("Không có nội dung để dịch.")

# ✅ STEP 3: Chạy ứng dụng
# streamlit run app.py

# ✅ STEP 4: Đưa lên GitHub
# - Tạo repo GitHub
# - Thêm file app.py
# - Tạo file requirements.txt chứa:
# streamlit
# PyMuPDF
# deep-translator

# ✅ Bổ sung file .gitignore:
# __pycache__/
# *.pyc
# venv/
# .streamlit/secrets.toml
