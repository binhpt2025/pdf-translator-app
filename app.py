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

# Khởi tạo trạng thái trang
if "page_number" not in st.session_state:
    st.session_state.page_number = 1

uploaded_file = st.file_uploader("Tải lên file PDF tiếng Anh:", type="pdf")

if uploaded_file:
    pdf_doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    total_pages = len(pdf_doc)

    # Xử lý nút Prev / Next
    col_nav1, col_nav2 = st.columns([1, 1])
    with col_nav1:
        if st.button("⬅️ Prev page"):
            if st.session_state.page_number > 1:
                st.session_state.page_number -= 1
    with col_nav2:
        if st.button("Next page ➡️"):
            if st.session_state.page_number < total_pages:
                st.session_state.page_number += 1

    # Lấy nội dung trang hiện tại
    page_number = st.session_state.page_number
    page = pdf_doc[page_number - 1]
    html_text = page.get_text("html")
    text_plain = page.get_text()

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"**📄 Trang {page_number} / {total_pages}**")
        st.markdown("<div style='font-size:20pt; line-height:2.0;'>" + html_text + "</div>", unsafe_allow_html=True)

    with col2:
        st.markdown(f"**🌐 Bản dịch tiếng Việt (Trang {page_number}):**")
        if text_plain.strip() != "":
            with st.spinner("⏳ Đang dịch bằng Google Translate..."):
                try:
                    translated = GoogleTranslator(source='en', target='vi').translate(text_plain)
                    st.markdown(f"<div style='font-size:20pt; line-height:2.0;'>{translated}</div>", unsafe_allow_html=True)
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
