import streamlit as st
from utils import load_data, download_game_board_button
from settings import images_dir

st.title('Rules of the Game')

rules = load_data('rules.md')

download_game_board_button()

st.write(rules)

# Adding a clickable email address
st.markdown('**Send your feedback:** [rdubar@gmail.com](mailto:rdubar@gmail.com)', unsafe_allow_html=True)