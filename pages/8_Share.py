import streamlit as st
from tools.settings import QR_CODE_PATH, PAGE_URL

st.set_page_config(page_title="Delivery Game", page_icon=":game_die:")

st.title("Share This Game")


st.image(QR_CODE_PATH, use_column_width=False, width=200, caption="Scan to play on your phone")

st.markdown(f"[{PAGE_URL}]({PAGE_URL})")

